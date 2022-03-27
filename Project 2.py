import random

class Student(object):

    def __init__(self, name, number):
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(100)

    def getName(self):
        return self.name

    def setScore(self, i, score):
        self.scores[i - 1] = score

    def getScore(self, i):
        return self.scores[i - 1]

    def getAverage(self):
        return sum(self.scores) / len(self._scores)

    def getHighScore(self):
        return max(self.scores)

    def __str__(self):
        return "Name: " + self.name + "\nScores: " + \
               " ".join(map(str, self.scores))

    def __lt__(self, self2):
        return self.name < self2.name

    def __ge__(self, self2):
        return self.name >= self2.name

    def __eq__(self, self2):
        if self is self2:
            return True
        elif type(self) != type(self2):
            return False
        else:
            return self.name == self2.name

def main():
    # Create the list and put 7 students into it
    lyst = []
    for count in reversed(range(1)):
        s1 = Student("Kyle ", 10)
        s2 = Student("John ", 10)
        s3 = Student("Mina ", 10)
        s4 = Student("Allen ", 10)
        s5 = Student("Harry ", 10)
        s6 = Student("Sharon ", 10)
        s7 = Student("JJ ", 10)

        lyst.append(s1)
        lyst.append(s2)
        lyst.append(s3)
        lyst.append(s4)
        lyst.append(s5)
        lyst.append(s6)
        lyst.append(s7)
       
    # Complete the definition of the main function
    print("Sorted list of students:")
    # Shuffle the list using the import statement random
    random.shuffle(lyst)
   
    # Sort the list using the sort() method.
    lyst.sort()

    # Display the student list data.
    for obj in lyst:
        print(obj.__str__())

if __name__ == "__main__":
    main()