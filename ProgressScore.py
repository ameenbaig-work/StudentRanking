# Defining the Progress Score
class ProgressScore:

    # Initializing method for class ProgressScore
    # This method defines the properties and populates them
    def __init__(self, mock_maths_marks, actual_maths_marks, mock_english_marks, actual_english_marks, mock_science_marks, actual_science_marks):
        self.max_marks = 100
        self.validate_input_values(mock_maths_marks, actual_maths_marks, mock_english_marks, actual_english_marks, mock_science_marks, actual_science_marks)
        self.actual_maths_marks = actual_maths_marks
        self.actual_english_marks = actual_english_marks
        self.actual_science_marks = actual_science_marks
        self.mock_maths_marks = mock_maths_marks
        self.mock_english_marks = mock_english_marks
        self.mock_science_marks = mock_science_marks

    # Method for calling the two testing methods below.
    def validate_input_values(self, mock_maths_marks, actual_maths_marks, mock_english_marks, actual_english_marks, mock_science_marks, actual_science_marks):
        self.validate_input_size(mock_maths_marks, actual_maths_marks, mock_english_marks, actual_english_marks, mock_science_marks, actual_science_marks)
        self.validate_input_datatype(mock_maths_marks, actual_maths_marks, mock_english_marks, actual_english_marks, mock_science_marks, actual_science_marks)

    # Raises an error if any of the properties are greater than 100
    def validate_input_size(self, mock_maths_marks, actual_maths_marks, mock_english_marks, actual_english_marks, mock_science_marks, actual_science_marks):
        if (mock_maths_marks > self.max_marks) or (actual_maths_marks > self.max_marks) or (mock_english_marks > self.max_marks) or \
                (actual_english_marks > self.max_marks) or (mock_science_marks > self.max_marks) or (actual_science_marks > self.max_marks):
            raise ValueError("Scores cannot exceed 100 marks")

    # Raises an error if any of the properties are a string
    def validate_input_datatype(self, mock_maths_marks, actual_maths_marks, mock_english_marks, actual_english_marks, mock_science_marks, actual_science_marks):
        if isinstance(mock_maths_marks,str) or isinstance(actual_maths_marks,str) or isinstance(mock_english_marks,str) \
                or isinstance(actual_english_marks,str) or isinstance(mock_science_marks,str) or isinstance(actual_science_marks,str):
            raise ValueError("Input cannot be a string")

    # Calculates the average progress score for the 3 subjects
    def calculate_avg_progress_score(self):
        m_progress_marks = (self.actual_maths_marks - self.mock_maths_marks)
        e_progress_marks = (self.actual_english_marks - self.mock_english_marks)
        p_progress_marks = (self.actual_science_marks - self.mock_science_marks)
        avg_progress_score = (m_progress_marks + e_progress_marks + p_progress_marks)/ (10*3)
        avg_progress_score = round(avg_progress_score, 2)
        return avg_progress_score
