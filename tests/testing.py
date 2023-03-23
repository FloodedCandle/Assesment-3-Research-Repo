class HelpDeskTicketingSystem:
    def __init__(self):
        self.counter = 0
        self.tickets = []
        self.num_tickets_submitted = 0
        self.num_tickets_resolved = 0
        self.num_open_tickets = 0
    
    def create_ticket(self, staff_id, ticket_creator, email, description):
        ticket_number = f'I{self.counter + 2000}'
        self.counter += 1
        
        if 'password change' in description.lower():
            new_password = f'{staff_id[:2]}{ticket_creator[:3]}'
            response = f'New password: {new_password}'
        else:
            response = 'Not Yet Provided'
        
        ticket = {
            'Ticket Number': ticket_number,
            'Ticket Creator': ticket_creator,
            'Staff ID': staff_id,
            'Email': email,
            'Description': description,
            'Status': 'Open',
            'Response': response
        }
        self.tickets.append(ticket)
        self.num_tickets_submitted += 1
        self.num_open_tickets += 1
        return ticket
    
    def respond_to_ticket(self, ticket_number, response):
        for ticket in self.tickets:
            if ticket['Ticket Number'] == ticket_number:
                ticket['Response'] = response
                ticket['Status'] = 'Closed'
                self.num_tickets_resolved += 1
                self.num_open_tickets -= 1
                return True
        return False
    
    def reopen_ticket(self, ticket_number):
        for ticket in self.tickets:
            if ticket['Ticket Number'] == ticket_number:
                ticket['Status'] = 'Reopened'
                self.num_tickets_resolved -= 1
                self.num_open_tickets += 1
                return True
        return False
    
    def display_ticket(self, ticket_number):
        for ticket in self.tickets:
            if ticket['Ticket Number'] == ticket_number:
                print('Ticket Number:', ticket['Ticket Number'])
                print('Ticket Creator:', ticket['Ticket Creator'])
                print('Staff ID:', ticket['Staff ID'])
                print('Email:', ticket['Email'])
                print('Description:', ticket['Description'])
                print('Status:', ticket['Status'])
                print('Response:', ticket['Response'])
                return True
        return False
    
    def display_statistics(self):
        print('Number of Tickets Submitted:', self.num_tickets_submitted)
        print('Number of Resolved Tickets:', self.num_tickets_resolved)
        print('Number of Open Tickets:', self.num_open_tickets)