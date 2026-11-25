import random

from config import p,e

def roll_dice(sides=6,count=1):
    rolls = list()
    total = 0
    p(f"Rolling {count} dice with {sides} sides.")
    for i in range(count):
        roll = random.randint(1,sides)
        total += roll
        rolls.append(roll)
        p(f"Rolled {roll} - Total: {total}")

    p(f"Total of rolls: {total}") 
    return rolls,total

def roll3d6stat():
    roll, total = roll3d6()
    if total < 8:
        total = 8
    return total 

def roll3d6():
    return roll_dice(sides=6,count=3)
    p(f"Rolling {count} dice with {sides} sides.")

def roll2d10():
    return roll_dice(sides=10,count=2)
    p(f"Rolling {count} dice with {sides} sides.")

def rolld6(count=1):
    return roll_dice(sides=6,count=count)
    p(f"Rolling {count} dice with {sides} sides.")

def rolld4(count=1):
    return roll_dice(sides=4,count=count)
    p(f"Rolling {count} dice with {sides} sides.")

if __name__ == "__main__":
    print("Testing...")
    rolls,total=roll_dice(sides=6,count=4)
    print(f"Total: {total}\n Rolls: {rolls}")

    rolls,total=roll3d6()
    print(f"3D6 Total: {total}\n Rolls: {rolls}")