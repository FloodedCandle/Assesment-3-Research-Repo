class bcolors:
    #  print(bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def menu():
    print(bcolors.OKBLUE + "\n ========== TICKET SYSTEM ==========\n" + bcolors.ENDC)
    print("[1] Display all tickets.")
    print("[2] Submit new ticket.")
    print("[3] provide response to ticket.")
    print("[4] reopen ticket.")
    print("[5] Display Statistics.")
    print("[0] Exit.")


class TicketSystem():
    

    def CreatingTicket():
        print(bcolors.OKBLUE +"\n ========== TICKETS SUBMITTED ==========\n" + bcolors.ENDC)
        Ticket_Number = input("Ticket Number: ")
        Ticket_Creator = input("Ticket Creator: ")
        Staff_ID = input("Staff ID: ")
        Email = input("Email: ")
        Description = input("Description: ")
        Response = None
        Ticket_Status = None
        
    
class Ticket():
    Ticket_Number = None
    Ticket_Creator = None
    Staff_ID = None
    Email = None
    Description = None
    Response = None
    Ticket_Status =None

    def __init__(self, Ticket_Number, Ticket_Creator, Staff_ID, Email, Description, Response):
        self.Ticket_Number = Ticket_Number
        self.Ticket_Creator = Ticket_Creator
        self.Staff_ID = Staff_ID
        self.Email = Email
        self.Description = Description
        self.Response = Response
        self.Ticket_Status = "Submitted"

    def display(self):
        print(bcolors.OKBLUE + "\n ========== TICKETS SUBMITTED ==========\n" + bcolors.ENDC)
        print("Ticket Number: "+ self.Ticket_Number)
        print("Ticket Creator: "+ self.Ticket_Creator)
        print("Staff ID: "+ self.Staff_ID)
        print("Email: "+ self.Email)
        print("Description: "+ self.Description)
        print("Response: "+ self.Response)
        print("Ticket Status: "+ self.Ticket_Status)


# author = "jeffrey"

# # if __name__ == "__main__":
# #     menu()
