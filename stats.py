#Input function read the a line from the input 
#Then function Open is excecuted to open a specific filename 
fileName = input("Enter: ")
f = open(fileName, 'r')


list = []
for line in f:
    words = line.split()
    for word in words:
        #append method is used to add a single item to existing list
        list.append(float(word)) 

def median(list): #This function will calculate the median
    if len(list) == 0: #Checking for empty list
        return 0
    list.sort() #Arranging list of elements
    midNum = int(len(list) / 2)   #Determine middle element
    if len(list) % 2 == 1:
        #return median if the elements in list is odd result
        return list[midNum]      
    else:
       #return median if the elements in list is even result
        return (list[midNum] + list[midNum - 1]) / 2

def mode(list): #This function will calculate the mode
    if len(list) == 0: #Checking for empty list
        return 0

    numDictionary = {} #Creating dictionary
    for digit in list:
        number = numDictionary.get(digit, None)
        if number == None:
            numDictionary[digit] = 1
        else: 
            numDictionary[digit] = number + 1
    #Getting the maximum value from list
    maxValue = max(numDictionary.values())
    modeList = []
    for key in numDictionary:
        #Determing elements which has the maximum value
        if numDictionary[key] == maxValue:
            return key     
    
def mean(list): #This function will calculate the mean
    if len(list) == 0: #Checking for empty list 
        return 0
    #function sum computes the value inside the list 
    #then divide it with the number of elements stored in the list
    return sum(list)/len(list) 

def main():
    #Prints the data stored in the opened file and output it in an array list.
    print (list)
    
    #calls out the function median 
    print ("Median :", median(list))
    #calls out the function mode
    print ("Mode: ", mode(list))
    #calls out the function mean 
    print ("Mean: ", mean(list))
    
main()