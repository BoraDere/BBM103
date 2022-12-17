import sys
set = sys.argv[1].split(",")
list = []
for i in set:
    if int(i) % 2 == 0:
        set.remove(i)
for n in range(len(set)):
    if n == 0:
        continue
    for i in reversed(set):
        try:
            if set.index(i) > 0 and (set.index(i) + 1) % int(set[n]) == 0:
                set.remove(i)
                for j in set:
                    list.append(int(j))
                print(list)
                list = []
        except:
            IndexError