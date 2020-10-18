import random
import datetime

def greet_and_intro():
    global name
    global child_name
    name = input("Enter You Name : ")
    child_name = input("Enter You Child Name : ")
    responses = [
        f"\n{get_time()} Mr/Ms.{name}, This is Child care Bot. Please Type the given Options to handle your child {child_name} in a right way.",
        f"\n{get_time()} Mr/Ms.{name}, I am Child Care Bot. How can I assest You. Kindly Please Choose the given Options to handle your child {child_name} in a right way",
        f"\n{get_time()} Mr/Ms.{name}, This is Child Care Bot. How can I help You, Please Select the Options given below to handle your child {child_name} in a right way.",
        f"\n{get_time()} Mr/Ms.{name} I am Child Care Bot, Do you want to learn how to treat your child {child_name} in a right way then select the given Options."
    ]

    print(random.choice(responses))

def cos_name():
    return name

def get_time():
    current_time = datetime.datetime.now()
    hour = current_time.hour
    greeting = "Good morning!" if 5<=hour<12 else "Good afternoon!" if 12<=hour<17 else "Good evening!" if 17<=hour<22 else "Oh! It's High Time!" 
    return greeting

def menu():
    print(f"\nPress 1 if you want to know which Cartoon Channels {child_name} wants to watch.")
    print(f"Press 2 if you want to Consult the best Doctors all over the India through online.")
    print(f"Press 3 if you want to shop the best Baby Care Products to your child {child_name}.")
    print(f"Press 4 if you want to buy the legal and trusty Medicines to {child_name}.")
    print(f"Press 5 if you want to Quit the Bot.\n")
    





