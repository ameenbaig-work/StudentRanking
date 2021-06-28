import unittest
from ProgressScore import *

# TestCase for ProgressScore
# Child class of Parent Class: unittest.TestCase
class TestProgressScore(unittest.TestCase):

    # Method for checking if the Average ProgressScore is correct to 2 decimal places
    # Raises an error if the calculated value is incorrect
    def test_calculate_avg_progress_score(self):
        # Instantiation of ProgressScore
        student_marks = ProgressScore(99, 88, 92, 96, 79, 54)
        self.assertAlmostEqual(student_marks.calculate_avg_progress_score(), -1.07, 2, "Average Score Not Calculated Correctly")

    # Method for checking if any of the properties exceed 100 marks
    def test_check_input_size(self):
        # Instantiation of ProgressScore
        student_marks = ProgressScore(99, 88, 92, 96, 79, 54)
        self.assertRaises(ValueError, student_marks.validate_input_size, 990, 88, 92, 96, 79, 54)

    # Method for checking if any of the properties are of datatype "string"
    def test_check_input_datatype(self):
        self.assertRaises(ValueError, ProgressScore.validate_input_datatype, self, "99", 88, 92, 96, 79, 54)

if __name__ == '__main__':
    unittest.main()
