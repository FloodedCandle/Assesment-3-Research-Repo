class Ticket:
    ticket_counter = 0
    tickets_created = []
    tickets_resolved = []
    tickets_open = []
    
    def __init__(self, staff_id, creator_name, contact_email, description):
        self.staff_id = staff_id
        self.creator_name = creator_name
        self.contact_email = contact_email
        self.description = description
        Ticket.ticket_counter += 1
        self.ticket_number = Ticket.ticket_counter + 2000
        self.response = "Not Yet Provided"
        self.status = "Open"
        Ticket.tickets_created.append(self)
        Ticket.tickets_open.append(self)
    
    def resolve_ticket(self, response):
        if "Password Change" in self.description:
            new_password = self.generate_password()
            self.response = "New password generated: " + new_password
        else:
            self.response = response
        self.status = "Closed"
        Ticket.tickets_resolved.append(self)
        Ticket.tickets_open.remove(self)
    
    def reopen_ticket(self):
        self.status = "Reopened"
        Ticket.tickets_resolved.remove(self)
        Ticket.tickets_open.append(self)
    
    def generate_password(self):
        password = self.staff_id[:2] + self.creator_name[:3]
        return password
    
    def display_ticket(self):
        print("Ticket Number:", self.ticket_number)
        print("Ticket Creator:", self.creator_name)
        print("Staff ID:", self.staff_id)
        print("Email Address:", self.contact_email)
        print("Description:", self.description)
        print("Response:", self.response)
        print("Ticket Status:", self.status)
        print()
    
    @classmethod
    def ticket_stats(cls):
        print("Tickets Created:", len(cls.tickets_created))
        print("Tickets Resolved:", len(cls.tickets_resolved))
        print("Tickets To Solve:", len(cls.tickets_open))
        print()
    
def main():
    ticket1 = Ticket("INNAM", "Inna", "inna@whitecliffe.co.nz", "My monitor stopped working")
    ticket2 = Ticket("MARIAH", "Maria", "maria@whitecliffe.co.nz", "Request for a videocamera to conduct webinars")
    ticket3 = Ticket("JOHNS", "John", "john@whitecliffe.co.nz", "Password change")
    ticket3.resolve_ticket("")
    
    Ticket.ticket_stats()
    
    ticket1.resolve_ticket("The monitor has been replaced.")
    
    Ticket.ticket_stats()
    
    ticket2.reopen_ticket()
    
    Ticket.ticket_stats()
    
    Ticket.tickets_created[0].display_ticket()
    Ticket.tickets_created[1].display_ticket()
    Ticket.tickets_created[2].display_ticket()

if __name__ == '__main__':
    