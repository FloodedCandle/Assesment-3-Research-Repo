from Ticketing import *

if __name__ == "__main__":
    Tickets = []
    ticket_count = 2000
    ticket_amount = 0

    def display():
        for t in Tickets:
            t.display()

    menu()

    print("\n")

    selection = int(input(bcolors.OKBLUE +"Enter your option: " + bcolors.ENDC))
                    
    while selection != 0:
        if selection == 1:
            # preform option 1
            display
            menu()
            

        elif selection == 2:
            # creating new tickets
            TicketSystem.CreatingTicket()
            menu()
            ticket_count+=1
            

        elif selection == 3:
            # do option 3
            print()
            

        elif selection == 4:
            # do option 4
            print()
            

        elif selection == 5:
            # do option 5
            print()
            

        else:
            print()
            print("Invalid option. Choose from [0-5]")
            

        # print("\n")
        # Ticketing.menu()
        # print("\n")

        selection = int(input(bcolors.OKBLUE +"Enter your option: " + bcolors.ENDC))
                        
    print("system shutdown")
