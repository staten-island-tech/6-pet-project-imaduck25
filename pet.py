class yournewpet():
    def __init__(self, name, energy=5, happiness=5, money=5):
        self.name = name
        self.energy = energy
        self.happiness = happiness
        self.money = money 
        self.inventory = []
    def buy(self, item):
        self.inventory.append(item)
        print(self.name, "'s inventory", str(self.inventory))

def pet():
        pet_name = input("Hi! You have just been gifted a new pet! The species is unkown, but pick a name for it! ")
        my_pet = yournewpet(pet_name)
        print("So you named for pet", pet_name, "!", "What a nice name!")
        while True:
            print(pet_name, "has", str(my_pet. energy), "energy and", str(my_pet.happiness), "happiness")
            activities = input(f"What would you like to do with {pet_name}? Options: Feed, Play, Take a nap, Analyze: ")
            if activities == "feed":                
                my_pet.happiness += 1
                my_pet.energy += 2
                print("You fed", pet_name,". Energy is now", str(my_pet.energy),".")
            elif activities == "play":
                my_pet.happiness += 1  
                my_pet.energy -= 2
                print("You played with", pet_name, ". Happiness is now", str(my_pet.happiness), "Energy is now", str(my_pet.energy),".")
            elif activities == "take a nap":
                my_pet.energy += 2
                print(pet_name, "took a nap. Energy is now", str(my_pet.energy),".")
            elif activities == "analyze":
                my_pet.happiness -= 4  
                my_pet.energy -= 1
                print(pet_name, "is bored now. Happiness is now", str(my_pet.happiness), ". Energy is now", str(my_pet.energy),"Your thoughts: what's differnet about", pet_name, "?", pet_name, "looks like a normal cat to me.")
            else:
                print("invalid choice")
                continue
pet()