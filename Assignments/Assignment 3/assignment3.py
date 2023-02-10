import sys                                                                                                                              #importing the
import os                                                                                                                               # required libraries
current_dir_path = os.getcwd()
reading_file_name = "input.txt"
reading_file_path = os.path.join(current_dir_path, reading_file_name)
writing_file_name = "output.txt"
writing_file_path = os.path.join(current_dir_path, writing_file_name)
category_list = []
category_data_list = []
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']  #alphabet for row naming
all_seats = {}


#defining a writing function to write the output
def write(output):
    with open(writing_file_path, "a") as w:
        w.write(output)


#defining a create function to create category
def CREATECATEGORY():
    if category not in category_list:
        category_data_list.append(line)
        seat_count = int(rows)*int(columns)
        category_list.append(category)
        output = "The category '" + category + "' having " + str(seat_count) + " seats has been created"
        print(output)
        write(output + "\n")
        for i in reversed(range(int(rows))):                                                                                            #reversed because seat alignment needs so
            for j in range(int(columns)):
                temp_dict = {category + " " + alphabet[i] + str(j): "X"}                                                                #creating a temporary dictionary to update the main one
                all_seats.update(temp_dict)
    else:
        output = "Warning: Cannot create the category for the second time. The stadium has already " + category + "."
        print(output)
        write(output + "\n")


#defining a sell function to sell the specified seats
def SELLTICKET():
    checklist1 = []                                                                                                                     #creating a checking list to use while checking for error statements
    rowlist = []                                                                                                                        #listing rows
    columnlist = []                                                                                                                     #listing columns
    category = line[2]
    for i in range(3, len(line)):
        selected_seat = line[i]
        for key, value in all_seats.items():
            checklist1.append(key[0:13])
        for key, value in all_seats.items():
            rowlist.append(key)
            for i in rowlist:
                if i.startswith(category):
                    columnlist.append(i[13:])
        if "-" not in selected_seat:                                                                                                    #determining if a range is specified
            if category + " " + selected_seat[0] in checklist1 and category + " " + selected_seat not in all_seats:                     #column checking
                output = "Error: The category '" + category + "' has less column than specified index " + selected_seat + "!"
                print(output)
                write(output + "\n")
            if category + " " + selected_seat[0] not in checklist1:                                                                     #checking for less row && less row and column
                if selected_seat[1:] in columnlist:
                    output = "Error: The category '" + category + "' has less row than specified index " + selected_seat + "!"
                    print(output)
                    write(output + "\n")
                else:
                    output = "Error: The category '" + category + "' has less row and column than specified index " + selected_seat + "!"
                    print(output)
                    write(output + "\n")
            if category + " " + selected_seat in all_seats:
                if all_seats[category + " " + selected_seat] != "X":                                                                    #checking if it has been sold
                    output = "Warning: The seat " + selected_seat + " cannot be sold to " + name + " since it was already sold!"
                    print(output)
                    write(output + "\n")
                else:
                    output = "Success: " + name + " has bought " + selected_seat + " at " + category
                    print(output)
                    write(output + "\n")
                    if ticket_type == "student":                                                                                        #updating category according to the ticket type
                        all_seats[category + " " + selected_seat] = "S"
                    if ticket_type == "full":
                        all_seats[category + " " + selected_seat] = "F"
                    if ticket_type == "season":
                        all_seats[category + " " + selected_seat] = "T"
        else:
            checklist2 = []                                                                                                             #creating a checking list to use while checking for error statements
            seat_list = []                                                                                                              #creating a list so dictionary updating would be easier
            seat_elements = selected_seat.split("-")
            column_letter = seat_elements[0][0:1]
            first_seat_num = seat_elements[0][1:]
            last_seat_num = seat_elements[1]
            last_seat = column_letter + seat_elements[1]
            if category + " " + last_seat[0] in checklist1 and category + " " + last_seat not in all_seats:                             #checking the last seat is enough
                output = "Error: The category '" + category + "' has less column than specified index " + selected_seat + "!"           # because this block requires all seats
                print(output)                                                                                                           # in the given range to be created.
                write(output + "\n")                                                                                                    #if the last seat in the range is created
            if category + " " + last_seat[0] not in checklist1:                                                                         # seats before that have to be created.
                if last_seat[1:] in columnlist:
                    output = "Error: The category '" + category + "' has less row than specified index " + selected_seat + "!"
                    print(output)
                    write(output + "\n")
                else:
                    output = "Error: The category '" + category + "' has less row and column than specified index " + selected_seat + "!"
                    print(output)
                    write(output + "\n")
            if category + " " + last_seat in all_seats:
                for i in range(int(first_seat_num), int(last_seat_num)+1):
                    checklist2.append(all_seats[category + " " + column_letter + str(i)])
                    seat_list.append(column_letter + str(i))
                if "S" in checklist2 or "F" in checklist2 or "T" in checklist2:                                                         #checking if any seat in the given range is already sold
                    output = "Error: The seats " + selected_seat + " cannot be sold to " + name + " due some of them have already been sold!"
                    print(output)
                    write(output + "\n")
                else:
                    for i in seat_list:
                        if ticket_type == "student":                                                                                    #updating category according to the ticket type
                            all_seats[category + " " + i] = "S"
                        if ticket_type == "full":
                            all_seats[category + " " + i] = "F"
                        if ticket_type == "season":
                            all_seats[category + " " + i] = "T"
                    output = "Success: " + name + " has bought " + selected_seat + " at " + category
                    print(output)
                    write(output + "\n")


#defining a cancel function to cancel the specified ticket
def CANCELTICKET():
    checklist1 = []                                                                                                                     #creating a checking list to use while checking for error statements
    rowlist = []                                                                                                                        #listing rows
    columnlist = []                                                                                                                     #listing columns
    for i in range(1, len(line)):
        selected_seat = line[i]
        for key, value in all_seats.items():
            checklist1.append(key[0:13])
        for key, value in all_seats.items():
            rowlist.append(key)
            for i in rowlist:
                if i.startswith(category):
                    columnlist.append(i[1:])
        if category + " " + selected_seat[0] in checklist1 and category + " " + selected_seat not in all_seats:                         #column checking
            output = "Error: The category '" + category + "' has less column than specified index " + selected_seat + "!"
            print(output)
            write(output + "\n")
        if category + " " + selected_seat[0] not in checklist1:                                                                         #checking for less row && less row and column
            if selected_seat[1:] in columnlist:
                output = "Error: The category '" + category + "' has less row than specified index " + selected_seat + "!"
                print(output)
                write(output + "\n")
            else:
                output = "Error: The category '" + category + "' has less row and column than specified index " + selected_seat + "!"
                print(output)
                write(output + "\n")
        if category + " " + selected_seat in all_seats:                                                                                 #deciding if cancellation is necessary
            if all_seats[category + " " + selected_seat] != "X":
                all_seats[category + " " + selected_seat] = "X"
                output = "Success: The seat " + selected_seat + " at '" + category + "' has been canceled and now ready to sell again"
                print(output)
                write(output + "\n")
            else:
                output = "Error: The seat " + selected_seat + " at '" + category + "' has already been free! Nothing to cancel"
                print(output)
                write(output + "\n")


#defining a balance function to display the total income of the specified category
def BALANCE():
    students_sum = 0                                                                                                                    #creating initial values for ticket types
    full_sum = 0
    season_sum = 0
    value_list = []
    for key, value in all_seats.items():
        if category in key:
            value_list.append(value)
    for i in value_list:                                                                                                                #updating ticket type values
        if i == "S":
            students_sum += 1
        if i == "F":
            full_sum += 1
        if i == "T":
            season_sum += 1
    sum = students_sum*10 + full_sum*20 + season_sum*250                                                                                #creating the total balance
    print("Category report of '" + category + "'")
    write("Category report of '" + category + "'" + "\n")
    print("-"*len("Category report of '" + category + "'"))
    write("-"*len("Category report of '" + category + "'") + "\n")
    print("Sum of students = " + str(students_sum) + ", Sum of full pay = " + str(full_sum) + ", Sum of season ticket = " + str(season_sum) + ", and Revenues = " + str(sum) + " Dollars")
    write("Sum of students = " + str(students_sum) + ", Sum of full pay = " + str(full_sum) + ", Sum of season ticket = " + str(season_sum) + ", and Revenues = " + str(sum) + " Dollars" + "\n")


#defining a show function to visualize
def SHOWCATEGORY():
    for i in category_data_list:
        if line in i:
            rows = i[1][0:2]
            columns = i[1][3:]
            print("Printing category layout of " + category)
            write("Printing category layout of " + category + "\n")
            for i in reversed(range(int(rows))):
                print(alphabet[i], end=" ")
                write(alphabet[i] + " ")
                for j in range(int(columns)):
                    print(all_seats[category + " " + alphabet[i] + str(j)], end="  ")
                    write(all_seats[category + " " + alphabet[i] + str(j)] + "  ")
                print("")                                                                                                               #printing new line
                write("\n")
            for i in range(int(columns)):
                if len(str(i)) == 1:
                    print("  " + str(i), end="")
                    write("  " + str(i))
                else:
                    print(" " + str(i), end="")
                    write(" " + str(i))
            print("")                                                                                                                   #printing new line
            write("\n")
        else:
            pass


#Driver Code
if sys.argv[1] == "input.txt":
    with open("input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            if "CREATECATEGORY " in line:
                line = line[15:].replace("\n", "").replace(" ", ", ").split(", ")
                category = line[0]
                rows = line[1][0:2]
                columns = line[1][3:5]
                CREATECATEGORY()
            if "SELLTICKET " in line:
                line = line[11:].replace("\n", "").replace(" ", ", ").split(", ")
                name = line[0]
                ticket_type = line[1]
                SELLTICKET()
            if "CANCELTICKET " in line:
                line = line[13:].replace("\n", "").replace(" ", ", ").split(", ")
                category = line[0]
                CANCELTICKET()
            if "BALANCE " in line:
                line = line[8:].replace("\n", "").replace(" ", ", ")
                category = line
                BALANCE()
            if "SHOWCATEGORY " in line:
                line = line[13:].replace("\n", "")
                category = line
                SHOWCATEGORY()
else:
    pass
