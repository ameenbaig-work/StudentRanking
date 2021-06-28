#Defining the actual Average Score
class AverageScore:

    #Initializing method for class AverageScore
    #This method difines the properties and populates them
    def __init__(self, maths_marks, english_marks, science_marks):
        self.max_marks = 100
        self.validate_input_values(maths_marks, english_marks, science_marks)
        self.maths_marks = maths_marks
        self.english_marks = english_marks
        self.science_marks = science_marks

    def validate_input_values(self, maths_marks, english_marks, science_marks):
        self.validate_negative_input(maths_marks, english_marks, science_marks)
        self.validate_input_size(maths_marks, english_marks, science_marks)
        self.validate_input_datatype(maths_marks, english_marks, science_marks)

    def validate_negative_input(self, maths_marks, english_marks, science_marks):
        if (maths_marks < 0) or (english_marks < 0) or (science_marks < 0):
            print("before raising error")
            raise ValueError("Only positive values are allowed")

    def validate_input_size(self, maths_marks, english_marks, science_marks):
        if (maths_marks > self.max_marks) or (english_marks > self.max_marks) or (science_marks > self.max_marks):
            raise ValueError("Scores cannot exceed 100 marks")

    def validate_input_datatype(self, maths_marks, english_marks, science_marks):
        if isinstance(maths_marks,str) or isinstance(english_marks,str) or isinstance(science_marks,str):
            raise ValueError("Input cannot be a string")

    #Calculates the average score for the 3 subjects
    def calculate_avg_score(self):
        avg_score = (self.maths_marks + self.english_marks + self.science_marks)/3
        avg_score = round(avg_score,2)
        return avg_score

