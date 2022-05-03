filename = input("Enter file name: ") #asks for user to input the file name
file = open(filename, 'r') #opens the file with the same name as the input in filename variable
linecount = 0 #initializes line count

for line in file: #adds 1 to total line number, as it starts with 0 by default
    linecount = linecount + 1

print("Number of lines in the file: ", linecount)#displays number of lines

#while loop for the program to run as long as the user has not picked the option to quit
while True:
    linenum = 0
    num = int(input("Enter the line number to be displayed (enter 0 to quit): ")) #asks for user to input the desired line number to be displayed
    
    if num >=1 and num <= linecount: #if user selects between 1 to the total number of lines, then the respective line will be displayed.
        file = open(filename, 'r')
        for lines in file:
            linenum = linenum + 1 #adds 1 to each line, as it starts with 0 by default
            if linenum == num:
                print(lines) #displays selected line
    else:
        if num == 0: #quits the program if 0 is inputted
            print("Program closed.")
            break