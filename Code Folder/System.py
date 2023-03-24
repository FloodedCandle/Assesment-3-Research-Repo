from Ticketing import *


if __name__ == "__main__":
    # Tickets = []
    ticket_count = 2000
    ticket_amount = 0

    ts = TicketSystem()

    menu()

    print("\n")

    selection = int(input(bcolors.OKBLUE +"Enter your option: " + bcolors.ENDC))
                    
    while selection != 0:
        if selection == 1:
            # Display all tickets.
            print("hitiing display")
            
            menu()
            

        elif selection == 2:
            # creating new tickets
            ts.CreatingTicket()
            menu()
            ticket_count+=1
            

        elif selection == 3:
            # rovide response to ticket.
            print()
            

        elif selection == 4:
            # reopen ticket.
            print()
            

        elif selection == 5:
            # Display Statistics.
            print()
            

        else:
            print()
            print("Invalid option. Choose from [0-5]")
            menu()
            

        # print("\n")
        # Ticketing.menu()
        # print("\n")

        selection = int(input(bcolors.OKBLUE +"Enter your option: " + bcolors.ENDC))
                        
    print("system shutdown")
