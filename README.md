# discord_pokemon_fusion

Built using python 3.11

```
python3.11 -m venv venv/
source venv/bin/activate
pip install -r requirements.txt
```

ensure you have a 'token.yml' file with a single entry
```
dev_token: ######
```

----
owner of the application needs to sync the bot.  In a private channe run the following after the bot as been added to needed servers.
```
!sync
```
once sync is completed, the slash command should work
```
/fuse mon1 mon2
```
