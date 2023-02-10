import os
import sys
current_dir_path = os.getcwd()
reading_file_name = sys.argv[1]
reading_file_path = os.path.join(current_dir_path, reading_file_name)
writing_file_name = sys.argv[2]
writing_file_path = os.path.join(current_dir_path, writing_file_name)


def write(x):
    with open(sys.argv[2], "a") as w:
        w.write(x)


list1 = []
n = 1
with open(sys.argv[1], "r") as r:
    data = r.readlines()
for i in range(len(data)):
    list1.append(data[i][0:4])
list1.sort()
list1 = list(dict.fromkeys(list1))
data.sort()
for i in list1:
    output = "Message\t" + str(n) + "\n"
    write(output)
    n += 1
    for j in data:
        if i in j:
            if "\n" not in j:
                j = j + "\n"
            write(j)
