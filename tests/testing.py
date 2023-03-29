import random


class Ticket():
    ticket_count = 2000

    def __init__(self, ticket_creator, staff_id, email, description):
        self.ticket_number = str(Ticket.ticket_count)
        self.ticket_creator = ticket_creator
        self.staff_id = staff_id
        self.email = email
        self.description = description
        self.response = "not provided yet"
        self.status = "Submitted"
        Ticket.ticket_count += 1

    def display(self):
        # print(f"Ticket Number: {self.ticket_number}")
        # print(f"Ticket Creator: {self.ticket_creator}")
        # print(f"Staff ID: {self.staff_id}")
        # print(f"Email: {self.email}")
        # print(f"Description: {self.description}")

        print("\n************************")
        print("Ticket number:",self.ticket_number)
        print("Staff Id: ", self.staff_id)
        print("Name: ",self.ticket_creator)
        print("Email: ",self.email)
        print("Issue: ",self.description)
        print("Response:", self.response)
        print("Status:",self.status)
        # print("Response: ",self.response)
        # print("Ticket Status: ", self.status)
        print("************************\n")

       
class TicketSystem():
    tickets = []

    tickets = [Ticket("Inna", "INNAM", "inna@whitecliffe.co.nz", "My monitor stopped working"), 
               Ticket("Maria", "MARIAH", "maria@whitecliffe.co.nz", "Request for a videocamera to conduct webinars")]

    

    
    def create_ticket():
        print("\n========== CREATING NEW TICKET ==========\n")
        ticket_creator = input("Ticket Creator: ")
        staff_id = input("Staff ID: ")
        email = input("Email: ")
        description = input("Description: ")
        if "password change" in description.lower():
            response = staff_id[:2] + ticket_creator[:3]
            new_ticket = Ticket(ticket_creator, staff_id, email, description)
            new_ticket.response = response
        else:
            new_ticket = Ticket(ticket_creator, staff_id, email, description)
        TicketSystem.tickets.append(new_ticket)
        print("\nTicket submitted successfully.\n")

    
    def display_tickets():
        print("\n========== ALL TICKETS ==========\n")
        if not TicketSystem.tickets:
            print("No tickets found.")
        else:
            for ticket in TicketSystem.tickets:
                ticket.display()

    
    def respond_to_ticket():
        print("\n========== RESPOND TO TICKET ==========\n")
        ticket_number = input("Enter the ticket number: ")
        found_ticket = False
        for ticket in TicketSystem.tickets:
            if ticket.ticket_number == ticket_number:
                response = input("Enter your response: ")
                ticket.response = response
                ticket.status = "Response Provided"
                print("\nResponse added successfully.")
                found_ticket = True
                break
        if not found_ticket:
            print("\nTicket not found.")

    
    def reopen_ticket():
        print("\n========== REOPEN TICKET ==========\n")
        ticket_number = input("Enter the ticket number: ")
        found_ticket = False
        for ticket in TicketSystem.tickets:
            if ticket.ticket_number == ticket_number:
                ticket.status = "Submitted"
                print("\nTicket reopened successfully.")
                found_ticket = True
                break
        if not found_ticket:
            print("\nTicket not found.")

    
    def display_statistics():
        print("\n========== STATISTICS ==========\n")
        print("Total number of tickets:", len(TicketSystem.tickets))
        submitted_count = 0
        response_count = 0
        password_change_count = 0
        # total_tickes = 0
        for ticket in TicketSystem.tickets:
            if ticket.status == "Submitted":
                submitted_count += 1
            elif ticket.status == "Response Provided":
                response_count += 1
            elif ticket.status == "Password Change":
                password_change_count += 1
        print("Number of submitted tickets:", submitted_count)
        print("Number of tickets with response:", response_count)
        print("Number of password change tickets:", password_change_count)


def menu():
    print("\n========== TICKET SYSTEM ==========\n")
    print("[1] Display all tickets.")
    print("[2] Submit new ticket.")
    print("[3] Provide response to ticket.")
    print("[4] Reopen ticket.")
    print("[5] Display statistics.")
    print("[0] Exit.")



if __name__ == "__main__":
    menu()

    selection = int(input("Enter your option: "))
        
    while selection != 0:
        if selection == 1:
            # Display all tickets.
            TicketSystem.display_tickets()
            menu()
                

        elif selection == 2:
            # creating new tickets
            TicketSystem.create_ticket()
            menu()

        elif selection == 3:
            # provide response to ticket.
            print("hitting response to ticket")
            TicketSystem.respond_to_ticket()
            menu()
            
        elif selection == 4:
            # reopen ticket.
            print("hitting reopen ticket")
            TicketSystem.reopen_ticket()
            menu()

        elif selection == 5:
            # display statistics.
            print("hitting statistics")
            TicketSystem.display_statistics()
            menu()
            
        else:
            print("\nInvalid option. Choose from [0-5]")
            menu()

        selection = int(input("Enter your option: "))

    print("\nSystem shutdown.")
