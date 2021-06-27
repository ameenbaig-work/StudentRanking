#Defining the actual Average Score
class AverageScore:

    #Initializing method for class AverageScore
    #This method difines the properties and populates them
    def __init__(self, maths_marks, english_marks, physics_marks):
        self.max_marks = 100
        self.maths_marks = maths_marks
        self.english_marks = english_marks
        self.physics_marks = physics_marks

    def validate_input_values(self, maths_marks, english_marks, physics_marks):
        if (maths_marks < 0) or (english_marks < 0) or (physics_marks < 0):
            print("before raising error")
            raise ValueError("Only positive values are allowed")

    def validate_input_size(self, maths_marks, english_marks, physics_marks):
        if (maths_marks > self.max_marks) or (english_marks > self.max_marks) or (physics_marks > self.max_marks):
            raise ValueError("Scores cannot exceed 100 marks")

    def validate_input_datatype(self, maths_marks, english_marks, physics_marks):
        if isinstance(maths_marks,str) or isinstance(english_marks,str) or isinstance(physics_marks,str):
            raise ValueError("Input cannot be a string")

    #Calculates the average score for the 3 subjects
    def calculate_avg_score(self):
        avg_score = (self.maths_marks + self.english_marks + self.physics_marks)/3
        return avg_score

#s1 = AverageScore(50,60,70)
#s1.validate_input_size(120, 60, 70)

