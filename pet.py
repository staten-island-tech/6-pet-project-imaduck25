class urpet:
    def __init__(self, name, energy=5, happiness=5, coins=6):
        self.name = name
        self.energy = energy
        self.happiness = happiness
        self.coins = coins
        self.inventory = []
    def buy(self, item, cost):
        if self.coins >= cost:
            self.coins -= cost
            self.inventory.append(item)
            print(self.name, "bought", item, ". Coins left:", str(self.coins))
        else:
            print(self.name, "doesn’t have enough coins to buy", item, "!")
def pet():
    pet_name = input("Hi! you have just been gifted a new pet! the species is unknown, but pick a name for it! ")
    my_pet = urpet(pet_name)
    print("So you named your pet", pet_name, "! What a nice name!")
    while True:
        if my_pet.happiness <= 0:
            print(pet_name, "was too dissatisfied. It eats you.")
            break
        if my_pet.energy >= 10:
            print(pet_name, "was too chaotically excited. It eats you.")
            break
        print(pet_name, " has", str(my_pet.energy), "energy,", str(my_pet.happiness), "happiness, and", str(my_pet.coins), "coins.")
        activities = input("What would you like to do with " + pet_name + "? Options: Feed, Play, Take a nap, Analyze, Shop, Quit: ").lower().strip()
        if activities == "feed":
            if "food" in my_pet.inventory:
                my_pet.inventory.remove("food")
                my_pet.happiness += 1
                my_pet.energy += 2
                print("You fed", pet_name, ". Happiness is now", str(my_pet.happiness), "and energy is now", str(my_pet.energy), ".")
            else:
                print("No food in inventory!", pet_name, " is starving...")
                my_pet.happiness -= 1
                print("You didn't feed", pet_name, ". Happiness is now", str(my_pet.happiness), "and energy is now", str(my_pet.energy), ".")
                print("Also, you must buy food before feeding", pet_name, "by going to shop.")
                if my_pet.energy < 1:
                    my_pet.happiness -= 3
                    print(pet_name, " lost 3 happiness due to starvation!")
        elif activities == "play":
            my_pet.happiness += 2
            my_pet.energy -= 2
            print("You played with", pet_name, ". Happiness is now", str(my_pet.happiness), "and energy is now", str(my_pet.energy), ".")
        elif activities == "take a nap":
            my_pet.energy += 2
            my_pet.happiness += 1
            print(pet_name, "took a nap. Energy is now", str(my_pet.energy), ".")
        elif activities == "analyze":
            my_pet.happiness -= 3
            my_pet.energy -= 1
            print("Your thoughts: what's diffrent about", pet_name, "?", pet_name," looks like a normal cat to me... or does it?")
            print(pet_name, " is bored now. Happiness is now ", str(my_pet.happiness), ", energy is now ", str(my_pet.energy), ".")
        elif activities == "shop":
            choice = input("Welcome to Shop Wrong! Food costs 2 coins. Buy food? (yes/no): ").lower().strip()
            if choice == "yes":
                my_pet.buy("food", 2)
            elif choice == "no":
                print("ok.....if you say so.......")
            else:
                print("Invalid choice.")
                continue
        elif activities == "quit":
            print("Thanks for playing! Goodbye...... :(")
            print("......")
            print("....................")
            break
        else:
            print("Invalid choice.")
            continue
pet()