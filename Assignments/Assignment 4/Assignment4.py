import sys                                                                      #importing the required module
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]                   #letter list to use on tables
used_letters = ["C", "B", "P", "S", "D"]                                        #used letter list to use while checking


#basically making an exception for number 10 in list
def fix_number(num):
    return str(num) if len(str(num)) == 2 else str(num) + " "


#function to organize the .in files
def txt_organizer(data):
    liste = []
    for j in data:
        liste.append([i if i else "-" for i in j.split(";")])
    return liste


#function to print and write the lists
def printer_and_writer(list1, list2):
    print("  " + " ".join(alphabet) + "\t\t" + "  " + " ".join(alphabet))
    print("\n".join([fix_number(i + 1) + " ".join(list1[i]) + "\t\t" + fix_number(i + 1) + " ".join(list2[i]) for i in range(len(list1))]))
    f.write("  " + " ".join(alphabet) + "\t\t" + "  " + " ".join(alphabet) + "\n")
    f.write("\n".join([fix_number(i + 1) + " ".join(list1[i]) + "\t\t" + fix_number(i + 1) + " ".join(list2[i]) for i in range(len(list1))]) + "\n")


#function to record the ship data to actual lists and dictionaries
def ship_recorder1(liste, dict_c, dict_s, dict_d):
    for i in range(len(liste)):
        for j in range(len(liste)):
            if liste[i][j] in used_letters:
                if liste[i][j] == "C":
                    temp = {alphabet[j] + str(i + 1): "C"}
                    dict_c.update(temp)
                if liste[i][j] == "S":
                    temp = {alphabet[j] + str(i + 1): "S"}
                    dict_s.update(temp)
                if liste[i][j] == "D":
                    temp = {alphabet[j] + str(i + 1): "D"}
                    dict_d.update(temp)


#function to record the ship data with optional files
def ship_recorder2(optional, n, dicti):
    for i in optional:
        if i.startswith(n):
            y_i = i.replace(n + ":", "").split(",")[1][0]
            x_i = i.replace(n + ":", "").split(",")[0]
            index = alphabet.index(y_i)
            if "B" in n:
                if "right" in i:
                    for j in range(4):
                        temp = {alphabet[index + j] + x_i: n[0]}
                        dicti.update(temp)
                if "down" in i:
                    for j in range(4):
                        temp = {y_i + str(int(x_i) + j): n[0]}
                        dicti.update(temp)
            if "P" in n:
                if "right" in i:
                    for j in range(2):
                        temp = {alphabet[index + j] + x_i: n[0]}
                        dicti.update(temp)
                if "down" in i:
                    for j in range(2):
                        temp = {y_i + str(int(x_i) + j): n[0]}
                        dicti.update(temp)


#function to execute the specified shooting processes
def shooter(moves, actual, hidden, dict_list):
    try:
        row = moves[i - 1].split(",")[0]
        column = moves[i - 1].split(",")[1]
        assert int(row) < 11
        assert column < "K"
        move = column + row
        if actual[int(row) - 1][alphabet.index(column)] == "-":
            actual[int(row) - 1][alphabet.index(column)] = "O"
            hidden[int(row) - 1][alphabet.index(column)] = "O"
        else:
            actual[int(row) - 1][alphabet.index(column)] = "X"
            hidden[int(row) - 1][alphabet.index(column)] = "X"
        for d in dict_list:
            if move in d:
                d.pop(move)
    except ValueError:
        f.write(f"ValueError: Your move {moves_1[i - 1]} does not fit the supported move pattern. "
                f"Supported last move is: 10,J\n\n")
    except AssertionError:
        f.write("AssertionError: Invalid Operation.\n\n")
    except IndexError:
        f.write(f"IndexError: Your move '{moves_1[i - 1]}' does not fit the supported move pattern. Supported move pattern is: 'number,letter' while number is less than 11 and positive, and letter comes before than 'K' in alphabet.\n\n")


#function to print and write the current ship status
def ship_status_printer_and_writer():
    global patrol1
    global patrol2
    print("Carrier\t\t-\t\t\t\tCarrier\t\t" if len(carrier1) != 0 else "Carrier\t\tX\t\t\t\tCarrier\t\t", end="")
    f.write("Carrier\t\t-\t\t\t\tCarrier\t\t" if len(carrier1) != 0 else "Carrier\t\tX\t\t\t\tCarrier\t\t")
    print("-" if len(carrier2) != 0 else "X")
    f.write("-" if len(carrier2) != 0 else "X")
    if len(battleship1_1) != 0 and len(battleship1_2) != 0:
        f.write("\nBattleship\t- -")
        print("Battleship\t- -", end="")
    if len(battleship1_1) == 0 and len(battleship1_2) != 0:
        f.write("\nBattleship\tX -")
        print("Battleship\tX -", end="")
    if len(battleship1_1) != 0 and len(battleship1_2) == 0:
        f.write("\nBattleship\tX -")
        print("Battleship\tX -", end="")
    if len(battleship1_1) == 0 and len(battleship1_2) == 0:
        f.write("\nBattleship\tX X")
        print("Battleship\tX X", end="")
    if len(battleship2_1) != 0 and len(battleship2_2) != 0:
        f.write("\t\t\t\tBattleship\t- -")
        print("\t\t\t\tBattleship\t- -")
    if len(battleship2_1) == 0 and len(battleship2_2) != 0:
        f.write("\t\t\t\tBattleship\tX -")
        print("\t\t\t\tBattleship\tX -")
    if len(battleship2_1) != 0 and len(battleship2_2) == 0:
        f.write("\t\t\t\tBattleship\tX -")
        print("\t\t\t\tBattleship\tX -")
    if len(battleship2_1) == 0 and len(battleship2_2) == 0:
        f.write("\t\t\t\tBattleship\tX X")
        print("\t\t\t\tBattleship\tX X")
    print("Destroyer\t-\t\t\t\tDestroyer\t" if len(destroyer1) != 0 else "Destroyer\tX\t\t\t\tDestroyer\t", end="")
    f.write("\nDestroyer\t-\t\t\t\tDestroyer\t" if len(destroyer1) != 0 else "\nDestroyer\tX\t\t\t\tDestroyer\t")
    print("-" if len(destroyer2) != 0 else "X")
    f.write("-" if len(destroyer2) != 0 else "X")
    print("Submarine\t-\t\t\t\tSubmarine\t" if len(submarine1) != 0 else "Submarine\tX\t\t\t\tSubmarine\t", end="")
    f.write("\nSubmarine\t-\t\t\t\tSubmarine\t" if len(submarine1) != 0 else "\nSubmarine\tX\t\t\t\tSubmarine\t")
    print("-" if len(submarine2) != 0 else "X")
    f.write("-" if len(submarine2) != 0 else "X")
    if patrol1 > 6:
        f.write("\nPatrol Boat\t- - - -")
        print("Patrol Boat\t- - - -", end="")
    if 6 >= patrol1 > 4:
        f.write("\nPatrol Boat\tX - - -")
        print("Patrol Boat\tX - - -", end="")
    if 4 >= patrol1 > 2:
        f.write("\nPatrol Boat\tX X - -")
        print("Patrol Boat\tX X - -", end="")
    if 2 >= patrol1 > 0:
        f.write("\nPatrol Boat\tX X X -")
        print("Patrol Boat\tX X X -", end="")
    if patrol1 == 0:
        f.write("\nPatrol Boat\tX X X X")
        print("Patrol Boat\tX X X X", end="")
    if patrol2 > 6:
        f.write("\t\t\tPatrol Boat\t- - - -")
        print("\t\t\tPatrol Boat\t- - - -")
    if 6 >= patrol2 > 4:
        f.write("\t\t\tPatrol Boat\tX - - -")
        print("\t\t\tPatrol Boat\tX - - -")
    if 4 >= patrol2 > 2:
        f.write("\t\t\tPatrol Boat\tX X - -")
        print("\t\t\tPatrol Boat\tX X - -")
    if 2 >= patrol2 > 0:
        f.write("\t\t\tPatrol Boat\tX X X -")
        print("\t\t\tPatrol Boat\tX X X -")
    if patrol2 == 0:
        f.write("\t\t\tPatrol Boat\tX X X X")
        print("\t\t\tPatrol Boat\tX X X X")


try:
    with open(sys.argv[1], "r") as f:
        data_1 = f.read().splitlines()
    with open(sys.argv[2], "r") as f:
        data_2 = f.read().splitlines()
    with open(sys.argv[3], "r") as f:
        moves_1 = f.read().split(";")
    moves_1.remove("")
    with open(sys.argv[4], "r") as f:
        moves_2 = f.read().split(";")
    moves_2.remove("")
    with open("OptionalPlayer1.txt", "r") as f:
        optional_data1 = f.read().splitlines()
    with open("OptionalPlayer2.txt", "r") as f:
        optional_data2 = f.read().splitlines()
    f = open("Battleship.out", "w")

    hidden_1 = [["-" for j in range(10)] for i in range(10)]                        #the list which does not
    hidden_2 = [["-" for j in range(10)] for i in range(10)]                        # show the ship information

    #Ships for the first player
    carrier1 = {}
    destroyer1 = {}
    submarine1 = {}
    battleship1_1 = {}
    battleship1_2 = {}
    patrol1_1 = {}
    patrol1_2 = {}
    patrol1_3 = {}
    patrol1_4 = {}

    #Ships for the second player
    carrier2 = {}
    destroyer2 = {}
    submarine2 = {}
    battleship2_1 = {}
    battleship2_2 = {}
    patrol2_1 = {}
    patrol2_2 = {}
    patrol2_3 = {}
    patrol2_4 = {}

    #Dictionary lists for iterating
    dict_list1 = [carrier1, destroyer1, submarine1, battleship1_1, battleship1_2, patrol1_1, patrol1_2, patrol1_3, patrol1_4]
    dict_list2 = [carrier2, destroyer2, submarine2, battleship2_1, battleship2_2, patrol2_1, patrol2_2, patrol2_3, patrol2_4]

    actual_1 = txt_organizer(data_1)                                                #creating the actual lists
    actual_2 = txt_organizer(data_2)                                                # which contain ship data
    ship_recorder1(actual_1, carrier1, submarine1, destroyer1)
    ship_recorder1(actual_2, carrier2, submarine2, destroyer2)
    ship_recorder2(optional_data1, "B1", battleship1_1)
    ship_recorder2(optional_data1, "B2", battleship1_2)
    ship_recorder2(optional_data1, "P1", patrol1_1)
    ship_recorder2(optional_data1, "P2", patrol1_2)
    ship_recorder2(optional_data1, "P3", patrol1_3)
    ship_recorder2(optional_data1, "P4", patrol1_4)
    ship_recorder2(optional_data2, "B1", battleship2_1)
    ship_recorder2(optional_data2, "B2", battleship2_2)
    ship_recorder2(optional_data2, "P1", patrol2_1)
    ship_recorder2(optional_data2, "P2", patrol2_2)
    ship_recorder2(optional_data2, "P3", patrol2_3)
    ship_recorder2(optional_data2, "P4", patrol2_4)

    #Driver Code which does the main printing and writing operations
    if len(moves_1) == len(moves_2):
        print("Battle of Ships Game\n")
        f.write("Battle of Ships Game\n\n")
        for i in range(1, len(moves_1) + 1):
            patrol1 = len(patrol1_2) + len(patrol1_2) + len(patrol1_3) + len(patrol1_4)
            patrol2 = len(patrol2_2) + len(patrol2_2) + len(patrol2_3) + len(patrol2_4)
            print("Player1's Move\n")
            f.write("Player1's Move\n\n")
            print("Round :", str(i) + "\t\t\t\t\tGrid Size: 10x10\n")
            f.write("Round :" + " " + str(i) + "\t\t\t\t\tGrid Size: 10x10\n\n")
            print("Player1's Hidden Board\t\tPlayer2's Hidden Board")
            f.write("Player1's Hidden Board\t\tPlayer2's Hidden Board\n")
            printer_and_writer(hidden_1, hidden_2)
            print("")  #newline
            f.write("\n")
            ship_status_printer_and_writer()
            print("")
            f.write("\n\n")
            print("Enter your move:", moves_1[i - 1] + "\n")
            f.write("Enter your move:" + " " + moves_1[i - 1] + "\n\n")
            shooter(moves_1, actual_2, hidden_2, dict_list2)
            print("Player2's Move\n")
            f.write("Player2's Move\n\n")
            print("Round :", str(i) + "\t\t\t\t\tGrid Size: 10x10\n")
            f.write("Round :" + " " + str(i) + "\t\t\t\t\tGrid Size: 10x10\n\n")
            print("Player1's Hidden Board\t\tPlayer2's Hidden Board")
            f.write("Player1's Hidden Board\t\tPlayer2's Hidden Board\n")
            printer_and_writer(hidden_1, hidden_2)
            print("")  #newline
            f.write("\n")
            ship_status_printer_and_writer()
            print("")
            f.write("\n\n")
            print("Enter your move:", moves_2[i - 1] + "\n\n")
            f.write("Enter your move:" + " " + moves_2[i - 1] + "\n\n")
            shooter(moves_2, actual_1, hidden_1, dict_list1)

        length1 = len(carrier1) + len(battleship1_1) + len(battleship1_2) + len(destroyer1) + len(submarine1) + len(patrol1_1) + len(patrol1_2) + len(patrol1_3) + len(patrol1_4)
        length2 = len(carrier2) + len(battleship2_1) + len(battleship2_2) + len(destroyer2) + len(submarine2) + len(patrol2_1) + len(patrol2_2) + len(patrol2_3) + len(patrol2_4)

        if length1 > length2:
            print("Player1 Wins!\n")
            f.write("Player1 Wins!\n\n")
        if length2 > length1:
            print("Player2 Wins!\n")
            f.write("Player2 Wins!\n\n")
        if length2 == length1:
            print("It is a Draw!\n")
            f.write("It is a Draw!\n\n")
        print("Final Information\n")
        f.write("Final Information\n\n")
        print("Player1's Board\t\t\t\tPlayer2's Board")
        f.write("Player1's Board\t\t\t\tPlayer2's Board\n")
        printer_and_writer(actual_1, actual_2)
        print("")
        f.write("\n")
        ship_status_printer_and_writer()
    else:
        f.write("kaBOOM: run for your life!")

except FileNotFoundError:
    f = open("Battleship.out", "w")
    checklist = []
    if sys.argv[1] != "Player1.txt":
        checklist.append(sys.argv[1])
    if sys.argv[2] != "Player2.txt":
        checklist.append(sys.argv[2])
    if sys.argv[3] != "Player1.in":
        checklist.append(sys.argv[3])
    if sys.argv[4] != "Player2.in":
        checklist.append(sys.argv[4])
    f.write("IOError: input file(s) " + ", ".join(i for i in checklist) + " is/are not reachable.")
except IndexError:
    f = open("Battleship.out", "w")
    f.write("kaBOOM: run for your life!")
