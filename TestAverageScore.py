import unittest
from AverageScore import *

class TestAverageScore(unittest.TestCase):

    def test_validate_input_values(self):
        self.assertRaises(ValueError, AverageScore.validate_negative_input, self, -88, 96, 54)

    def test_calculate_avg_score(self):
        student_marks = AverageScore(88, 96, 54)
        self.assertAlmostEqual(student_marks.calculate_avg_score(), 79.33, 2, "Average Score Not Calculated Correctly")

    def test_check_input_size(self):
        student_marks = AverageScore(88, 96, 54)
        self.assertRaises(ValueError, student_marks.validate_input_size, 880, 96, 54)

    def test_check_input_datatype(self):
        self.assertRaises(ValueError, AverageScore.validate_input_datatype, self, "88", 96, 54)

if __name__ == '__main__':
    unittest.main()