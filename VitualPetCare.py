# # import time
# #
# # # Initialize pet stats
# # pet_name = input("Name your pet: ")
# # hunger = 5      # 0 = full, 10 = starving
# # happiness = 5   # 0 = sad, 10 = very happy
# #
# # def show_status():
# #     print(f"\n{pet_name}'s Status:")
# #     print(f"Hunger: {hunger}/10")
# #     print(f"Happiness: {happiness}/10")
# #
# # def feed_pet():
# #     global hunger
# #         hunger -= 2
# #         print(f"You fed {pet_name}. Yum!")
# #     else:
# #     if hunger > 0:
# #         print(f"{pet_name} is already full!")
# #
# # def play_with_pet():
# #     global happiness, hunger
# #     happiness += 2
# #     hunger += 1
# #     print(f"You played with {pet_name}. So much fun!")
# #
# # def time_passes():
# #     global hunger, happiness
# #     hunger += 1
# #     happiness -= 1
# #
# # # Main game loop
# # while True:
# #     show_status()
# #     print("\nWhat would you like to do?")
# #     print("1. Feed")
# #     print("2. Play")
# #     print("3. Do nothing")
# #     print("4. Quit")
# #
# #     choice = input("Enter your choice: ")
# #
# #     if choice == "1":
# #         feed_pet()
# #     elif choice == "2":
# #         play_with_pet()
# #     elif choice == "3":
# #         print(f"You let time pass...")
# #     elif choice == "4":
# #         print(f"Goodbye! {pet_name} will miss you.")
# #         break
# #     else:
# #         print("Invalid choice. Try again.")
# #
# #     time_passes()
# #     time.sleep(1)
# #
# #     # Check for extreme conditions
# #     if hunger >= 10:
# #         print(f"\nOh no! {pet_name} is starving. Game over.")
# #         break
# #     if happiness <= 0:
# #         print(f"\n{pet_name} is too sad to continue. Game over.")
# #         break
#
#
#
# import time
# import random
#
# def adopt_pet():
#     name = input("\n🐾 What would you like to name your new pet? ")
#     time.sleep(1)
#     print(f"🎉 You adopted {name}!")
#     return name, 5, 5  # hunger, happiness
#
# def show_status(name, hunger, happiness):
#     time.sleep(1)
#     print(f"\n{name}'s Status:")
#     time.sleep(1)
#     print(f"Hunger: {hunger}/10")
#     time.sleep(1)
#     print(f"Happiness: {happiness}/10")
#
# def feed_pet(hunger):
#     time.sleep(1)
#     print("\n🍽️ What would you like to feed your pet?")
#     time.sleep(1)
#     print("1. Donut (-2 hunger)")
#     time.sleep(1)
#     print("2. Cake (-3 hunger, happiness - 1)")
#     choice = input("Choose food: ")
#     if choice == "1":
#         hunger = max(0, hunger - 2)
#         print("🍩 Yum! Donut time.")
#     elif choice == "2":
#         hunger = max(0, hunger - 3 , happiness - 1)
#         print("🍰 Delicious cake!")
#     else:
#         print("❌ Invalid choice.")
#     return hunger
#
# def play_with_pet(happiness, hunger):
#     time.sleep(1)
#     print("\n🎮 Where would you like to play?")
#     time.sleep(1)
#     print("1. Outside (+3 happiness, +3 hunger)")
#     time.sleep(1)
#     print("2. Inside (+2 happiness, +1 hunger)")
#     choice = input("Choose location: ")
#     if choice == "1":
#         happiness = min(10, happiness + 3)
#         hunger = min(10, hunger + 2)
#         print("🌳 You played outside !")
#     elif choice == "2":
#         happiness = min(10, happiness + 2)
#         hunger = min(10, hunger + 1)
#         print("🏠 You played inside!")
#     else:
#         print("❌ Invalid choice.")
#     return happiness, hunger
#
# def sleep_pet(hunger):
#     sleep_time = random.randint(1, 100)
#     hunger = min(10, hunger + sleep_time // 20)
#     time.sleep(1)
#     print(f"\n😴 Your pet slept for {sleep_time} minutes.")
#     return hunger
#
# # Game loop
# while True:
#     pet_name, hunger, happiness = adopt_pet()
#
#     while True:
#         show_status(pet_name, hunger, happiness)
#
#         # Win condition
#         if hunger < 1 and happiness > 9:
#             print(f"\n🏆 {pet_name} is perfectly happy and healthy! You win!")
#             break
#
#         print("\nWhat would you like to do?")
#         time.sleep(1)
#         print("1. Feed")
#         print("2. Play")
#         print("3. Sleep")
#         print("4. Adopt a new pet")
#         print("5. Quit")
#
#         action = input("Enter your choice: ")
#
#         if action == "1":
#             hunger = feed_pet(hunger)
#         elif action == "2":
#             happiness, hunger = play_with_pet(happiness, hunger)
#         elif action == "3":
#             hunger = sleep_pet(hunger)
#         elif action == "4":
#             print("🐾 Time to adopt a new pet!")
#             break
#         elif action == "5":
#             print(f"👋 Goodbye! {pet_name} will miss you.")
#             exit()
#         else:
#             print("❌ Invalid choice.")
#
#         time.sleep(1)
#
#         # Game over conditions
#         if hunger >= 10:
#             print(f"\n⚠️ {pet_name} is starving. Game over.")
#             break
#         if happiness <= 0:
#             print(f"\n😢 {pet_name} is too sad to continue. Game over.")
#             break



import time
import random

def adopt_pet():
    print("\n🐾 Choose your pet type:")
    print("1. Dog")
    print("2. Cat")
    print("3. Rabbit")
    print("Dog(Loves playing outside (gets happier:)))")
    print("Cat(Dislikes vet visits (gets sad:())")
    print("Rabbit(Sensitive sleeper (gets hungry:())")
    pet_type = input("Enter choice: ")
    types = {"1": "Dog", "2": "Cat", "3": "Rabbit"}
    pet_kind = types.get(pet_type, "Mystery Pet")
    name = input(f"Name your {pet_kind}: ")

    # Set different starting stats and traits
    if pet_kind == "Dog":
        hunger, happiness = 4, 6
        trait = "Loves playing outside (+3 happiness)"
    elif pet_kind == "Cat":
        hunger, happiness = 5, 5
        trait = "Dislikes vet visits (-5 happiness)"
    elif pet_kind == "Rabbit":
        hunger, happiness = 3, 7
        trait = "Sensitive sleeper (+4 hunger)"
    else:
        hunger, happiness = 5, 5
        trait = "Unknown trait"

    print(f"🎉 You adopted a {pet_kind} named {name}!")
    return name, pet_kind, hunger, happiness, trait

def show_status(name, pet_kind, hunger, happiness):
    time.sleep(1)
    print(f"\n{name} the {pet_kind}'s Status:")
    time.sleep(1)
    print(f"Hunger: {hunger}/10")
    time.sleep(1)
    print(f"Happiness: {happiness}/10")

def feed_pet(hunger):
    time.sleep(1)
    print("\n🍽️ What would you like to feed your pet?")
    time.sleep(1)
    print("1. Donut (-2 hunger)")
    time.sleep(1)
    print("2. Cake (-3 hunger, happiness - 1)")
    choice = input("Choose food: ")
    if choice == "1":
        hunger = max(0, hunger - 2)
        print("🍩 Yum! Donut time.")
    elif choice == "2":
        hunger = max(0, hunger - 3, happiness - 1)
        print("🍰 Delicious cake!")
    else:
        print("❌ Invalid choice.")
    return hunger

def play_with_pet(happiness, hunger):
    time.sleep(1)
    print("\n🎮 Where would you like to play?")
    time.sleep(1)
    print("1. Outside (+3 happiness, +2 hunger)")
    time.sleep(1)
    print("2. Inside (+2 happiness, +1 hunger)")
    choice = input("Choose location: ")

    # Random bug bite event (33% chance)
    if choice == "1" and random.random() < 0.33:
        happiness = max(0, happiness - 2)
        print("🐛 Oh no! Your pet got bitten by a bug!")
        return happiness, hunger, "bug"
    # Grandma stepping on pet (10% chance, only inside)
    if choice == "2" and random.random() < 0.1:
        happiness = max(0, happiness - 3)
        print("👵 Grandma accidentally stepped on your pet!")
        return happiness, hunger, "grandma"

    if choice == "1":
        happiness = min(10, happiness + 3)
        hunger = min(10, hunger + 2)
        print("🌳 You played outside!")
    elif choice == "2":
        happiness = min(10, happiness + 2)
        hunger = min(10, hunger + 1)
        print("🏠 You played inside!")
    else:
        print("❌ Invalid choice.")
    return happiness, hunger,"BAD"

def sleep_pet(hunger):
    sleep_time = random.randint(1, 100)
    hunger = min(10, hunger + sleep_time // 20)
    print(f"\n😴 Your pet slept for {sleep_time} minutes.")
    return hunger

def vet_visit(happiness, hunger):
    print("\n🚑 You took your pet to the vet.")
    happiness = min(10, happiness + 3)
    hunger = min(10, hunger + 1)
    print("🩺 Your pet feels much better now!")
    return happiness, hunger

# Game loop
while True:
    pet_name, pet_kind, hunger, happiness,trait = adopt_pet()

    while True:
        show_status(pet_name, pet_kind, hunger, happiness)

        # Win condition
        if hunger < 1 and happiness > 9:
            print(f"\n🏆 {pet_name} the {pet_kind} is perfectly happy and healthy! You win!")
            break

        print("\nWhat would you like to do?")
        time.sleep(1)
        print("1. Feed")
        time.sleep(1)
        print("2. Play")
        time.sleep(1)
        print("3. Sleep")
        time.sleep(1)
        print("4. Adopt a new pet")
        time.sleep(1)
        print("5. Quit")

        action = input("Enter your choice: ")

        if action == "1":
            hunger = feed_pet(hunger)
        elif action == "2":
            happiness, hunger, event_type = play_with_pet(happiness, hunger)
            if event_type:
                print(f"\n⚠️ {pet_name} the {pet_kind} had a rough time due to a {event_type} incident.")
                choice = input("Do you want to take your pet to the vet? (yes/no): ").lower()
                if choice == "yes":
                    happiness, hunger = vet_visit(happiness, hunger)
                else:
                    print(f"\n💔 You chose not to help {pet_name}. Game over.")
                    break

        elif action == "3":
            hunger = sleep_pet(hunger)
        elif action == "4":
            print("🐾 Time to adopt a new pet!")
            break
        elif action == "5":
            print(f"👋 Goodbye! {pet_name} will miss you.")
            exit()
        else:
            print("❌ Invalid choice.")

        time.sleep(1)

        # Game over conditions
        if hunger >= 10:
            print(f"\n⚠️ {pet_name} is starving. Game over.")
            break
        if happiness <= 0:
            print(f"\n😢 {pet_name} is too sad to continue. Game over.")
            break
