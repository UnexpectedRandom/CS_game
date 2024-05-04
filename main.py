import random
from time import sleep
from os import system

try:
    from colorama import Fore
except ImportError:
    print("Colorama is not recognized. Please install it using 'pip install colorama'.")

# Player stats
player_stats = {
    "name": "",
    "age": 0,
    "city": "",
    "country": "",
    "health": 100,
    "money": 50,
    "inventory": []
}

# Weapons
weapons = {
    "Dagger": {"price": 25, "damage": 7},
    "Apprentice Sword": {"price": 100, "damage": 15},
    "Master Sword": {"price": 150, "damage": 25},
    "Demi Sword": {"price": 999, "damage": 100}
}

# Foods
foods = {
    "Apple": {"price": 10, "health_gain": 20},
    "Bread": {"price": 15, "health_gain": 30},
    "Potion": {"price": 30, "health_gain": 50}
}

# Mobs
mobs = {
    "Wendigo": {"health": 500, "damage": 17, "speed": 1.3},
    "Infected": {"health": 75, "damage": 5, "speed": 1}
}

def welcome_message(player_stats, name, age, city, country):
    print(Fore.CYAN+f'[+] You were born in {country}')
    sleep(5)
    try:
         system('cls')
    except:
        system('clear')
    print(f'[+] at the city of {city}')
    sleep(5)
    try:
         system('cls')
    except:
        system('clear')
    print(f'[+] you are {name}')
    sleep(5)
    try:
         system('cls')
    except:
        system('clear')
    print(f'[+] you are the hero of the city')
    sleep(5)
    try:
         system('cls')
    except:
        system('clear')
    print('[+] There are mobs trying to destroy your city')
    sleep(5)
    try:
         system('cls')
    except:
        system('clear')
    print('[+] Fight to protect the city and get better swords to kill foes'+Fore.RESET)
    sleep(5)
    try:
         system('cls')
    except:
        system('clear')
    print(Fore.GREEN + f"[+] Player {player_stats['name']} has joined")
    sleep(0.5)
    print(Fore.BLUE + f"[-] You have spawned in with Health: {player_stats['health']}, Money: {player_stats['money']}")
    sleep(0.6)
    print("[-] Weapon: Fist"+Fore.RESET)

def help_menu():
    print("Help Menu:")
    print("1. /stat - Display player statistics")
    print("2. /help - Display this help menu")
    print("3. 1 - Go to the weapons store")
    print("4. 2 - Go to the food store")
    print("5. 3 - Attack mobs")
    print("6. -q - Quit the game")


def help_functions():
    choices = [
        Fore.GREEN + "\n[+] SYSTEM: To get your stats type '/stat'",
        Fore.GREEN + "\n[+] SYSTEM: Hostile mobs can attack you anywhere",
        Fore.GREEN + "\n[+] SYSTEM: If you want to end the game, type '-q'"
    ]
    return random.choice(choices)

def display_weapons():
    print("Weapons:")
    for weapon, stats in weapons.items():
        print(f"{weapon}: Damage: {stats['damage']}, Price: {stats['price']}")

def display_food():
    print("Food Items:")
    for food, stats in foods.items():
        print(f"{food}: Health Gain: {stats['health_gain']}, Price: {stats['price']}")

def buy_weapon(player_stats):
    display_weapons()
    choice = input("Enter the name of the weapon you want to buy: ")
    if choice in weapons:
        weapon = weapons[choice]
        if player_stats["money"] >= weapon["price"]:
            player_stats["inventory"].append(choice)
            player_stats["money"] -= weapon["price"]
            print(f"You bought {choice}!")
        else:
            print("You don't have enough money.")
    else:
        print("Invalid weapon choice.")

def buy_food(player_stats):
    display_food()
    choice = input("Enter the name of the food item you want to buy: ")
    if choice in foods:
        food = foods[choice]
        if player_stats["money"] >= food["price"]:
            player_stats["money"] -= food["price"]
            player_stats["health"] = min(100, player_stats["health"] + food["health_gain"])  # Cap health at 100
            print(f"You bought {choice} and gained {food['health_gain']} health!")
        else:
            print("You don't have enough money.")
    else:
        print("Invalid food choice.")
        
def attack_mob(player_stats):
    mob_name = random.choice(list(mobs.keys()))
    print(f"You encountered a {mob_name}!")
    while True:
        command = input("Do you want to attack? (yes/no): ")
        if command.lower() == "yes":
            weapon_choice = input("Choose a weapon from your inventory: ")
            if weapon_choice in player_stats["inventory"]:
                weapon_damage = weapons[weapon_choice]["damage"]
                mob_health = mobs[mob_name]["health"]
                mob_damage = mobs[mob_name]["damage"]
                player_stats["health"] -= mob_damage
                mob_health -= weapon_damage
                mobs[mob_name]["health"] = mob_health
                print(f"\nYou attacked the {mob_name} with {weapon_choice}, dealing {weapon_damage} damage!")
                print(f"The {mob_name} attacked you, dealing {mob_damage} damage!")
                print(f"Your health: {player_stats['health']}, {mob_name}'s health: {mob_health}\n")
                if player_stats["health"] <= 0:
                    print("You died. Game over.")
                    exit(1)
                if mob_health <= 0:
                    money_gain = random.randint( 50,200)  # Random money gain between 20 and 50
                    player_stats["money"] += money_gain
                    print(f"You defeated the {mob_name} and gained {money_gain} money!")
                    break
            else:
                print("You don't have that weapon.")
        elif command.lower() == "no":
            print("You chose not to attack.")
            break
        else:
            print("Invalid command. Please enter 'yes' or 'no'.")


def menu(player_stats):
    while True:
        command = input("> ")
        if command == "-q":
            exit(1)
        elif command == "/stat":
            print(player_stats)
        elif command == "/help":
            help_menu()
        elif command == "1":
            buy_weapon(player_stats)
        elif command == "2":
            buy_food(player_stats)
        elif command == "3":
            attack_mob(player_stats)


def main():
    name = input("What is your name: ")
    age = input("\nWhat is your age: ")
    city = input("\nWhat city are you in: ")
    country = input("\nLand that the city is located in: ")

    player_stats["name"] = name
    player_stats["age"] = age
    player_stats["city"] = city
    player_stats["country"] = country

    try:
        system('cls')
    except:
        system('clear')

    welcome_message(player_stats, name, age, city, country)
    menu(player_stats)

if __name__ == '__main__':
    main()
