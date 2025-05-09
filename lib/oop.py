class Animal:

    count = 0
    all_animals = []

    #constructor
    def __init__(self,Name,Color, Age, Legs, Food):
        #atrributes
        self.Name = Name
        self.Color= Color
        self.Age = Age
        self.Legs = Legs 
        self.Food = Food
        Animal.count += 1
        Animal.all_animals.append(self)
    # instance methods
    def grazing(self):
        print(f"The {self.Name} is grazing")
    
    def running(self):
        print(f"The {self.Name} is running")

    @classmethod
    def total_number(cls):
        return (f"I have a total of {cls.count} in my Zoo")
    
    @classmethod
    def allAnimal(cls):
        print("Here is my animals lists")

        for animal in cls.all_animals:
            print(f"{animal.Name}")


Dog = Animal("Dog","Black","34 months", "4 legs", "Canivores")
Rabbit = Animal("Rabbit","White","3 months","4 legs","Herbivors")

print(Dog.Food)
Dog.running()
Rabbit.grazing()
print(Animal.total_number())
Animal.allAnimal()
