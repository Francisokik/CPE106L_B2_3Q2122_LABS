"""
File: student.py
Resources to manage a student's name and test scores.
"""
class Student(object):
    """Represents a student."""
    self:str
    self2:str

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def __init__(self2, name, number):
        """All scores are initially 0."""
        self2.name = name
        self2.scores = []
        for count in range(number):
            self2.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self._scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return (self.scores)

    def equalityTest(self, self2):
        """Returns comparison of two students' names using Equal To (==) operator."""
        return self.name == self2.name 

    def lessTest(self, self2):
        """Returns comparison of two students' names using Less Than (<) operator."""
        return self.name < self2.name 

    def greaterTest(self, self2):
        """Returns comparison of two students' names using Greater Than or Equal To (>=) operator."""
        return self.name >= self2.name 
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))

def main():
    """A simple test."""
    student1 = Student("Ken", 5)
    student2 = Student("Allen", 5)
    
    print("STUDENT 1:")
    print(student1)
    print("\nSTUDENT 2:")
    print(student2)
        
    print("\nStudent 1 is equal to Student 2 Test: ")
    print(student1.equalityTest(student2))
    print("\nStudent 1 is less than Student 2 Test: ")
    print(student1.lessTest(student2))
    print("\nStudent 1 is greater than or equal to Student 2 Test: ")
    print(student1.greaterTest(student2))

if __name__ == "__main__":
    main()


