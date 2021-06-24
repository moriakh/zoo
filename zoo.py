from animal import Frog, Tiger, Bear, Peacock


class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
        self.animal_class = ''
        self.regular_food = ''
        self.max_qty_food = ''
        self.gender = ''
        self.random_attribute = ''

    def add_animal(self):
        self.animal_class = ''
        self.regular_food = ''
        self.max_qty_food = ''
        self.gender = ''

        while self.animal_class == '':
            print('According to the following list:')
            print('1 : Amphibia')
            print('2 : Reptiles')
            print('3 : Birds')
            print('4 : Mammals')
            animal_class = input('Please insert the animal class: ')
            if animal_class == '1':
                self.animal_class = 'Amphibia'
            elif animal_class == '2':
                self.animal_class = 'Reptiles'
            elif animal_class == '3':
                self.animal_class = 'Birds'
            elif animal_class == '4':
                self.animal_class = 'Mammals'
            else:
                self.animal_class = ''

        while self.regular_food == '':
            self.regular_food = input('How many kilograms eat daily? ')
        
        while self.max_qty_food == '':
            self.max_qty_food = input('Max kilograms/day? ')
        # hacer validador para que max sea mayor que regular

        while self.gender == '':
            self.gender = input("Enter 'F' for Female or 'M' for Male: ")
        return self

    def add_frog(self, name):
        self.add_animal()
        self.random_attribute = input(f"Insert {name}'s jumps: ")
        self.random_attribute = float(self.random_attribute)
        self.animals.append(Frog(name, 'Amphibia', self.regular_food, self.max_qty_food, self.gender, self.random_attribute))

    def add_tiger(self, name):
        self.add_animal()
        self.random_attribute = input(f"Insert {name}'s bites: ")
        self.random_attribute = float(self.random_attribute)
        self.animals.append(Tiger(name, 'Mammals', self.regular_food, self.max_qty_food, self.gender, self.random_attribute))

    def add_bear(self, name):
        self.add_animal()
        self.random_attribute = input(f"Insert {name}'s roars: ")
        self.random_attribute = float(self.random_attribute)
        self.animals.append(Bear(name, 'Mammals', self.regular_food, self.max_qty_food, self.gender, self.random_attribute))


    def add_peacock(self, name):
        self.add_animal()
        self.random_attribute = input(f"Insert {name}'s flies: ")
        self.random_attribute = float(self.random_attribute)
        self.animals.append(Peacock(name, 'Birds', self.regular_food, self.max_qty_food, self.gender, self.random_attribute))
    
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            if animal.state == "'I'm died'":
                # tb puede ser un animal.health == 0
                pass # limpiar lista
            else:
                animal.display_info()  
                print("\n") 
        return self

