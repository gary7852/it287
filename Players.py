import json

from rich.console import Console
from rich import print
from rich.prompt import Prompt
from rich.text import Text

from Dice import roll_dice,roll3d6,rolld6,roll3d6stat

class PlayerCharacter:
    def __init__(self, name):
        # Store passed in values in the object
        self.name = name
        self.current_hp = 0
        
        self.strength = 8
        self.constitution = 8
        self.agility = 8
        self.armor = 2
        self.roll_stats()

    def __str__(self):
        return(f"{self.name}, HP: {self.current_hp}/{self.get_max_hp()},STRENGTH: {self.strength},CONSTITUION: {self.constitution},AGILITY: {self.agility},ARMOR: {self.armor}")


    def roll_stats(self):
        self.strength = roll3d6stat()
        self.constitution = roll3d6stat()
        self.agility = roll3d6stat()
        self.current_hp = self.get_max_hp()

    def get_max_hp(self):
        return self.constitution * 2

    def get_damage_max(self):
        return int(self.strength / 2)

    def take_damage(self, enemy):
        rolls,damage = roll_dice(enemy.get_damage_max(),count=1)
        
        self.current_hp = self.current_hp - damage + self.armor
        print(f"{self.name} took {damage} damage - armor absorbed {self.armor} hit points")

    def heal(self):
            rolls, heal = roll_dice(5)
            self.current_hp = self.current_hp + heal
            print(f"{self.name} healed for {heal} hit points.")

    def is_knocked_out(self):
            if self.current_hp < 1:
                return True
            return False

    def load_from_json(self, name, file_path="Dungeon_Crawler_Organized/players.json"):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    npc_list = json.load(f)

                for npc in npc_list:
                    if npc["name"].lower() == name.lower():
                        self.name = npc["name"]
                        self.str = int(npc["strength"])
                        self.ag = int(npc["agility"])
                        self.con = int(npc["constitution"])
                        self.armor = int(npc["armor"])
                        self.current_hp = int(npc["current_hp"])
                        return True


                print(f"[!] NPC '{name}' not found in {file_path}.")
                return False


            except Exception as e:
                print(f"[!] Failed to load JSON: {e}")
                return False

    def save_to_json(self, file_path="Dungeon_Crawler_Organized/players.json"):
            our_data = {
                "name": self.name,
                "race": "Unknown",  # Could be extended to a property
                "strength": str(self.strength),
                "agility": str(self.agility),
                "constitution": str(self.constitution),
                "armor": str(self.armor),
                "current_hp": str(self.current_hp)
            }
    
            try:
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        npc_list = json.load(f)
                except FileNotFoundError:
                    npc_list = []
                updated = False
                for i, npc in enumerate(npc_list):
                    if npc["name"].lower() == self.name.lower():
                        npc_list[i] = our_data
                        updated = True
                        break
    
                if not updated:
                    npc_list.append(our_data)
    
                # Save back
                with open(file_path, "w", encoding="utf-8") as f:
                    json.dump(npc_list, f, indent=2)
    
                print(f"[✓] {self.name} saved to {file_path}\n")
    
            except Exception as e:
                print(f"[!] Failed to save JSON: {e}")

def LoadAllCharacters(file_path="Dungeon_Crawler_Organized/players.json"):
        players = list()
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                npc_list = json.load(f)

                for npc in npc_list:
                    name = npc["name"]
                    pc = PlayerCharacter(name)
                    
                    #pc.str = int(npc["strength"])
                    #pc.ag = int(npc["agility"])
                    #pc.con = int(npc["constitution"])
                    #pc.armor = int(npc["armor"])
                    #pc.current_hp = int(npc["current_hp"])
                    pc.load_from_json(name)
                    players.append(pc)

                return players


                


        except Exception as e:
            print(f"[!] Failed to load JSON: {e}")
            return False
         



if __name__ == "__main__":
    print("Testing...")
    characters = {"Mickey_Mouse","Mario","Pikachu","Batman","Homer_Simpson","Frank"}

    for character in characters:
    
  
        characterobj = PlayerCharacter(character)
        print(f"{character} Rolls: {characterobj}")
        characterobj.load_from_json(character)
        print(f"{character} Load: {characterobj}")
        characterobj.save_to_json()