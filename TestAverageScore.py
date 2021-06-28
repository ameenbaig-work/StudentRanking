import unittest
from AverageScore import *

# TestCase for AverageScore
# Child class of Parent Class: unittest.TestCase
class TestAverageScore(unittest.TestCase):

    # Method for checking if any of the properties are negative
    def test_validate_input_values(self):
        self.assertRaises(ValueError, AverageScore.validate_negative_input, self, -88, 96, 54)

    # Method for checking if the AverageScore is correct to 2 decimal places
    # Raises an error if the calculated value is incorrect
    def test_calculate_avg_score(self):
        # Instantiation of AverageScore
        student_marks = AverageScore(88, 96, 54)
        self.assertAlmostEqual(student_marks.calculate_avg_score(), 79.33, 2, "Average Score Not Calculated Correctly")

    # Method for checking if any of the properties exceed 100 marks
    def test_check_input_size(self):
        # Instantiation of AverageScore
        student_marks = AverageScore(88, 96, 54)
        self.assertRaises(ValueError, student_marks.validate_input_size, 880, 96, 54)

    # Method for checking if any of the properties are of datatype "string"
    def test_check_input_datatype(self):
        self.assertRaises(ValueError, AverageScore.validate_input_datatype, self, "88", 96, 54)

if __name__ == '__main__':
    unittest.main()