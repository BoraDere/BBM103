n = int(input("Enter a number: "))
oddTotal = 0
evenTotal = 0
for oddNumber in range(1,n+1):
    if oddNumber%2 !=0:
        oddTotal = oddTotal + oddNumber
for evenNumber in range(1,n+1):
    if evenNumber%2 ==0:
        evenTotal = evenTotal + evenNumber
    evenCount = (n/2)
    evenAverage = evenTotal/evenCount
print("Sum of odds: " + str(oddTotal))
print("Average of evens: " + str(round(evenAverage)))