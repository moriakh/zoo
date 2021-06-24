import time
from zoo import Zoo


def add_animal_menu(main_zoo):
    while True:
        print("\nWhat animal do you want to add to the Zoo")
        print("1 : Frog")
        print("2 : Tiger")
        print("3 : Bear")
        print("4 : Peacock")
        print("e : Exit")
        menu2 = input("Please insert a value to add an animal or 'e' for exit: ")
        if menu2 == 'e':
            return
        animal_name = input("Please insert the name of the animal: ")
        if menu2 == '1':
            main_zoo.add_frog(animal_name)
            return
        elif menu2 == '2':
            main_zoo.add_tiger(animal_name)
            return
        elif menu2 == '3':
            main_zoo.add_bear(animal_name)
            return
        elif menu2 == '4':
            main_zoo.add_peacock(animal_name)
            return
        else:
            print("\nPlease insert a right value\n")
            continue

def animals_menu(main_zoo):
    while True:
        print(f"\nWelcome to {main_zoo.name}'s Zoo")
        i = 1
        print('What do you want to do?')
        print("1 : Feed the animals")
        print("2 : Add an animal")
        print("3 : See animal status")
        print("4 : Return to the main menu")
        menu = input("Please insert a value: ")
        if menu == '1':
            while True:
                if len(main_zoo.animals) == 0:
                    first_step = input("There is no animals yet, do you want to add one [y/n]? ")
                    if first_step == 'y':
                        add_animal_menu(main_zoo)
                    elif first_step == 'n':
                        print("Ok! See you soon!")
                        break
                    else:
                        print("\nPlease insert a right value\n")
                        continue
                else:
                    print('What animal do you want to feed?')
                    for animal in main_zoo.animals:
                        print(f"\n{i}: {animal.name}, class: {animal.animal_class}, weight: {animal.food[0]/0.02}")
                        i += 1
                    menu2 = input("Please insert a value to see the animal or 'e' for exit: ")
                    if menu2 == 'e':
                        break
                    elif int(menu2)>0:
                        print("\n")
                        place = int(menu2)-1
                        main_zoo.animals[place].display_info()
                        food = input(f"Do you want to feed {main_zoo.animals[place].name} [y/n]? ")
                        if food == 'y':
                            print(f"The food recommended is {main_zoo.animals[place].food[0]} kg., and the maximum is {main_zoo.animals[place].food[1]} kg.")
                            quantity = input("Please insert the amount of food (kg.): ")
                            main_zoo.animals[place].feeding(quantity)
                    else:
                        print("\nPlease insert a right value\n")
                        continue
        elif menu == '2':
            add_animal_menu(main_zoo)
        elif menu == '3':
            for animal in main_zoo.animals:
                animal.display_info()
        elif menu == '4':
            break
        else:
            print("\nPlease insert a right value\n")
            continue

def zookeepers_menu(main_zoo):
    print("The zoo keepers menu is not implemented yet")
    print("Coming soon you could see the complete list of zoo keepers hired and calculate the ratio according to the current amount of animals")
    print(f"Current amount of animals: {len(main_zoo.animals)}")

def cages_menu(main_zoo):
    print("The cages menu is not implemented yet")
    print("Coming soon you could see the complete list of cages available and space needed according to the current animals")
    total_weight = 0
    m2_needed = 0
    if len(main_zoo.animals)>0:
        for animal in main_zoo.animals:
            total_weight = animal.food[0]/0.02 # en teoría un animal debería comer alrededor del 2% de su peso
        print(f"Total weight: {total_weight} kgs")
        m2_needed = total_weight/60 # acá debería ir un modelo factorial súper complejo que calcule los metros necesarios según los animales almacenados, el peso de estos, el tipo y las jaulas disponibles
        print(f"m2 needed: {m2_needed}")
    else:
        while True:
            first_step = input("There is no animals yet, do you want to add one [y/n]? ")
            if first_step == 'y':
                add_animal_menu(main_zoo)
            elif first_step == 'n':
                print("Ok! See you soon!")
                break
            else:
                print("\nPlease insert a right value\n")
                continue


def takenap(main_zoo):
    if len(main_zoo.animals) == 0:
        pass
    else:
        for i in range(5,0,-1):
            print("ZzzzzzZZz...ZzzZz")
            time.sleep(1)
        for animal in main_zoo.animals:
            animal.feed -= animal.food[0]*0.3
            animal.health -= 5
            animal.happiness -= 5

def main():
    name = input("Welcome! Please insert zoo name: ")
    main_zoo = Zoo(name)
    # Profezoor Rooza
    while True:
        print(f"\nWelcome to {main_zoo.name}'s Zoo")
        print('What do you want to do?')
        print("1 : See the animals options")
        print("2 : See cages availables")
        print("3 : See zoo keepers list")
        print("4 : Take a nap")
        print("5 : Show Zoo's Info")
        print("e : Exit")
        menu = input('Please insert a value: ')
        if menu == '1':
            animals_menu(main_zoo)
        elif menu == '2':
            cages_menu(main_zoo)
        elif menu == '3':
            zookeepers_menu(main_zoo)
        elif menu == '4':
            print("Warning! If you take a nap, your animals could be hungry tomorrow")
            nap = input("Do you want to continue [y/n]? ")
            if nap == 'y':
                takenap(main_zoo)
            elif nap == 'n':
                continue
            else:
                print("Wrong value, you will be back to the main menu")
                continue
        elif menu == '5':
            main_zoo.print_all_info()
        elif menu == 'e':
            break
        else:
            print("\nPlease insert a right value\n")
            continue

main()

# import pdb; pdb.set_trace()