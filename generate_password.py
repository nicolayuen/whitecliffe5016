staff_id="123456"
ticket_creator="john"

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

#Provide different values for staff_ID and ticket_creator
print("Your new password is: ")
print(generate_password(staff_id,ticket_creator,1))