import os
current_dir_path = os.getcwd()
reading_file_name = "doctors_aid_inputs.txt"
reading_file_path = os.path.join(current_dir_path, reading_file_name)
writing_file_name = "doctors_aid_outputs.txt"
writing_file_path = os.path.join(current_dir_path, writing_file_name)
patient_data_list = []


#defining a reading function to open the input file
def read():
    with open(reading_file_path, "r") as f:
        return f.readlines()


#defining a writing function to write the output
def write(output):
    with open(writing_file_path, "a") as w:
        w.write(output)


#defining a create function to enter the patient data to the list
def create():
    if patient_data not in patient_data_list:                                                #checking it patient is already recorded
        patient_data_list.append(patient_data)                                               #recording the patient if not recorded before
        output = "Patient " + patient_name + " is recorded.\n"
        write(output)
    else:                                                                                    #stating that they are already recorded
        output = "Patient " + patient_name + " cannot be recorded due to duplication.\n"
        write(output)


#defining a probability function to calculate the actual probability of patient having the disease
def probability():
    for i in patient_data_list:                                                              #searching every element
        if line in i:                                                                        # until finding the right one
            patient_name = i[0]
            disease_name = i[2]
            diagnosis_accuracy = float(i[1])
            domain = int(i[3][3:])                                                           #slicing the fraction
            positive = int(i[3][0:2])                                                        # to use in calculations
            negative = domain - positive
            TP = diagnosis_accuracy * positive
            FP = round(positive - TP, 2)
            TN = diagnosis_accuracy * negative
            FN = round(negative - TN, 2)
            probability = round(TP / (TP + FP + FN) * 100, 2)                                #calculating the probability
            if int(probability) == float(probability):
                probability = int(probability)
            else:
                probability = float(probability)
            output = "Patient " + patient_name + " has a probability of " + str(probability) + "% of having " + disease_name.lower() + ".\n"  #lowercasing the disease name as required
            write(output)
            break
    else:                                                                                    #if specified patient was not recorded before
        output = "Probability for " + line + " cannot be calculated due to absence.\n"
        write(output)


#defining a remove function to remove the patient data from the list
def remove():
    for i in patient_data_list:                                                              #searching every element
        if patient_name in i:                                                                # until finding the right one
            patient_data_list.remove(i)                                                      #removing the patient if exists
            output = "Patient " + patient_name + " is removed.\n"
            write(output)
            break                                                                            #breaking the loop since it is a for-else structure
    else:                                                                                    #stating that specified patient does not exist in the list
        output = "Patient " + patient_name + " cannot be removed due to absence.\n"
        write(output)


#defining a recommendation function to decide if patient should have the treatment
def recommendation():
    for i in patient_data_list:                                                              #searching every element
        if patient_name in i:                                                                # until finding the right one
            diagnosis_accuracy = float(i[1])                                                 #doing the probability calculation again and not returning a value
            domain = int(i[3][3:])                                                           # from the probability function may seem unnecessary but I specifically did that.
            positive = int(i[3][0:2])                                                        #I want the calculation to be seen clearly where it is used, I think it is important to
            negative = domain - positive                                                     # be able to see that at the first sight and not needing to check the function above.
            TP = diagnosis_accuracy * positive
            FP = round(positive - TP, 2)
            TN = diagnosis_accuracy * negative
            FN = round(negative - TN, 2)
            probability = round(TP / (TP + FP + FN) * 100, 2)
            treatment_risk = round(float(i[5].replace("\n", "")) * 100, 2)                   #defining the treatment_risk to use it in comparison
            if treatment_risk > probability:
                output = "System suggests " + patient_name + " NOT to have the treatment.\n"
                write(output)
            else:  # since there is no possibility of treatment_risk and probability being equal to each other
                output = "System suggests " + patient_name + " to have the treatment.\n"
                write(output)
            break                                                                            #breaking the loop since it is a for-else structure
    else:
        output = "Recommendation for " + patient_name + " cannot be calculated due to absence.\n"
        write(output)


#defining a list function to list the current patient data
def list():
    output = "Patient\tDiagnosis\tDisease\t\t\tDisease\t\tTreatment\t\tTreatment\nName\tAccuracy\tName\t\t\tIncidence\tName\t\t\tRisk\n" \
             "-------------------------------------------------------------------------\n"   #assigning the first output, which should be printed even though there is no patient record
    write(output)
    for i in patient_data_list:
        if len(i[0]) == 2:
            name = i[0] + "\t\t"
        else:
            name = i[0] + "\t"
        if len(i[2]) == 11:
            disease = i[2] + "\t\t"
        else:
            disease = i[2] + "\t"
        if len(i[4]) == 7:
            treatment = i[4] + "\t\t\t"
        elif len(i[4]) == 16:
            treatment = i[4]
        else:
            treatment = i[4] + "\t"
        if len(str(i[1])) == 4:
            accuracy = str(float(i[1])*100) + "0%\t\t"
        if len(str(i[1])) == 5:
            accuracy = str(float(i[1]) * 100) + "0%\t\t"
        if len(str(i[1])) == 6:
            accuracy = str(float(i[1]) * 100) + "%\t\t"
        output = name + accuracy + disease + i[3] + "\t" + treatment + str(int(float(i[5])*100)) + "%\n"
        write(output)


#Driver Code
lines = read()                                                                              #collecting all the data read with the read function
for line in lines:                                                                          #activating the correct function with respect to first word of the line
    if line.startswith("create "):
        patient_data = line[7:].replace("\n", "").split(", ")                               #doing necessary slicing, splitting and replacing operations to obtain the required format
        patient_name = patient_data[0]
        create()
    if line.startswith("probability "):
        line = line[12:].replace("\n", "")                                                  #doing necessary slicing and replacing operations to obtain the required format
        probability()
    if line.startswith("recommendation "):
        patient_name = line[15:].replace("\n", "")                                          #doing necessary slicing and replacing operations to obtain the required format
        recommendation()
    if line.startswith("list"):
        list()
    if line.startswith("remove "):
        patient_name = line[7:].replace("\n", "")                                           #doing necessary slicing and replacing operations to obtain the required format
        remove()
