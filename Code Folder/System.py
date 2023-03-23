import Ticketing
Ticketing.menu()

print("\n")

selection = int(input(Ticketing.bcolors.OKBLUE +"Enter your option: " + Ticketing.bcolors.ENDC))
                
while selection != 0:
    if selection == 1:
        # preform option 1
        print()
        Ticketing.option1()

    elif selection == 2:
        # do option 2
        print()
        Ticketing.option2()

    elif selection == 3:
        # do option 3
        print()
        Ticketing.option3()

    elif selection == 4:
        # do option 4
        print()
        Ticketing.option4()

    elif selection == 5:
        # do option 5
        print()
        Ticketing.option5()

    else:
        print()
        print("Invalid option. Choose from [0-5]")
        Ticketing.menu()

    # print("\n")
    # Ticketing.menu()
    # print("\n")

    selection = int(input(Ticketing.bcolors.OKBLUE +"Enter your option: " + Ticketing.bcolors.ENDC))
                    
print("system shutdown")
