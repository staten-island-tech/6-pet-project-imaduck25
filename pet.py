def pet():
    class yournewpet():
        def __init__(self, name, energy, happiness):
            self.name = name
            self.energy = energy
            self.happiness = happiness
        def buy(self, item):
            self.inventory.append(item)
            print(self.inventory)
        pet_name = input("Hi! You have just been gifted a new pet! The species is unkown, but pick a name for it! ")
        print(pet_name)
        print("So you named for pet", pet_name, "!", "What a nice name!")
        activities = input(pet_name,"has 5 energy. What would you like to do with him? Feed, play, take a nap, analyze")
        print(activities)
