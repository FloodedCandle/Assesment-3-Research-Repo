import Ticketing 
print("\n\n ========== TICKET SYSTEM ==========\n\n")

Ticketing.menu()
print("\n")

selection = int(input("Enter your option: "))

while selection != 0:
    if selection == 1: 
        #preform option 1
        print()
        print("1 called")
        
    elif selection == 2:
        #do option 2
        print()
        print("2 called")
        
    elif selection == 3:
        #do option 3
        print()
        print("3 called")
        
    elif selection == 4:
        #do option 4
        print()
        print("4 called")
        
    else:
        print()
        print("Invalid option")
    
    print("\n")
    Ticketing.menu()
    print("\n")

    selection = int(input("Enter your option: "))

print("system shutdown")
# Tickets can be submitted by providing all of the following information:
# Staff ID,
# Ticket creator name,
# Contact email
# Description of the issue


# Statistics:

# There should be a way to keep track of:
# The number of tickets submitted
# The number of resolved tickets
# The Number of open tickets
# A way to display those statistics to the console.


# Displaying the ticket:

# There should be a way to display the ticket information:
# Ticket number,
# Name of the ticket’s creator,
# StaffID,
# Email address,
# Description of the issue,
# Response from the IT department and ticket status (open, closed or reopened).
