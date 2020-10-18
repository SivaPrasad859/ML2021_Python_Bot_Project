import webbrowser

def cartoon_channels():
    print("There are 3 Major Channels for Childrens : ")
    stories = {
        "Cartoon Network" : "A classic channel that is timeless, this is a great channel to watch cartoons with your kids.",
        "Disney Kids" : "Which kid doesn’t love a Disney show toon? Disney Kids has shows like the classic Mickey Mouse Clubhouse and Kim Perfect.",
        "Hungama" : "This regional cartoon channel is a magnificent way for your young ones to pick up the local languages of the country."
    }
    i = 1
    for k,v in stories.items():
        print(f"    {i}) {k} : {v}")
        i+=1

    flag = 0
    print("\nIf You want to know more information [y/n] or if you want more channels [m] : ",end=" ")
    info = input().lower()
    if(info == "y"):
        channel = input("\nEnter specific channel name without spaces : ").lower()
        if(channel == "cartoonnetwork"):
            webbrowser.open("https://en.wikipedia.org/wiki/List_of_programmes_broadcast_by_Cartoon_Network_(India)")
        elif(channel == "disneykids"):
            webbrowser.open("https://disneynow.com/all-shows")
        elif(channel == "hungama"):
            webbrowser.open("https://latestnews.fresherslive.com/articles/hungama-tv-schedule-today-145113")
        else:
            print(f"\nOops! Sorry we can't find '{channel}' channel :( , Do you want to explore more channels [y/n] : ",end=" ")
            more = input().lower()
            if(more == "y"):
                webbrowser.open("https://parenting.firstcry.com/articles/good-kid-friendly-tv-channels-that-parent-should-know-about/")
            else:
                flag = 1
                print("\nThanks! for Spending your valuable time with me, Have a good day :)") 
    elif(info == "m"):
        webbrowser.open("https://parenting.firstcry.com/articles/good-kid-friendly-tv-channels-that-parent-should-know-about/")
    if(flag != 1): print("\nThanks! for Spending your valuable time with me, Have a good day :)")

def doctor_care():
    webbrowser.open("https://www.doctorinsta.com/pediatrics.php")


def baby_store():
    print("Choose You Store : ")
    stores = ["FirstCare","Amazon","FlipCart","IndiaMart"]
    i = 1
    for k in stores:
        print(f"    {i}) {k}")
        i+=1
    num = int(input("Enter the Number Where You Want to Shop [1-4]  (or) Do you want to Explore More Stores [5] : "))
    if(num==1):
        webbrowser.open("https://www.firstcry.com/health-and-safety")
    elif(num==2):
        webbrowser.open("https://www.amazon.in/s?k=baby+care+products+combo&adgrpid=58071909519&ext_vrnc=hi&gclid=CjwKCAjwrKr8BRB_EiwA7eFapleuT4Uw7ooEp-_6HhT0aMMB4NHWyVCB5Q22_3sDCcWIPJbdYm6v1xoCuJ0QAvD_BwE&hvadid=294138541915&hvdev=c&hvlocphy=9299531&hvnetw=g&hvqmt=b&hvrand=1544092810991076609&hvtargid=kwd-706006018072&hydadcr=11207_1734841&tag=googinhydr1-21&ref=pd_sl_9q5o4i146_b")
    elif(num==3):
        webbrowser.open("https://www.flipkart.com/baby-care/pr?sid=kyh")
    elif(num==4):
        webbrowser.open("https://dir.indiamart.com/indianexporters/baby.html")
    elif(num==5):
        webbrowser.open("https://www.shumee.in/collections/storage-bags-bibs-accessories-for-kids?gclid=CjwKCAjwrKr8BRB_EiwA7eFapoCyXOvmjDiKRm-Yx1U87fUuLkZNBQLqqZwndshOVV9FYhvazdLM4hoCfZ8QAvD_BwE")
    else:
        print("Oops! Invalid Number, Do you want to Explore More Stores [y/n] : ",end=" ")
        explore = input()
        if(explore=="y"):
            webbrowser.open("https://babysworld.in/")
        else:
            print("\nThanks! for Spending your valuable time with me, Have a good day :)")

def medical_store():
    print("These are the 4 major Medical Stores in India : ")
    stores = ["Netmeds","Medplus Mart","Medidart","1mgAYUSH"]
    i = 1
    for k in stores:
        print(f"    {i}) {k}")
        i+=1
    num = int(input("Enter the Number Where You Want to Shop [1-4] (or) Do you want to Explore More Stores [5]: "))
    if(num==1):
        webbrowser.open("https://www.netmeds.com/")
    elif(num==2):
        webbrowser.open("https://www.medplusmart.com/")
    elif(num==3):
        webbrowser.open("https://www.indiamart.com/medidart/")
    elif(num==4):
        webbrowser.open("https://dir.indiamart.com/indianexporters/baby.html")
    elif(num==5):
        webbrowser.open("https://theultrasoft.com/medical/top-10-online-medical-store-india/")
    else:
        print("Oops! Invalid Number, Do you want to Explore More Stores [y/n] : ",end=" ")
        explore = input()
        if(explore=="y"):
            webbrowser.open("https://theultrasoft.com/medical/top-10-online-medical-store-india/")
        else:
            print("\nThanks! for Spending your valuable time with me, Have a good day :)")





    


