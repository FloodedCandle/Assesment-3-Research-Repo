import datetime

class Ticket:

    def __init__(self, id, requester_name, request, email, description):
        self.id = id
        self.requester_name = requester_name
        self.request = request
        self.email = email
        self.description = description
        
    def display(self):
        print("Ticket")
        print("Staff ID: ", self.id)
        print("Ticket creator name: ", self.requester_name)
        print("request: ", self.request)
        print("email: ", self.email)
        print("discription: ", self.description)


print("**** Input New Ticket ****")
staff_id = input("")
name = input("")
email = input("")

# Create tickets
t1 = Ticket(1, "John Doe", "Cannot access email" , "testing@gmail.com","help")
t2 = Ticket(2, "Jane Smith", "Password change","testing2@gmail.com","help2")
t3 = Ticket(3, "Bob Johnson", "Printer not working","testing3@gmail.com","help3")

t1.display()
t2.display()
t3.display()
