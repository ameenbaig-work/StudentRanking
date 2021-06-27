#Defining the actual Progress Score
class ProgressScore:

    #Initializing method for class ProgressScore
    #This method defines the properties and populates them
    def __init__(self, actual_maths_marks, actual_english_marks, actual_physics_marks, mock_maths_marks, mock_english_marks, mock_physics_marks):
        self.max_marks = 100
        self.actual_maths_marks = actual_maths_marks
        self.actual_english_marks = actual_english_marks
        self.actual_physics_marks = actual_physics_marks
        self.mock_maths_marks = mock_maths_marks
        self.mock_english_marks = mock_english_marks
        self.mock_physics_marks = mock_physics_marks

    #Calculates the average progress score for the 3 subjects
    def calculate_avg_progress_score(self):
        m_progress_marks = (self.actual_maths_marks - self.mock_maths_marks)
        e_progress_marks = (self.actual_english_marks - self.mock_english_marks)
        p_progress_marks = (self.actual_physics_marks - self.mock_physics_marks)
        avg_progress_score = (m_progress_marks + e_progress_marks + p_progress_marks)/ (10*3)
        avg_progress_score = round(avg_progress_score, 2)
        return avg_progress_score