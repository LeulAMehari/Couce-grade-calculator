#Author:            Leul Adane
#Date:              November 30, 2021
#Purpose:           reads the student information from a tab separated values (tsv) file, then the
#                   program then creates a text file that records the course grades of the students.

first_names = []
last_names = []
mid1 = []
mid2 = []
final = []
num_of_tests = 3
grade = ''

filename = input("Enter the file name: ")

with open(filename, 'r') as file:                   
    lines = file.readlines()                #Read the file text into a string

for line in lines:                          # Iterate over each line

    student_info = line.split()                    #Splits each line into list
    
    first_names.append((student_info[0]))         #Adds the first element of the list to the list first names   
    last_names.append((student_info[1]))
    mid1.append(float(student_info[2]))            #Converts the third item of the list to float, then adds it to the list mid1
    mid2.append(float(student_info[3]))
    final.append(float(student_info[4]))

with open('ReportGrade.txt', '+w') as output:               #Open fie for writing and appending, automatically close the file when complete.
    for i in range(len(first_names)):
        average = (mid1[i]+mid2[i]+final[i])/num_of_tests       

        if average >= 90:                               #Assigns a grade to the average, if it is above 90 it sets to 'A'
            grade = 'A'
        elif average >= 80:
            grade = 'B'
        elif average >= 70:
            grade = 'C'
        elif average >= 60:
            grade = 'D'
        else:
            grade = 'F'

        print('{}\t{}\t{}\t{}\t{}\t{}\t'.format( 
            last_names[i],first_names[i],mid1[i],
            mid2[i],final[i],grade),
            file=output)
        
    #The statement 'file = output' grants access to our program, and when it runs, it saves the file directly to our computer (tab separated) rather than displaying it as the output.
        
    ave_mid1 = sum(mid1)/len(mid1)                  
    ave_mid2 = sum(mid2)/len(mid2)
    ave_finals = sum(final)/len(final)
            #Calulates the average of each exam score
    
    print('\nAverages: midterm1 {:.2f}, midterm2 {:.2f}, final {:.2f}'.format(ave_mid1, ave_mid2, ave_finals),file=output)          #Outputs the average of each exam score at the end of our text file

    

            
