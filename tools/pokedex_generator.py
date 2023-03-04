"""
Stand alone script to generate pokedex json for infinite fusion
As of 3/3/2023 there are only 420 base pokemon in infinite fusion.
The first 251 are from gen 1+2 and the last 169 are picked between gen 3 and 7.

This script will call the pokemon api to get the offical numbers for the first 251 pokemon
Then it will use a hard coded table for the last 169 from the '169.csv' file.
"""

import requests
import json
import csv


def get_first_251() -> dict:
    dex = {}
    for id in range(1,252):
        try:
            pokemon_info = get_pokemon_info(id)
            dex[pokemon_info[0]] = pokemon_info[1]
            
        except InvalidPokemon as pokemon:
            print(f"{pokemon} is invalid.")
    return dex

	# "bulbasaur": {
	# 	"fid": 1,
    #   "oid": 1
	# 	"dname": "Bulbasaur"
	# },

def get_second_169() -> dict:
    dex = {}
    with open('data/169.csv') as csvfile:
        fusion_dex = csv.reader(csvfile, delimiter='\t')
        for row in fusion_dex:
            fid = row[0]
            dname = row[1]
            # print(fid, dname)
            try:
                pokemon_info = get_pokemon_info(dname, fid)
                dex[pokemon_info[0]] = pokemon_info[1]
            except InvalidPokemon as pokemon:
                print(f"{pokemon} is invalid.")
    return dex


def special_cases(pokemon: str) -> dict:
    """
    Special cases for pokemon info.
    """
    special_cases = [
        "Mime Jr.",
        "Aegislash",
        "Giratina",
        "Mimikyu",
        "Deoxys"
    ]
    
    if pokemon in special_cases:
        if pokemon == "Mime Jr.":
            return ("mime-jr", {'fid': 258, 'oid': 439, "dname": pokemon})
        elif pokemon == "Aegislash":
            return ("aegislash-shield", {'fid': 329, 'oid': 681, "dname": pokemon})
        elif pokemon == "Giratina":
            return ("giratina-altered", {'fid': 345, 'oid': 487, "dname": pokemon})
        elif pokemon == "Mimikyu":
            return ("mimikyu-disguised", {'fid': 373, 'oid': 778, "dname": pokemon})
        elif pokemon == "Deoxys":
            return ("deoxys-normal", {'fid': 380, 'oid': 386, "dname": pokemon})


def get_pokemon_info(pokemon, fid = False) -> dict:
    """
    'pokemon' param can be str or int.
    'fid' is the fusion dex override, if not passed, it will use the offical dex number
    
    checks if the entry is a valid pokemon, if yes it returns the pokedex number.
    uses https://pokeapi.co/ to determine if pokemon name is valid.
    """

    is_special = special_cases(pokemon)
    if is_special:
        return is_special
    
    if type(pokemon) == str:
        pokemon = pokemon.lower()
    
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')
    if response.status_code == 200:
        mon_data = response.json()
        if not fid: fid = mon_data['id']
        
        return (mon_data['name'], {'fid': int(fid), 'oid': int(mon_data['id']), "dname": str(mon_data['name']).capitalize()})
    else:
        raise InvalidPokemon(f"{pokemon}")

def write_dex(dex: dict):
    json_object = json.dumps(dex, indent=4)
    with open("data/infinite_fusion_pokedex.json", "w") as outfile:
        outfile.write(json_object)

# Error Handling Setup
class InvalidPokemon(Exception):
    pass


def main():
    dex = get_first_251()
    second_169 = get_second_169()
    
    dex.update(second_169)
    
    write_dex(dex)
    print("done")
    

if __name__ == "__main__":
    main()