# Software_Project.py
#
# @ author: N.Yuen20220963
# date: November2022

#Please enter your Staff ID:
staff_ID="12345"

#Ticket created by:
ticket_creator="John Smith"

#Contact email:
contact_email="email@email.com"

#Please enter your support issue:
description="description"

x=2000

ticket_no=x+1

#Prints out ticket
print ("Kia Ora, welcome to the helpdesk.")
print ("")
print ("Ticket number:")
print(ticket_no)
print ("")
print ("Staff ID:")
print (staff_ID)
print ("")
print ("Ticket creator:")
print(ticket_creator)
print ("")
print ("Contact Email")
print(contact_email)
print ("")
print ("Description:")
print(description)

print("")


# setting the maxsplit parameter to 1, will return a list with 2 elements!
split1=staff_ID.split("3")
split2=ticket_creator.split("3")

print(split1)
print(split2)

newpassword="-".join(split1),(split2)
print(split1),(split2)

print(newpassword)
 
print("")

# input string
newpassword2 = (split1),(split2)
print("The new password is")
print(newpassword)
print("")
# print the string after split method
print(staff_ID.split("3"))
print(ticket_creator.split("2"))
# print the string after join method
print("-".join(staff_ID.split("2"))),("-".join(ticket_creator.split()))
print("")
print("if description is password change")
print("new_password=str(staff_ID)(ticket_creator)")
print("The first two characters of the staff ID, followed by the first three characters of the ticket creator name. ")
