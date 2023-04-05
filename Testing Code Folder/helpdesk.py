class Ticket:
    # class variables to store the ticket information and statistics
    tickets_created = 0
    tickets_resolved = 0
    tickets_to_solve = 0
    
    def __init__(self, staff_id, creator_name, contact_email, description):
        # instance variables to store the ticket information
        self.staff_id = staff_id
        self.creator_name = creator_name
        self.contact_email = contact_email
        self.description = description
        self.ticket_number = Ticket.tickets_created + 2001
        self.response = "Not Yet Provided"
        self.status = "Open"
        
        # increment the class variables for ticket statistics
        Ticket.tickets_created += 1
        Ticket.tickets_to_solve += 1
        
    def resolve_ticket(self):
        if self.status == "Open":
            if "Password Change" in self.description:
                # generate new password and set the response
                new_password = self.staff_id[:2] + self.creator_name[:3]
                self.response = f"New password generated: {new_password}"
            self.status = "Closed"
            Ticket.tickets_resolved += 1
            Ticket.tickets_to_solve -= 1
            
    def reopen_ticket(self):
        if self.status == "Closed":
            self.status = "Reopened"
            Ticket.tickets_resolved -= 1
            Ticket.tickets_to_solve += 1
            
    def provide_response(self, response):
        if self.status == "Open":
            self.response = response
            
    def print_ticket_info(self):
        print(f"Ticket Number: {self.ticket_number}")
        print(f"Ticket Creator: {self.creator_name}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Email Address: {self.contact_email}")
        print(f"Description: {self.description}")
        print(f"Response: {self.response}")
        print(f"Ticket Status: {self.status}")
