from _collections import deque
from time import sleep
from random import choice
fighters = deque([
    "Scorpion", "Liu Kang", "Sub Zero", "Kano",
    "Sonya Blade", "Raiden", "Baraka", "Jax",
    "Johnny Cage", "Kung Lao", "Jade",
    "Noob Saibot", "Kabal", "Geras", "D'Vorah",
    "Jacqui Briggs", "Scarlett", "Cassie Cage",
    "Kotal Kahn", "Erron Black"
])
killed = []

player = input("Enter your name: ")
player_strength = 80
player_blood = 100
player_power = player_strength
is_connected = False
print("Welcome to Mortal Combat GAME!")

while True:
    if player_blood <= 0:
        print(f"{player} is dead!\nYou loose the game!\nGAME OVER\n")
        break
    computer = fighters.popleft()
    comp_strength = choice(range(20, 80))
    comp_power = choice(range(20, 80))
    comp_blood = 100
    player_blood = 100
    if is_connected:
        while True:
            question = input("Do you want to continue fight Y/N? ").upper()
            if question == "Y":
                print("Game will continue with next battle!!!")
                break
            elif question == "N":
                print(f"{player} wants to quit the game")
                print(f"{player} was killed {', '.join(killed)}")
                print("GAME OVER")
                exit()
            else:
                print("Incorrect answer")
                continue
    is_connected = True
    print()
    print("Loading...", end="")
    for _ in range(3):
        sleep(2)
        print(".", end="")
    print()
    print()
    while True:
        print(f"{player} will hit {computer}")
        print(f"Before hit {computer} have {comp_blood}")
        sleep(3)
        if player_power > comp_strength:
            comp_blood -= (player_power - comp_strength)
        else:
            comp_blood -= player_power//2
        print(f"After hit {computer} have {comp_blood}")
        sleep(2)
        if comp_blood <= 0:
            print(f"{player} kill {computer}")
            killed.append(computer)
            break
        print()
        sleep(2)
        print(f"{computer} will hit {player}")
        print(f"Before hit {player} have {player_blood}")
        sleep(3)
        if comp_power > player_strength:
            player_blood -= (player_power - player_strength)
        else:
            player_blood -= comp_power//2
        print(f"After hit {player} have {player_blood}")
        sleep(2)
        if player_blood <= 0:
            print(f"{computer} kill {player}")
            print(f"{player} was killed {', '.join(killed)}")
            print("GAME OVER")
            exit()
    player_strength += 3
    player_power += 3
    print()
