import sys                                # Importing the required library.

# Problem1: Basketball Score Calculator
try:                                      # Trying to run this block of code first.
    i = int(sys.argv[1])*2                # 2 pointers.
    ii = int(sys.argv[2])*3               # 3 pointers.
    iii = int(sys.argv[3])                # Free throws.
    totalPoint = i + ii + iii             # Calculating the summation of 3 different score types.
    print(totalPoint)                     # Displaying the total points.

# Problem2: Body Mass Index Calculator
except:                                   # Deciding to run this block of code if the attempt to run the first block fails.
    def healthStatus(height, mass):       # Defining healthStatus function.
        BMI = (mass/(height**2))          # Calculating BMI.
        if BMI < 18.5:                    # Checking BMI value for certain limit values.
            return("underweight")         # If BMI is less than 18.5, person is underweight.
        elif BMI >= 18.5 and BMI < 24.9:  # Checking BMI value for certain limit values.
            return("healthy")             # If BMI is more than or equal to 18.5 and less than 24.9, person is healthy.
        elif BMI >= 24.9 and BMI < 30:    # Checking BMI value for certain limit values.
            return("overweight")          # If BMI is more than or equal to 24.9 and less than 30, person is healthy.
        else:                             # Checking BMI value whether it suits the limitations above.
            return("obese")               # If BMI does not fit to the limitations above, person is obese.
