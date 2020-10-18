import random  
from Activities import cartoon_channels, doctor_care, baby_store, medical_store 
from Greetings import greet_and_intro, menu, cos_name

"""
This is an Child Care ChatBot : 
1) Firstly the bot used to greet the coustomer by asking the users name and there child name then it will greet the user according to the timestamp whether it is good morning/good evening.
2) Secondly the Menu list will be visible to the user and asks the user to enter the desired number by giving some description.
3) Thirdly It provied all the necessary baby care products, doctor care, medical products, cartoon channels and takes the user to their desired websites in google chrome.
4) Finally by pressing 5 we will quit the bot by asking one more time, else it will continue till the user accepts his quit. 

"""

greet_and_intro()
while(True):
    menu()
    choice = int(input("Enter Your Choice Here : "))
    if(choice==1):
        cartoon_channels()
    elif(choice==2):
        doctor_care()
    elif(choice==3):
        baby_store()
    elif(choice==4):
        medical_store()
    elif(choice==5):
        q = input(f"\nMr/Ms.{cos_name()}, Are You Sure!! Do you want to Quit [y/n] : ")
        if(q=="y"):
            print("\nThanks! for Spending your valuable time with me, Have a good day :)")
            quit()
    else:
        print("\nOops!! Invalid Number, Enter the Numbers from 1 to 5.")







