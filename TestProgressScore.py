import unittest
from ProgressScore import *

class TestProgressScore(unittest.TestCase):

    def test_calculate_avg_progress_score(self):
        student_marks = ProgressScore(99, 88, 92, 96, 79, 54)
        self.assertAlmostEqual(student_marks.calculate_avg_progress_score(), -1.07, 2, "Average Score Not Calculated Correctly")

    def test_check_input_size(self):
        student_marks = ProgressScore(99, 88, 92, 96, 79, 54)
        self.assertRaises(ValueError, student_marks.validate_input_size, 990, 88, 92, 96, 79, 54)

    def test_check_input_datatype(self):
        self.assertRaises(ValueError, ProgressScore.validate_input_datatype, self, "99", 88, 92, 96, 79, 54)

if __name__ == '__main__':
    unittest.main()