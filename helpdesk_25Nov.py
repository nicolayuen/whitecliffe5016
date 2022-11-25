#Generate new ticket nuber
get_ticket = True
a=2000
generate_ticket=a

        
#Generate new password
def generate_password(staff_ID,ticket_creator,ticket_no):
    password_number_list = []
    i = 0
    if ticket_no < 5:
        while ticket_no != 0:
            password_number_list.append(staff_ID[:2] + ticket_creator[:3])
            i = i+1
            ticket_no = ticket_no - 1
    else:
        for i in range(5):
            password_number_list.append(staff_ID + ":" + ticket_creator[:3] + str(2000+ticket_no))
            i = i+1
            ticket_no = ticket_no - 1
        password_number_list = password_number_list[::-1]

    return password_number_list


#ticket statistics
x=0
y=0
z=0

tickets_created=x
tickets_resolved=y
tickets_unresolved=z

menu = "1: Submit ticket\n2: Respond to a ticket\n3: Resolve a ticket\n4: Reopen a ticket"

print("")
print(menu)
print("")

get_menu = True

while get_menu:
    answer = input("Enter your menu item:\n")
    if answer == "1":
        print("1: Submit a ticket\n")
        staff_id=input("Enter your staff ID:")
        ticket_creator=input("Name:")
        print('Hello, ' + ticket_creator)
        contact_email=input("Contact Email:")
        from datetime import date
        today = date.today()
        print("Date:")
        print(today)
        issue = input("Support issue:")
        get_tickets = False
        get_ticket_no = input("Submit ticket?\n")
        if get_ticket_no == "True":
            a=(a+1)
            print("Ticket number:")
            print(a)
        if get_ticket_no == "False":
            get_ticket = False
            issue = 0
            print("No ticket number") 
        print("")
        print("You've submitted a ticket. "
              "Nice one!\n")
        x=(x+1)
        tickets_created=x
        z=(z+1)
        tickets_unresolved=z
        print(menu)
        print("")
        # If password change is requested, password change loop is run
        # Exit loop - get menu
        get_menu = False
    if answer == "2":
        print("2: Respond to a ticket\n")
        ticket_number=input("Ticket number:") 
        issue = 0
        status = ("Open")
        print("")
        response=input("Type your response:")
        print("")
        print("Ticket status:")
        print(status)
        print("")
        print("You've responded to this ticket.")
        print("")
        # Exit loop - get menu
        get_menu = True
        get_tickets = False
    if answer == "3":
        print("3: Resolve a ticket\n")
        ticket_number=input("Ticket number:") 
        issue = 0
        status = ("Resolved")
        print("")
        print("Status: ")
        print(status)
        print("You've resolved this ticket.")
        print("")
        y=(y+1)
        tickets_resolved=y
        z=(z-1)
        tickets_unresolved=z
        print(menu)
        print("")
        # Exit loop - get menu
        get_menu = True
        get_tickets = False
    if answer == "4":
        print("4: Reopen a ticket\n")
        ticket_number=input("Ticket number:") 
        issue = 0
        print("")
        Print = ("Status: ")        
        status = ("Reopened")
        print(status)
        print("You've reopened this ticket.")
        print("")
        y=(y-1)
        tickets_resolved=y
        z=(z+1)
        tickets_unresolved=z
        print(menu)
        print("")
        # Exit loop - get menu
        get_menu = True
        get_tickets = False
    if issue == "password change":
        #Provide different values for staff_ID and ticket_creator
        print("")
        print("You've requested a password change. The new password is: ")
        print(generate_password(staff_id,ticket_creator,1))
        print("")
        print("This ticket has been closed.")
        tickets_resolved=y+1
        tickets_unresolved=z
        print(menu)
        print("")
        # Exit loop - get menu
        get_menu = True
        get_tickets = False
        issue == 0
    else:
        issue == 0
        print("Tickets Created:")
        print(tickets_created)
        print("Tickets resolved")
        print(tickets_resolved)
        print("Tickets to solve")
        print(tickets_unresolved)
        print("")
        get_menu = True
        get_tickets = False