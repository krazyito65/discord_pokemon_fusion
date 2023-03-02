from typing import Literal, Optional

import discord
import requests
import yaml
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Context, Greedy  # or a subclass of yours

# Loading Base Config
try:
    print("Loading Config...")
    with open("token.yml", 'r') as config_file:
        token = yaml.load(config_file, Loader=yaml.FullLoader)
except Exception as e:
    print("Unable to load token.yml. Make sure you created your configuration.")
    print(f"Exception: {e}")
    exit(1)

## TODO: when i have a 'prod' token
token = token['dev_token']

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = '!', intents=intents)

# Add the guild ids in which the slash command will appear. 
# If it should be in all, remove the argument, 
# but note that it will take some time (up to an hour) to register the command if it's for all guilds.
@bot.tree.command(description="Get the fused pictures of 2 pokemon")
@app_commands.describe(
    mon1='First Pokemon to fuse',
    mon2='2nd Pokemon to fuse')
async def fuse(interaction: discord.Interaction, mon1: str, mon2: str):
    print(f'we got the fuse command')
    
    try:
        mon1_id = get_pokemon_id(mon1)
        mon2_id = get_pokemon_id(mon2)
    except InvalidPokemon as invalid:
        print(f"{interaction.user.name}#{interaction.user.discriminator} passed an invalid pokemon: {invalid}")
        await interaction.response.send_message(f"❗Invalid pokemon entered: {invalid}❗", ephemeral=True)
        return
    
    urls = get_images(mon1_id, mon2_id)
    
    urls[0]["name"] = f"{mon1.capitalize()}/{mon2.capitalize()}"
    if not mon1_id == mon2_id:
        urls[1]["name"] = f"{mon2.capitalize()}/{mon1.capitalize()}"
    else:
        urls = [urls[0]]
    
    embed_list = []
    for url in urls:
        embed = discord.Embed(url="http://foo.bar/")
        embed.set_image(url=url['url'])
        embed_list.append(embed)
        first_embed = embed_list[0]
        first_embed.add_field(name='Name', value=f"{url['name']} - {url['type']}")
    
    await interaction.response.send_message(embeds=embed_list)


def get_pokemon_id(pokemon: str):
    """
    checks if the entry is a valid pokemon, if yes it returns the pokedex number.
    uses https://pokeapi.co/ to determine if pokemon name is valid.
    """
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}')
    if response.status_code == 200:
        mon_data = response.json()
        return mon_data['id']
    else:
        raise InvalidPokemon(f"{pokemon}")

def get_images(mon1: int, mon2: int):    
    return (get_custom_image(mon1, mon2), get_custom_image(mon2, mon1))

def get_custom_image(mon1: int, mon2: int):
    """
    returns a tuple with the urls of a custom image.
    if not found, it will be false.
    https://raw.githubusercontent.com/Aegide/custom-fusion-sprites/main/CustomBattlers/7.74.png | Custom
    """
    sprite = f'https://raw.githubusercontent.com/Aegide/custom-fusion-sprites/main/CustomBattlers/{mon1}.{mon2}.png'

    response = requests.get(sprite)
    if response.status_code == 200:
        return {
                'url': sprite,
                'type': "custom"
                }
    return get_generated_image(mon1, mon2)
    

def get_generated_image(mon1: int, mon2: int):
    """
    returns a tuple with a true or false if there is a generated image.
    if not found, it will be false.
    https://raw.githubusercontent.com/Aegide/autogen-fusion-sprites/master/Battlers/74/74.7.png | Auto gen
    """
    sprite = f'https://raw.githubusercontent.com/Aegide/autogen-fusion-sprites/master/Battlers/{mon1}/{mon1}.{mon2}.png'

    response = requests.get(sprite)
    if response.status_code == 200:
        return {
                'url': sprite,
                'type': "autogen"
                }
    return False


# Error Handling Setup
class InvalidPokemon(Exception):
    pass

@bot.event
async def on_ready():
    print(f'We have logged in as: {bot.user}')


@bot.command()
@commands.guild_only()
@commands.is_owner()
async def sync(ctx: Context, guilds: Greedy[discord.Object], spec: Optional[Literal["local", "copy", "clear"]] = None) -> None:
    """
        This function is used to sync the slash commands.  It is only accessable to the onwer of the bot.
        
        Most often, we will use the 'copy' function to test on a private server, 
            this will sync all the commands we want to use globally (or on other servers) to the test server we invoke from
            Specifically this helps only sync the single server instead of all servers that the bot lives on.

        The 'global' sync will sync all servers the bot lives on with all the 'global' commands.
        
        The 'local' command will only sync the commands specifically tied to the server (will not sync global ones)
        
        'clear' removes all slash commands from the invoked server.
    """
    if not guilds:
        if spec == "local":
            # will only sync the commands specificed to this particular guild
            print("running 'local' please wait...")
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "copy":
            # will copy the 'global' commands (ones without guild parameters) 
            # to this specific guild for local testing
            print("running 'copy' please wait...")
            ctx.bot.tree.copy_global_to(guild=ctx.guild)
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "clear":
            print("running 'clear' please wait...")
            # clears all commands on this specific guild
            ctx.bot.tree.clear_commands(guild=ctx.guild)
            await ctx.bot.tree.sync(guild=ctx.guild)
            synced = []
        else:
            print("running 'global' please wait...")
            # syncs the 'global' list (ones without guild parameters)
            synced = await ctx.bot.tree.sync()

        await ctx.send(
            f"Synced {len(synced)} commands {'globally' if spec is None else 'to the current guild.'}"
        )
        print(f"sync'd {len(synced)} commands using {spec}")
        return
    
    # ??? if we pass in guilds, it only syncs those specific guilds. 
    # No copy function for these.
    ret = 0
    for guild in guilds:
        try:
            await ctx.bot.tree.sync(guild=guild)
        except discord.HTTPException:
            pass
        else:
            ret += 1

    await ctx.send(f"Synced the tree to {ret}/{len(guilds)}.")


bot.run(token)