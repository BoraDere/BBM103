import sys
import os


def round(x):  # since built-in round function does not do the job
    integer, decimal = str(x).split(".")
    if int(decimal[0]) >= 5:  # so you can give floats such as 4.4999999999999 and still get the correct result
        return int(integer) + 1
    else:
        return int(integer)


try:
    operand_list = []
    comparison_data_list = []
    result_list = []
    comparison_list = []
    n = 0
    current_dir_path = os.getcwd()
    reading_file_name_1 = sys.argv[1]
    reading_file_path_1 = os.path.join(current_dir_path, reading_file_name_1)
    reading_file_name_2 = sys.argv[2]
    reading_file_path_2 = os.path.join(current_dir_path, reading_file_name_2)
    with open(reading_file_path_1, "r") as f:
        operand_data = f.readlines()
    with open(reading_file_path_2, "r") as f:
        comparison_data = f.readlines()
    for i in operand_data:
        operand_list.append(i.replace("\n", "").split(" "))
    for i in comparison_data:
        comparison_data_list.append(i.replace("\n", ""))
    for element in operand_list:
        print("-----------")
        try:
            div = element[0]
            nondiv = element[1]
            frOm = element[2]
            to = element[3]
            try:
                for j in range(round(float(frOm)), round(float(to)) + 1):
                    if j % round(float(div)) == 0 and j % round(float(nondiv)) != 0:
                        result_list.append(j)
                for i in comparison_data_list[n].split(" "):
                    comparison_list.append(int(i))
                print("My results:\t\t" + " ".join([str(i) for i in result_list]))
                print("Results to compare:\t" + " ".join([str(i) for i in comparison_list]))
                if result_list == comparison_list:
                    print("Goool!!!")
                else:
                    print("Assertion Error: results don’t match.")
                result_list = []
                comparison_list = []
                n += 1
            except ZeroDivisionError:
                print("ZeroDivisionError: You can’t divide by 0.")
                print("Given input:", operand_data[n], end="")
                n += 1
            except ValueError:
                print("ValueError: only numeric input is accepted.")
                print("Given input:", operand_data[n], end="")
                n += 1
        except IndexError:
            print("IndexError: number of operands less than expected.")
            print("Given input:", operand_data[n], end="")
            n += 1
except IndexError:
    print("IndexError: number of input files less than expected.")
except FileNotFoundError:
    if sys.argv[1] == "operands.txt" and sys.argv[2] != "comparison_data.txt":
        print("IOError: cannot open", sys.argv[2], end="")
    if sys.argv[1] != "operands.txt" and sys.argv[2] == "comparison_data.txt":
        print("IOError: cannot open", sys.argv[1], end="")
    if sys.argv[1] != "operands.txt" and sys.argv[2] != "comparison_data.txt":
        print("IOError: cannot open", sys.argv[1], "and", sys.argv[2], end="")
finally:
    print("˜ Game Over ˜")