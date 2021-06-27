import unittest
from AverageScore import *

class TestAverageScore(unittest.TestCase):

    def test_validate_input_values(self):
        self.assertRaises(ValueError, AverageScore.validate_input_values, self, -50, 60, 70)

    def test_calculate_avg_score(self):
        student_marks = AverageScore(50,60,70)
        self.assertAlmostEquals(student_marks.calculate_avg_score(), 60, 2, "Average Score Not Calculated Correctly")

    def test_check_input_size(self):
        self.assertRaises(ValueError, AverageScore.validate_input_size, self, 500, 60, 70)

    def test_check_input_datatype(self):
        self.assertRaises(ValueError, AverageScore.validate_input_datatype, self, "50", 60, 70)

if __name__ == '__main__':
    unittest.main()