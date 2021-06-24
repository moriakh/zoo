class Animal:
    def __init__(self, name, animal_class, regular_food, max_qty_food, gender):
        self.name = name
        self.health = 50
        self.happiness = 50
        self.feed = 0
        self.animal_class = animal_class
        self.food = [float(regular_food), float(max_qty_food)]
        self.gender = gender
        self.state = 'Hungry'
    
    def display_info(self):
        self.status()
        print("*"*30," "*3, self.name, " "*3, "*"*30)
        print(f'{self.health}/100 level of health and {self.happiness}/100 level of happiness')
        print(f"'It's status is {self.state}'")
        return self

    def feeding(self, quantity):
        raise NotImplementedError

    def status(self):
        if self.happiness>70 and self.feed>(0.5*self.food[0]) and self.health>70:
            self.state = 'Happy'
        elif self.happiness<30 and self.feed>(0.6*self.food[0]) and self.health<70:
            self.state = 'I want to poop!'
        elif self.happiness<30 and self.feed<(0.2*self.food[0]) and self.health<50:
            self.state = 'Are you forgetting something?'
        elif self.happiness<30 and self.feed<(0.1*self.food[0]) and self.health<30:
            self.state = "'I'm so sad'"
        elif self.health==0:
            self.state = "'I'm died'"
        else:
            self.state = 'Hungry'
        return self

class Peacock(Animal):
    def __init__(self, name, animal_class, regular_food, max_qty_food, gender, flies):
        super().__init__(name, animal_class, regular_food, max_qty_food, gender)
        self.flies = flies
    
    def feeding(self, quantity):
        quantity = float(quantity)
        if quantity<=0:
            print('Are you joking?')
        elif self.food[0]>quantity or quantity>self.food[1]:
            print('You are not giving it the right portion of food')
        elif self.food[1]>quantity:
            print(f'{self.name} is doing a yummy face and doing {self.flies} flies')
            self.health += 10
            self.happiness += 10
            self.feed += quantity
            self.display_info()
        return self

class Tiger(Animal):
    def __init__(self, name, animal_class, regular_food, max_qty_food, gender, bites):
        super().__init__(name, animal_class, regular_food, max_qty_food, gender)
        self.bites = bites
    
    def feeding(self, quantity):
        quantity = float(quantity)
        if quantity<=0:
            print('Are you joking?')
            print(f'{self.name} wanna give you {self.bites} bites')
        elif self.food[0]>quantity or quantity>self.food[1]:
            print('You are not giving it the right portion of food')
        elif self.food[1]>quantity:
            print(f'{self.name} is doing a yummy face')
            self.health += 10
            self.happiness += 10
            self.feed += quantity
            self.display_info()
        return self

class Bear(Animal):
    def __init__(self, name, animal_class, regular_food, max_qty_food, gender, roars):
        super().__init__(name, animal_class, regular_food, max_qty_food, gender)
        self.roars = roars
    
    def feeding(self, quantity):
        quantity = float(quantity)
        if quantity<=0:
            print('Are you joking?')
        elif self.food[0]>quantity or quantity>self.food[1]:
            print('You are not giving it the right portion of food')
        elif self.food[1]>quantity:
            print(f'{self.name} is doing a yummy face and is roaring of happiness')
            self.health += 10
            self.happiness += 10
            self.feed += quantity
            self.display_info()
        return self

class Frog(Animal):
    def __init__(self, name, animal_class, regular_food, max_qty_food, gender, jumps):
        super().__init__(name, animal_class, regular_food, max_qty_food, gender)
        self.jumps = jumps

    def feeding(self, quantity):
        quantity = float(quantity)
        if quantity<=0:
            print('Are you joking?')
        elif self.food[0]>quantity or quantity>self.food[1]:
            print('You are not giving it the right portion of food')
        elif self.food[1]>quantity:
            print(f'{self.name} is doing a yummy face and jumping {self.jumps} times')
            self.health += 10
            self.happiness += 10
            self.feed += quantity
            self.display_info()
        return self

    def __repr__(self):
        return self.name