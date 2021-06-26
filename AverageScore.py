#Defining the actual Average Score
class AverageScore:

    #Initializing method for class AverageScore
    #This method difines the properties and populates them
    def __init__(self, maths_marks, english_marks, physics_marks):
        self.max_marks= 100
        self.maths_marks = maths_marks
        self.english_marks = english_marks
        self.physics_marks = physics_marks

    #Calculates the average score for the 3 subjects
    def calculate_avg_score(self):
        avg_score = (self.maths_marks + self.english_marks + self.physics_marks)/3
        return avg_score