from rich.console import Console
from rich import print
from rich.prompt import Prompt
from rich.text import Text

from Rooms import RoomObject
from Players import PlayerCharacter,LoadAllCharacters

print("[green bold]Welcome to the game!")

player_list = LoadAllCharacters()

print (f"Character List: \n{player_list}")
entryway = RoomObject("Entryway","You see big doors")
print(entryway)