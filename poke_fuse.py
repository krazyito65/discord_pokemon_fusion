from typing import Literal, Optional

import discord
import requests
import yaml
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Context, Greedy  # or a subclass of yours
pd_full_collection = {
    "bulbasaur" : { "id" : "1", "name" : "bulbasaur", "dname" : "Bulbasaur" }
    ,"ivysaur" : { "id" : "2", "name" : "ivysaur", "dname" : "Ivysaur" }
    ,"venusaur" : { "id" : "3", "name" : "venusaur", "dname" : "Venusaur" }
    ,"charmander" : { "id" : "4", "name" : "charmander", "dname" : "Charmander" }
    ,"charmeleon" : { "id" : "5", "name" : "charmeleon", "dname" : "Charmeleon" }
    ,"charizard" : { "id" : "6", "name" : "charizard", "dname" : "Charizard" }
    ,"squirtle" : { "id" : "7", "name" : "squirtle", "dname" : "Squirtle" }
    ,"wartortle" : { "id" : "8", "name" : "wartortle", "dname" : "Wartortle" }
    ,"blastoise" : { "id" : "9", "name" : "blastoise", "dname" : "Blastoise" }
    ,"caterpie" : { "id" : "10", "name" : "caterpie", "dname" : "Caterpie" }
    ,"metapod" : { "id" : "11", "name" : "metapod", "dname" : "Metapod" }
    ,"butterfree" : { "id" : "12", "name" : "butterfree", "dname" : "Butterfree" }
    ,"weedle" : { "id" : "13", "name" : "weedle", "dname" : "Weedle" }
    ,"kakuna" : { "id" : "14", "name" : "kakuna", "dname" : "Kakuna" }
    ,"beedrill" : { "id" : "15", "name" : "beedrill", "dname" : "Beedrill" }
    ,"pidgey" : { "id" : "16", "name" : "pidgey", "dname" : "Pidgey" }
    ,"pidgeotto" : { "id" : "17", "name" : "pidgeotto", "dname" : "Pidgeotto" }
    ,"pidgeot" : { "id" : "18", "name" : "pidgeot", "dname" : "Pidgeot" }
    ,"rattata" : { "id" : "19", "name" : "rattata", "dname" : "Rattata" }
    ,"raticate" : { "id" : "20", "name" : "raticate", "dname" : "Raticate" }
    ,"spearow" : { "id" : "21", "name" : "spearow", "dname" : "Spearow" }
    ,"fearow" : { "id" : "22", "name" : "fearow", "dname" : "Fearow" }
    ,"ekans" : { "id" : "23", "name" : "ekans", "dname" : "Ekans" }
    ,"arbok" : { "id" : "24", "name" : "arbok", "dname" : "Arbok" }
    ,"pikachu" : { "id" : "25", "name" : "pikachu", "dname" : "Pikachu" }
    ,"raichu" : { "id" : "26", "name" : "raichu", "dname" : "Raichu" }
    ,"sandshrew" : { "id" : "27", "name" : "sandshrew", "dname" : "Sandshrew" }
    ,"sandslash" : { "id" : "28", "name" : "sandslash", "dname" : "Sandslash" }
    ,"nidorina" : { "id" : "30", "name" : "nidorina", "dname" : "Nidorina" }
    ,"nidoqueen" : { "id" : "31", "name" : "nidoqueen", "dname" : "Nidoqueen" }
    ,"nidorino" : { "id" : "33", "name" : "nidorino", "dname" : "Nidorino" }
    ,"nidoking" : { "id" : "34", "name" : "nidoking", "dname" : "Nidoking" }
    ,"clefairy" : { "id" : "35", "name" : "clefairy", "dname" : "Clefairy" }
    ,"clefable" : { "id" : "36", "name" : "clefable", "dname" : "Clefable" }
    ,"vulpix" : { "id" : "37", "name" : "vulpix", "dname" : "Vulpix" }
    ,"ninetales" : { "id" : "38", "name" : "ninetales", "dname" : "Ninetales" }
    ,"jigglypuff" : { "id" : "39", "name" : "jigglypuff", "dname" : "Jigglypuff" }
    ,"wigglytuff" : { "id" : "40", "name" : "wigglytuff", "dname" : "Wigglytuff" }
    ,"zubat" : { "id" : "41", "name" : "zubat", "dname" : "Zubat" }
    ,"golbat" : { "id" : "42", "name" : "golbat", "dname" : "Golbat" }
    ,"oddish" : { "id" : "43", "name" : "oddish", "dname" : "Oddish" }
    ,"gloom" : { "id" : "44", "name" : "gloom", "dname" : "Gloom" }
    ,"vileplume" : { "id" : "45", "name" : "vileplume", "dname" : "Vileplume" }
    ,"paras" : { "id" : "46", "name" : "paras", "dname" : "Paras" }
    ,"parasect" : { "id" : "47", "name" : "parasect", "dname" : "Parasect" }
    ,"venonat" : { "id" : "48", "name" : "venonat", "dname" : "Venonat" }
    ,"venomoth" : { "id" : "49", "name" : "venomoth", "dname" : "Venomoth" }
    ,"diglett" : { "id" : "50", "name" : "diglett", "dname" : "Diglett" }
    ,"dugtrio" : { "id" : "51", "name" : "dugtrio", "dname" : "Dugtrio" }
    ,"meowth" : { "id" : "52", "name" : "meowth", "dname" : "Meowth" }
    ,"persian" : { "id" : "53", "name" : "persian", "dname" : "Persian" }
    ,"psyduck" : { "id" : "54", "name" : "psyduck", "dname" : "Psyduck" }
    ,"golduck" : { "id" : "55", "name" : "golduck", "dname" : "Golduck" }
    ,"mankey" : { "id" : "56", "name" : "mankey", "dname" : "Mankey" }
    ,"primeape" : { "id" : "57", "name" : "primeape", "dname" : "Primeape" }
    ,"growlithe" : { "id" : "58", "name" : "growlithe", "dname" : "Growlithe" }
    ,"arcanine" : { "id" : "59", "name" : "arcanine", "dname" : "Arcanine" }
    ,"poliwag" : { "id" : "60", "name" : "poliwag", "dname" : "Poliwag" }
    ,"poliwhirl" : { "id" : "61", "name" : "poliwhirl", "dname" : "Poliwhirl" }
    ,"poliwrath" : { "id" : "62", "name" : "poliwrath", "dname" : "Poliwrath" }
    ,"abra" : { "id" : "63", "name" : "abra", "dname" : "Abra" }
    ,"kadabra" : { "id" : "64", "name" : "kadabra", "dname" : "Kadabra" }
    ,"alakazam" : { "id" : "65", "name" : "alakazam", "dname" : "Alakazam" }
    ,"machop" : { "id" : "66", "name" : "machop", "dname" : "Machop" }
    ,"machoke" : { "id" : "67", "name" : "machoke", "dname" : "Machoke" }
    ,"machamp" : { "id" : "68", "name" : "machamp", "dname" : "Machamp" }
    ,"bellsprout" : { "id" : "69", "name" : "bellsprout", "dname" : "Bellsprout" }
    ,"weepinbell" : { "id" : "70", "name" : "weepinbell", "dname" : "Weepinbell" }
    ,"victreebel" : { "id" : "71", "name" : "victreebel", "dname" : "Victreebel" }
    ,"tentacool" : { "id" : "72", "name" : "tentacool", "dname" : "Tentacool" }
    ,"tentacruel" : { "id" : "73", "name" : "tentacruel", "dname" : "Tentacruel" }
    ,"geodude" : { "id" : "74", "name" : "geodude", "dname" : "Geodude" }
    ,"graveler" : { "id" : "75", "name" : "graveler", "dname" : "Graveler" }
    ,"golem" : { "id" : "76", "name" : "golem", "dname" : "Golem" }
    ,"ponyta" : { "id" : "77", "name" : "ponyta", "dname" : "Ponyta" }
    ,"rapidash" : { "id" : "78", "name" : "rapidash", "dname" : "Rapidash" }
    ,"slowpoke" : { "id" : "79", "name" : "slowpoke", "dname" : "Slowpoke" }
    ,"slowbro" : { "id" : "80", "name" : "slowbro", "dname" : "Slowbro" }
    ,"magnemite" : { "id" : "81", "name" : "magnemite", "dname" : "Magnemite" }
    ,"magneton" : { "id" : "82", "name" : "magneton", "dname" : "Magneton" }
    ,"farfetchd" : { "id" : "83", "name" : "farfetchd", "dname" : "Farfetchd" }
    ,"doduo" : { "id" : "84", "name" : "doduo", "dname" : "Doduo" }
    ,"dodrio" : { "id" : "85", "name" : "dodrio", "dname" : "Dodrio" }
    ,"seel" : { "id" : "86", "name" : "seel", "dname" : "Seel" }
    ,"dewgong" : { "id" : "87", "name" : "dewgong", "dname" : "Dewgong" }
    ,"grimer" : { "id" : "88", "name" : "grimer", "dname" : "Grimer" }
    ,"muk" : { "id" : "89", "name" : "muk", "dname" : "Muk" }
    ,"shellder" : { "id" : "90", "name" : "shellder", "dname" : "Shellder" }
    ,"cloyster" : { "id" : "91", "name" : "cloyster", "dname" : "Cloyster" }
    ,"gastly" : { "id" : "92", "name" : "gastly", "dname" : "Gastly" }
    ,"haunter" : { "id" : "93", "name" : "haunter", "dname" : "Haunter" }
    ,"gengar" : { "id" : "94", "name" : "gengar", "dname" : "Gengar" }
    ,"onix" : { "id" : "95", "name" : "onix", "dname" : "Onix" }
    ,"drowzee" : { "id" : "96", "name" : "drowzee", "dname" : "Drowzee" }
    ,"hypno" : { "id" : "97", "name" : "hypno", "dname" : "Hypno" }
    ,"krabby" : { "id" : "98", "name" : "krabby", "dname" : "Krabby" }
    ,"kingler" : { "id" : "99", "name" : "kingler", "dname" : "Kingler" }
    ,"voltorb" : { "id" : "100", "name" : "voltorb", "dname" : "Voltorb" }
    ,"electrode" : { "id" : "101", "name" : "electrode", "dname" : "Electrode" }
    ,"exeggcute" : { "id" : "102", "name" : "exeggcute", "dname" : "Exeggcute" }
    ,"exeggutor" : { "id" : "103", "name" : "exeggutor", "dname" : "Exeggutor" }
    ,"cubone" : { "id" : "104", "name" : "cubone", "dname" : "Cubone" }
    ,"marowak" : { "id" : "105", "name" : "marowak", "dname" : "Marowak" }
    ,"hitmonlee" : { "id" : "106", "name" : "hitmonlee", "dname" : "Hitmonlee" }
    ,"hitmonchan" : { "id" : "107", "name" : "hitmonchan", "dname" : "Hitmonchan" }
    ,"lickitung" : { "id" : "108", "name" : "lickitung", "dname" : "Lickitung" }
    ,"koffing" : { "id" : "109", "name" : "koffing", "dname" : "Koffing" }
    ,"weezing" : { "id" : "110", "name" : "weezing", "dname" : "Weezing" }
    ,"rhyhorn" : { "id" : "111", "name" : "rhyhorn", "dname" : "Rhyhorn" }
    ,"rhydon" : { "id" : "112", "name" : "rhydon", "dname" : "Rhydon" }
    ,"chansey" : { "id" : "113", "name" : "chansey", "dname" : "Chansey" }
    ,"tangela" : { "id" : "114", "name" : "tangela", "dname" : "Tangela" }
    ,"kangaskhan" : { "id" : "115", "name" : "kangaskhan", "dname" : "Kangaskhan" }
    ,"horsea" : { "id" : "116", "name" : "horsea", "dname" : "Horsea" }
    ,"seadra" : { "id" : "117", "name" : "seadra", "dname" : "Seadra" }
    ,"goldeen" : { "id" : "118", "name" : "goldeen", "dname" : "Goldeen" }
    ,"seaking" : { "id" : "119", "name" : "seaking", "dname" : "Seaking" }
    ,"staryu" : { "id" : "120", "name" : "staryu", "dname" : "Staryu" }
    ,"starmie" : { "id" : "121", "name" : "starmie", "dname" : "Starmie" }
    ,"scyther" : { "id" : "123", "name" : "scyther", "dname" : "Scyther" }
    ,"jynx" : { "id" : "124", "name" : "jynx", "dname" : "Jynx" }
    ,"electabuzz" : { "id" : "125", "name" : "electabuzz", "dname" : "Electabuzz" }
    ,"magmar" : { "id" : "126", "name" : "magmar", "dname" : "Magmar" }
    ,"pinsir" : { "id" : "127", "name" : "pinsir", "dname" : "Pinsir" }
    ,"tauros" : { "id" : "128", "name" : "tauros", "dname" : "Tauros" }
    ,"magikarp" : { "id" : "129", "name" : "magikarp", "dname" : "Magikarp" }
    ,"gyarados" : { "id" : "130", "name" : "gyarados", "dname" : "Gyarados" }
    ,"lapras" : { "id" : "131", "name" : "lapras", "dname" : "Lapras" }
    ,"ditto" : { "id" : "132", "name" : "ditto", "dname" : "Ditto" }
    ,"eevee" : { "id" : "133", "name" : "eevee", "dname" : "Eevee" }
    ,"vaporeon" : { "id" : "134", "name" : "vaporeon", "dname" : "Vaporeon" }
    ,"jolteon" : { "id" : "135", "name" : "jolteon", "dname" : "Jolteon" }
    ,"flareon" : { "id" : "136", "name" : "flareon", "dname" : "Flareon" }
    ,"porygon" : { "id" : "137", "name" : "porygon", "dname" : "Porygon" }
    ,"omanyte" : { "id" : "138", "name" : "omanyte", "dname" : "Omanyte" }
    ,"omastar" : { "id" : "139", "name" : "omastar", "dname" : "Omastar" }
    ,"kabuto" : { "id" : "140", "name" : "kabuto", "dname" : "Kabuto" }
    ,"kabutops" : { "id" : "141", "name" : "kabutops", "dname" : "Kabutops" }
    ,"aerodactyl" : { "id" : "142", "name" : "aerodactyl", "dname" : "Aerodactyl" }
    ,"snorlax" : { "id" : "143", "name" : "snorlax", "dname" : "Snorlax" }
    ,"articuno" : { "id" : "144", "name" : "articuno", "dname" : "Articuno" }
    ,"zapdos" : { "id" : "145", "name" : "zapdos", "dname" : "Zapdos" }
    ,"moltres" : { "id" : "146", "name" : "moltres", "dname" : "Moltres" }
    ,"dratini" : { "id" : "147", "name" : "dratini", "dname" : "Dratini" }
    ,"dragonair" : { "id" : "148", "name" : "dragonair", "dname" : "Dragonair" }
    ,"dragonite" : { "id" : "149", "name" : "dragonite", "dname" : "Dragonite" }
    ,"mewtwo" : { "id" : "150", "name" : "mewtwo", "dname" : "Mewtwo" }
    ,"mew" : { "id" : "151", "name" : "mew", "dname" : "Mew" }
    ,"chikorita" : { "id" : "152", "name" : "chikorita", "dname" : "Chikorita" }
    ,"bayleef" : { "id" : "153", "name" : "bayleef", "dname" : "Bayleef" }
    ,"meganium" : { "id" : "154", "name" : "meganium", "dname" : "Meganium" }
    ,"cyndaquil" : { "id" : "155", "name" : "cyndaquil", "dname" : "Cyndaquil" }
    ,"quilava" : { "id" : "156", "name" : "quilava", "dname" : "Quilava" }
    ,"typhlosion" : { "id" : "157", "name" : "typhlosion", "dname" : "Typhlosion" }
    ,"totodile" : { "id" : "158", "name" : "totodile", "dname" : "Totodile" }
    ,"croconaw" : { "id" : "159", "name" : "croconaw", "dname" : "Croconaw" }
    ,"feraligatr" : { "id" : "160", "name" : "feraligatr", "dname" : "Feraligatr" }
    ,"sentret" : { "id" : "161", "name" : "sentret", "dname" : "Sentret" }
    ,"furret" : { "id" : "162", "name" : "furret", "dname" : "Furret" }
    ,"hoothoot" : { "id" : "163", "name" : "hoothoot", "dname" : "Hoothoot" }
    ,"noctowl" : { "id" : "164", "name" : "noctowl", "dname" : "Noctowl" }
    ,"ledyba" : { "id" : "165", "name" : "ledyba", "dname" : "Ledyba" }
    ,"ledian" : { "id" : "166", "name" : "ledian", "dname" : "Ledian" }
    ,"spinarak" : { "id" : "167", "name" : "spinarak", "dname" : "Spinarak" }
    ,"ariados" : { "id" : "168", "name" : "ariados", "dname" : "Ariados" }
    ,"crobat" : { "id" : "169", "name" : "crobat", "dname" : "Crobat" }
    ,"chinchou" : { "id" : "170", "name" : "chinchou", "dname" : "Chinchou" }
    ,"lanturn" : { "id" : "171", "name" : "lanturn", "dname" : "Lanturn" }
    ,"pichu" : { "id" : "172", "name" : "pichu", "dname" : "Pichu" }
    ,"cleffa" : { "id" : "173", "name" : "cleffa", "dname" : "Cleffa" }
    ,"igglybuff" : { "id" : "174", "name" : "igglybuff", "dname" : "Igglybuff" }
    ,"togepi" : { "id" : "175", "name" : "togepi", "dname" : "Togepi" }
    ,"togetic" : { "id" : "176", "name" : "togetic", "dname" : "Togetic" }
    ,"natu" : { "id" : "177", "name" : "natu", "dname" : "Natu" }
    ,"xatu" : { "id" : "178", "name" : "xatu", "dname" : "Xatu" }
    ,"mareep" : { "id" : "179", "name" : "mareep", "dname" : "Mareep" }
    ,"flaaffy" : { "id" : "180", "name" : "flaaffy", "dname" : "Flaaffy" }
    ,"ampharos" : { "id" : "181", "name" : "ampharos", "dname" : "Ampharos" }
    ,"bellossom" : { "id" : "182", "name" : "bellossom", "dname" : "Bellossom" }
    ,"marill" : { "id" : "183", "name" : "marill", "dname" : "Marill" }
    ,"azumarill" : { "id" : "184", "name" : "azumarill", "dname" : "Azumarill" }
    ,"sudowoodo" : { "id" : "185", "name" : "sudowoodo", "dname" : "Sudowoodo" }
    ,"politoed" : { "id" : "186", "name" : "politoed", "dname" : "Politoed" }
    ,"hoppip" : { "id" : "187", "name" : "hoppip", "dname" : "Hoppip" }
    ,"skiploom" : { "id" : "188", "name" : "skiploom", "dname" : "Skiploom" }
    ,"jumpluff" : { "id" : "189", "name" : "jumpluff", "dname" : "Jumpluff" }
    ,"aipom" : { "id" : "190", "name" : "aipom", "dname" : "Aipom" }
    ,"sunkern" : { "id" : "191", "name" : "sunkern", "dname" : "Sunkern" }
    ,"sunflora" : { "id" : "192", "name" : "sunflora", "dname" : "Sunflora" }
    ,"yanma" : { "id" : "193", "name" : "yanma", "dname" : "Yanma" }
    ,"wooper" : { "id" : "194", "name" : "wooper", "dname" : "Wooper" }
    ,"quagsire" : { "id" : "195", "name" : "quagsire", "dname" : "Quagsire" }
    ,"espeon" : { "id" : "196", "name" : "espeon", "dname" : "Espeon" }
    ,"umbreon" : { "id" : "197", "name" : "umbreon", "dname" : "Umbreon" }
    ,"murkrow" : { "id" : "198", "name" : "murkrow", "dname" : "Murkrow" }
    ,"slowking" : { "id" : "199", "name" : "slowking", "dname" : "Slowking" }
    ,"misdreavus" : { "id" : "200", "name" : "misdreavus", "dname" : "Misdreavus" }
    ,"unown" : { "id" : "201", "name" : "unown", "dname" : "Unown" }
    ,"wobbuffet" : { "id" : "202", "name" : "wobbuffet", "dname" : "Wobbuffet" }
    ,"girafarig" : { "id" : "203", "name" : "girafarig", "dname" : "Girafarig" }
    ,"pineco" : { "id" : "204", "name" : "pineco", "dname" : "Pineco" }
    ,"forretress" : { "id" : "205", "name" : "forretress", "dname" : "Forretress" }
    ,"dunsparce" : { "id" : "206", "name" : "dunsparce", "dname" : "Dunsparce" }
    ,"gligar" : { "id" : "207", "name" : "gligar", "dname" : "Gligar" }
    ,"steelix" : { "id" : "208", "name" : "steelix", "dname" : "Steelix" }
    ,"snubbull" : { "id" : "209", "name" : "snubbull", "dname" : "Snubbull" }
    ,"granbull" : { "id" : "210", "name" : "granbull", "dname" : "Granbull" }
    ,"qwilfish" : { "id" : "211", "name" : "qwilfish", "dname" : "Qwilfish" }
    ,"scizor" : { "id" : "212", "name" : "scizor", "dname" : "Scizor" }
    ,"shuckle" : { "id" : "213", "name" : "shuckle", "dname" : "Shuckle" }
    ,"heracross" : { "id" : "214", "name" : "heracross", "dname" : "Heracross" }
    ,"sneasel" : { "id" : "215", "name" : "sneasel", "dname" : "Sneasel" }
    ,"teddiursa" : { "id" : "216", "name" : "teddiursa", "dname" : "Teddiursa" }
    ,"ursaring" : { "id" : "217", "name" : "ursaring", "dname" : "Ursaring" }
    ,"slugma" : { "id" : "218", "name" : "slugma", "dname" : "Slugma" }
    ,"magcargo" : { "id" : "219", "name" : "magcargo", "dname" : "Magcargo" }
    ,"swinub" : { "id" : "220", "name" : "swinub", "dname" : "Swinub" }
    ,"piloswine" : { "id" : "221", "name" : "piloswine", "dname" : "Piloswine" }
    ,"corsola" : { "id" : "222", "name" : "corsola", "dname" : "Corsola" }
    ,"remoraid" : { "id" : "223", "name" : "remoraid", "dname" : "Remoraid" }
    ,"octillery" : { "id" : "224", "name" : "octillery", "dname" : "Octillery" }
    ,"delibird" : { "id" : "225", "name" : "delibird", "dname" : "Delibird" }
    ,"mantine" : { "id" : "226", "name" : "mantine", "dname" : "Mantine" }
    ,"skarmory" : { "id" : "227", "name" : "skarmory", "dname" : "Skarmory" }
    ,"houndour" : { "id" : "228", "name" : "houndour", "dname" : "Houndour" }
    ,"houndoom" : { "id" : "229", "name" : "houndoom", "dname" : "Houndoom" }
    ,"kingdra" : { "id" : "230", "name" : "kingdra", "dname" : "Kingdra" }
    ,"phanpy" : { "id" : "231", "name" : "phanpy", "dname" : "Phanpy" }
    ,"donphan" : { "id" : "232", "name" : "donphan", "dname" : "Donphan" }
    ,"porygon2" : { "id" : "233", "name" : "porygon2", "dname" : "Porygon2" }
    ,"stantler" : { "id" : "234", "name" : "stantler", "dname" : "Stantler" }
    ,"smeargle" : { "id" : "235", "name" : "smeargle", "dname" : "Smeargle" }
    ,"tyrogue" : { "id" : "236", "name" : "tyrogue", "dname" : "Tyrogue" }
    ,"hitmontop" : { "id" : "237", "name" : "hitmontop", "dname" : "Hitmontop" }
    ,"smoochum" : { "id" : "238", "name" : "smoochum", "dname" : "Smoochum" }
    ,"elekid" : { "id" : "239", "name" : "elekid", "dname" : "Elekid" }
    ,"magby" : { "id" : "240", "name" : "magby", "dname" : "Magby" }
    ,"miltank" : { "id" : "241", "name" : "miltank", "dname" : "Miltank" }
    ,"blissey" : { "id" : "242", "name" : "blissey", "dname" : "Blissey" }
    ,"raikou" : { "id" : "243", "name" : "raikou", "dname" : "Raikou" }
    ,"entei" : { "id" : "244", "name" : "entei", "dname" : "Entei" }
    ,"suicune" : { "id" : "245", "name" : "suicune", "dname" : "Suicune" }
    ,"larvitar" : { "id" : "246", "name" : "larvitar", "dname" : "Larvitar" }
    ,"pupitar" : { "id" : "247", "name" : "pupitar", "dname" : "Pupitar" }
    ,"tyranitar" : { "id" : "248", "name" : "tyranitar", "dname" : "Tyranitar" }
    ,"lugia" : { "id" : "249", "name" : "lugia", "dname" : "Lugia" }
    ,"celebi" : { "id" : "251", "name" : "celebi", "dname" : "Celebi" }
    ,"azurill" : { "id" : "298", "name" : "azurill", "dname" : "Azurill" }
    ,"wynaut" : { "id" : "360", "name" : "wynaut", "dname" : "Wynaut" }
    ,"ambipom" : { "id" : "424", "name" : "ambipom", "dname" : "Ambipom" }
    ,"mismagius" : { "id" : "429", "name" : "mismagius", "dname" : "Mismagius" }
    ,"honchkrow" : { "id" : "430", "name" : "honchkrow", "dname" : "Honchkrow" }
    ,"bonsly" : { "id" : "438", "name" : "bonsly", "dname" : "Bonsly" }
    ,"happiny" : { "id" : "440", "name" : "happiny", "dname" : "Happiny" }
    ,"munchlax" : { "id" : "446", "name" : "munchlax", "dname" : "Munchlax" }
    ,"mantyke" : { "id" : "458", "name" : "mantyke", "dname" : "Mantyke" }
    ,"weavile" : { "id" : "461", "name" : "weavile", "dname" : "Weavile" }
    ,"magnezone" : { "id" : "462", "name" : "magnezone", "dname" : "Magnezone" }
    ,"lickilicky" : { "id" : "463", "name" : "lickilicky", "dname" : "Lickilicky" }
    ,"rhyperior" : { "id" : "464", "name" : "rhyperior", "dname" : "Rhyperior" }
    ,"tangrowth" : { "id" : "465", "name" : "tangrowth", "dname" : "Tangrowth" }
    ,"electivire" : { "id" : "466", "name" : "electivire", "dname" : "Electivire" }
    ,"magmortar" : { "id" : "467", "name" : "magmortar", "dname" : "Magmortar" }
    ,"togekiss" : { "id" : "468", "name" : "togekiss", "dname" : "Togekiss" }
    ,"yanmega" : { "id" : "469", "name" : "yanmega", "dname" : "Yanmega" }
    ,"leafeon" : { "id" : "470", "name" : "leafeon", "dname" : "Leafeon" }
    ,"glaceon" : { "id" : "471", "name" : "glaceon", "dname" : "Glaceon" }
    ,"gliscor" : { "id" : "472", "name" : "gliscor", "dname" : "Gliscor" }
    ,"mamoswine" : { "id" : "473", "name" : "mamoswine", "dname" : "Mamoswine" }
    ,"treecko" : { "id" : "252", "name" : "treecko", "dname" : "Treecko" }
    ,"grovyle" : { "id" : "253", "name" : "grovyle", "dname" : "Grovyle" }
    ,"sceptile" : { "id" : "254", "name" : "sceptile", "dname" : "Sceptile" }
    ,"torchic" : { "id" : "255", "name" : "torchic", "dname" : "Torchic" }
    ,"combusken" : { "id" : "256", "name" : "combusken", "dname" : "Combusken" }
    ,"blaziken" : { "id" : "257", "name" : "blaziken", "dname" : "Blaziken" }
    ,"mudkip" : { "id" : "258", "name" : "mudkip", "dname" : "Mudkip" }
    ,"marshtomp" : { "id" : "259", "name" : "marshtomp", "dname" : "Marshtomp" }
    ,"swampert" : { "id" : "260", "name" : "swampert", "dname" : "Swampert" }
    ,"ralts" : { "id" : "280", "name" : "ralts", "dname" : "Ralts" }
    ,"kirlia" : { "id" : "281", "name" : "kirlia", "dname" : "Kirlia" }
    ,"gardevoir" : { "id" : "282", "name" : "gardevoir", "dname" : "Gardevoir" }
    ,"gallade" : { "id" : "475", "name" : "gallade", "dname" : "Gallade" }
    ,"shedinja" : { "id" : "292", "name" : "shedinja", "dname" : "Shedinja" }
    ,"kecleon" : { "id" : "352", "name" : "kecleon", "dname" : "Kecleon" }
    ,"beldum" : { "id" : "374", "name" : "beldum", "dname" : "Beldum" }
    ,"metang" : { "id" : "375", "name" : "metang", "dname" : "Metang" }
    ,"metagross" : { "id" : "376", "name" : "metagross", "dname" : "Metagross" }
    ,"bidoof" : { "id" : "399", "name" : "bidoof", "dname" : "Bidoof" }
    ,"spiritomb" : { "id" : "442", "name" : "spiritomb", "dname" : "Spiritomb" }
    ,"lucario" : { "id" : "448", "name" : "lucario", "dname" : "Lucario" }
    ,"gible" : { "id" : "443", "name" : "gible", "dname" : "Gible" }
    ,"gabite" : { "id" : "444", "name" : "gabite", "dname" : "Gabite" }
    ,"garchomp" : { "id" : "445", "name" : "garchomp", "dname" : "Garchomp" }
    ,"mawile" : { "id" : "303", "name" : "mawile", "dname" : "Mawile" }
    ,"lileep" : { "id" : "345", "name" : "lileep", "dname" : "Lileep" }
    ,"cradily" : { "id" : "346", "name" : "cradily", "dname" : "Cradily" }
    ,"anorith" : { "id" : "347", "name" : "anorith", "dname" : "Anorith" }
    ,"armaldo" : { "id" : "348", "name" : "armaldo", "dname" : "Armaldo" }
    ,"cranidos" : { "id" : "408", "name" : "cranidos", "dname" : "Cranidos" }
    ,"rampardos" : { "id" : "409", "name" : "rampardos", "dname" : "Rampardos" }
    ,"shieldon" : { "id" : "410", "name" : "shieldon", "dname" : "Shieldon" }
    ,"bastiodon" : { "id" : "411", "name" : "bastiodon", "dname" : "Bastiodon" }
    ,"slaking" : { "id" : "289", "name" : "slaking", "dname" : "Slaking" }
    ,"absol" : { "id" : "359", "name" : "absol", "dname" : "Absol" }
    ,"duskull" : { "id" : "355", "name" : "duskull", "dname" : "Duskull" }
    ,"dusclops" : { "id" : "356", "name" : "dusclops", "dname" : "Dusclops" }
    ,"dusknoir" : { "id" : "477", "name" : "dusknoir", "dname" : "Dusknoir" }
    ,"wailord" : { "id" : "321", "name" : "wailord", "dname" : "Wailord" }
    ,"arceus" : { "id" : "493", "name" : "arceus", "dname" : "Arceus" }
    ,"turtwig" : { "id" : "387", "name" : "turtwig", "dname" : "Turtwig" }
    ,"grotle" : { "id" : "388", "name" : "grotle", "dname" : "Grotle" }
    ,"torterra" : { "id" : "389", "name" : "torterra", "dname" : "Torterra" }
    ,"chimchar" : { "id" : "390", "name" : "chimchar", "dname" : "Chimchar" }
    ,"monferno" : { "id" : "391", "name" : "monferno", "dname" : "Monferno" }
    ,"infernape" : { "id" : "392", "name" : "infernape", "dname" : "Infernape" }
    ,"piplup" : { "id" : "393", "name" : "piplup", "dname" : "Piplup" }
    ,"prinplup" : { "id" : "394", "name" : "prinplup", "dname" : "Prinplup" }
    ,"empoleon" : { "id" : "395", "name" : "empoleon", "dname" : "Empoleon" }
    ,"nosepass" : { "id" : "299", "name" : "nosepass", "dname" : "Nosepass" }
    ,"probopass" : { "id" : "476", "name" : "probopass", "dname" : "Probopass" }
    ,"honedge" : { "id" : "679", "name" : "honedge", "dname" : "Honedge" }
    ,"doublade" : { "id" : "680", "name" : "doublade", "dname" : "Doublade" }
    ,"pawniard" : { "id" : "624", "name" : "pawniard", "dname" : "Pawniard" }
    ,"bisharp" : { "id" : "625", "name" : "bisharp", "dname" : "Bisharp" }
    ,"luxray" : { "id" : "405", "name" : "luxray", "dname" : "Luxray" }
    ,"aggron" : { "id" : "306", "name" : "aggron", "dname" : "Aggron" }
    ,"flygon" : { "id" : "330", "name" : "flygon", "dname" : "Flygon" }
    ,"milotic" : { "id" : "350", "name" : "milotic", "dname" : "Milotic" }
    ,"salamence" : { "id" : "373", "name" : "salamence", "dname" : "Salamence" }
    ,"klinklang" : { "id" : "601", "name" : "klinklang", "dname" : "Klinklang" }
    ,"zoroark" : { "id" : "571", "name" : "zoroark", "dname" : "Zoroark" }
    ,"sylveon" : { "id" : "700", "name" : "sylveon", "dname" : "Sylveon" }
    ,"kyogre" : { "id" : "382", "name" : "kyogre", "dname" : "Kyogre" }
    ,"groudon" : { "id" : "383", "name" : "groudon", "dname" : "Groudon" }
    ,"rayquaza" : { "id" : "384", "name" : "rayquaza", "dname" : "Rayquaza" }
    ,"dialga" : { "id" : "483", "name" : "dialga", "dname" : "Dialga" }
    ,"palkia" : { "id" : "484", "name" : "palkia", "dname" : "Palkia" }
    ,"regigigas" : { "id" : "486", "name" : "regigigas", "dname" : "Regigigas" }
    ,"darkrai" : { "id" : "491", "name" : "darkrai", "dname" : "Darkrai" }
    ,"genesect" : { "id" : "649", "name" : "genesect", "dname" : "Genesect" }
    ,"reshiram" : { "id" : "643", "name" : "reshiram", "dname" : "Reshiram" }
    ,"zekrom" : { "id" : "644", "name" : "zekrom", "dname" : "Zekrom" }
    ,"kyurem" : { "id" : "646", "name" : "kyurem", "dname" : "Kyurem" }
    ,"roserade" : { "id" : "407", "name" : "roserade", "dname" : "Roserade" }
    ,"drifblim" : { "id" : "426", "name" : "drifblim", "dname" : "Drifblim" }
    ,"lopunny" : { "id" : "428", "name" : "lopunny", "dname" : "Lopunny" }
    ,"breloom" : { "id" : "286", "name" : "breloom", "dname" : "Breloom" }
    ,"ninjask" : { "id" : "291", "name" : "ninjask", "dname" : "Ninjask" }
    ,"banette" : { "id" : "354", "name" : "banette", "dname" : "Banette" }
    ,"rotom" : { "id" : "479", "name" : "rotom", "dname" : "Rotom" }
    ,"reuniclus" : { "id" : "579", "name" : "reuniclus", "dname" : "Reuniclus" }
    ,"whimsicott" : { "id" : "547", "name" : "whimsicott", "dname" : "Whimsicott" }
    ,"krookodile" : { "id" : "553", "name" : "krookodile", "dname" : "Krookodile" }
    ,"cofagrigus" : { "id" : "563", "name" : "cofagrigus", "dname" : "Cofagrigus" }
    ,"galvantula" : { "id" : "596", "name" : "galvantula", "dname" : "Galvantula" }
    ,"ferrothorn" : { "id" : "598", "name" : "ferrothorn", "dname" : "Ferrothorn" }
    ,"litwick" : { "id" : "607", "name" : "litwick", "dname" : "Litwick" }
    ,"lampent" : { "id" : "608", "name" : "lampent", "dname" : "Lampent" }
    ,"chandelure" : { "id" : "609", "name" : "chandelure", "dname" : "Chandelure" }
    ,"haxorus" : { "id" : "612", "name" : "haxorus", "dname" : "Haxorus" }
    ,"golurk" : { "id" : "623", "name" : "golurk", "dname" : "Golurk" }
    ,"pyukumuku" : { "id" : "771", "name" : "pyukumuku", "dname" : "Pyukumuku" }
    ,"klefki" : { "id" : "707", "name" : "klefki", "dname" : "Klefki" }
    ,"talonflame" : { "id" : "663", "name" : "talonflame", "dname" : "Talonflame" }
    ,"volcarona" : { "id" : "637", "name" : "volcarona", "dname" : "Volcarona" }
    ,"deino" : { "id" : "633", "name" : "deino", "dname" : "Deino" }
    ,"zweilous" : { "id" : "634", "name" : "zweilous", "dname" : "Zweilous" }
    ,"hydreigon" : { "id" : "635", "name" : "hydreigon", "dname" : "Hydreigon" }
    ,"latias" : { "id" : "380", "name" : "latias", "dname" : "Latias" }
    ,"latios" : { "id" : "381", "name" : "latios", "dname" : "Latios" }
    ,"jirachi" : { "id" : "385", "name" : "jirachi", "dname" : "Jirachi" }
    ,"nincada" : { "id" : "290", "name" : "nincada", "dname" : "Nincada" }
    ,"bibarel" : { "id" : "400", "name" : "bibarel", "dname" : "Bibarel" }
    ,"riolu" : { "id" : "447", "name" : "riolu", "dname" : "Riolu" }
    ,"slakoth" : { "id" : "287", "name" : "slakoth", "dname" : "Slakoth" }
    ,"vigoroth" : { "id" : "288", "name" : "vigoroth", "dname" : "Vigoroth" }
    ,"wailmer" : { "id" : "320", "name" : "wailmer", "dname" : "Wailmer" }
    ,"shinx" : { "id" : "403", "name" : "shinx", "dname" : "Shinx" }
    ,"luxio" : { "id" : "404", "name" : "luxio", "dname" : "Luxio" }
    ,"aron" : { "id" : "304", "name" : "aron", "dname" : "Aron" }
    ,"lairon" : { "id" : "305", "name" : "lairon", "dname" : "Lairon" }
    ,"trapinch" : { "id" : "328", "name" : "trapinch", "dname" : "Trapinch" }
    ,"vibrava" : { "id" : "329", "name" : "vibrava", "dname" : "Vibrava" }
    ,"feebas" : { "id" : "349", "name" : "feebas", "dname" : "Feebas" }
    ,"bagon" : { "id" : "371", "name" : "bagon", "dname" : "Bagon" }
    ,"shelgon" : { "id" : "372", "name" : "shelgon", "dname" : "Shelgon" }
    ,"klink" : { "id" : "599", "name" : "klink", "dname" : "Klink" }
    ,"klang" : { "id" : "600", "name" : "klang", "dname" : "Klang" }
    ,"zorua" : { "id" : "570", "name" : "zorua", "dname" : "Zorua" }
    ,"budew" : { "id" : "406", "name" : "budew", "dname" : "Budew" }
    ,"roselia" : { "id" : "315", "name" : "roselia", "dname" : "Roselia" }
    ,"drifloon" : { "id" : "425", "name" : "drifloon", "dname" : "Drifloon" }
    ,"buneary" : { "id" : "427", "name" : "buneary", "dname" : "Buneary" }
    ,"shroomish" : { "id" : "285", "name" : "shroomish", "dname" : "Shroomish" }
    ,"shuppet" : { "id" : "353", "name" : "shuppet", "dname" : "Shuppet" }
    ,"solosis" : { "id" : "577", "name" : "solosis", "dname" : "Solosis" }
    ,"duosion" : { "id" : "578", "name" : "duosion", "dname" : "Duosion" }
    ,"cottonee" : { "id" : "546", "name" : "cottonee", "dname" : "Cottonee" }
    ,"sandile" : { "id" : "551", "name" : "sandile", "dname" : "Sandile" }
    ,"krokorok" : { "id" : "552", "name" : "krokorok", "dname" : "Krokorok" }
    ,"yamask" : { "id" : "562", "name" : "yamask", "dname" : "Yamask" }
    ,"joltik" : { "id" : "595", "name" : "joltik", "dname" : "Joltik" }
    ,"ferroseed" : { "id" : "597", "name" : "ferroseed", "dname" : "Ferroseed" }
    ,"axew" : { "id" : "610", "name" : "axew", "dname" : "Axew" }
    ,"fraxure" : { "id" : "611", "name" : "fraxure", "dname" : "Fraxure" }
    ,"golett" : { "id" : "622", "name" : "golett", "dname" : "Golett" }
    ,"fletchling" : { "id" : "661", "name" : "fletchling", "dname" : "Fletchling" }
    ,"fletchinder" : { "id" : "662", "name" : "fletchinder", "dname" : "Fletchinder" }
    ,"larvesta" : { "id" : "636", "name" : "larvesta", "dname" : "Larvesta" }
    ,"stunfisk" : { "id" : "618", "name" : "stunfisk", "dname" : "Stunfisk" }
    #Special Cases
    ,"nidoran-m" : {"id" : "32", "name" : "nidoran-m", "dname" : "Nidoran (Male)"}
    ,"nidoran-f" : {"id" : "29", "name" : "nidoran-f", "dname" : "Nidoran (Female)"}
    ,"deoxys-normal" : {"id" : "386", "name" : "deoxys-normal", "dname" : "Deoxys Normal" }
    ,"mime-jr" : {"id" : "439", "name" : "mime-jr", "dname" : "Mime Jr." }
    ,"mr-mime" : {"id" : "122", "name" : "mr-mime", "dname" : "Mr. Mime" }
    ,"ho-oh" : {"id" : "250", "name" : "ho-oh", "dname" : "Ho-Oh"}
    ,"porygon-z" : {"id" : "474", "name" : "porygon-z", "dname" : "Porygon-Z" }
}


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
    mon2='Second Pokemon to fuse'
)
async def fuse(interaction: discord.Interaction, mon1: str, mon2: str):
    print(f'we are about to fuse {mon1} and {mon2}')

    '''try:
        mon1_id = get_pokemon_id(mon1)
        mon2_id = get_pokemon_id(mon2)
    except InvalidPokemon as invalid:
        print(f"{interaction.user.name}#{interaction.user.discriminator} passed an invalid pokemon: {invalid}")
        await interaction.response.send_message(f"❗Invalid pokemon entered: {invalid}❗", ephemeral=True)
        return'''

    mon1_id = pd_full_collection[mon1]["id"]
    mon2_id = pd_full_collection[mon2]["id"]
    urls = get_images(mon1_id, mon2_id)

    urls[0]["name"] = f"{pd_full_collection[mon1]['dname']}/{pd_full_collection[mon2]['dname']}"
    if not mon1_id == mon2_id:
        urls[1]["name"] = f"{pd_full_collection[mon2]['dname']}/{pd_full_collection[mon1]['dname']}"
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

@fuse.autocomplete('mon1')
@fuse.autocomplete('mon2')
async def fuse_autocomplete(interaction: discord.Interaction, current: str) -> list[app_commands.Choice[str]]:
    if len(current) > 1:
        return [
            app_commands.Choice(name=pd_full_collection[mon]["dname"], value=mon)
            for mon in pd_full_collection.keys() if current.lower() in mon.lower()
        ]
    else:
        return []

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
