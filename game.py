from rich.console import Console
from rich import print
from rich.prompt import Prompt
from rich.text import Text

from Rooms import RoomObject
from Players import PlayerCharacter,LoadAllCharacters

from config import p,e


print("[green bold]Welcome to the game!")
p("Game Started.")

player_list = LoadAllCharacters()

print (f"Character List: \n{player_list}")
p("Characters Loaded.")

entryway = RoomObject("Entryway","You see big doors")
print(entryway)