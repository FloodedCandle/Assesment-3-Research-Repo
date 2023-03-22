import Ticketing 

print(Ticketing.bcolors.OKBLUE + "\n\n ========== TICKET SYSTEM ==========\n\n" + Ticketing.bcolors.ENDC)

Ticketing.menu()
print("\n")

selection = int(input(Ticketing.bcolors.OKBLUE + "Enter your option: " + Ticketing.bcolors.ENDC))



while selection != 5:
    if selection == 1: 
        #preform option 1
        print()
        Ticketing.option1()
        
        
    elif selection == 2:
        #do option 2
        print()
        
        
    elif selection == 3:
        #do option 3
        print()
        Ticketing.option3()
        
    elif selection == 4:
        #do option 4
        print()
        Ticketing.option4()
        
    else:
        print()
        print("Invalid option")
    
    print("\n")
    Ticketing.menu()
    print("\n")

    selection = int(input(Ticketing.bcolors.OKBLUE + "Enter your option: " + Ticketing.bcolors.ENDC))

print("system shutdown")
