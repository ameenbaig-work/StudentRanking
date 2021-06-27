import unittest
from ProgressScore import *

class TestProgressScore(unittest.TestCase):

    def test_calculate_avg_progress_score(self):
        student_marks = ProgressScore(88,96,54,99,92,79)
        print(student_marks.calculate_avg_progress_score())
        self.assertAlmostEqual(student_marks.calculate_avg_progress_score(), -1.07, 2, "Average Score Not Calculated Correctly")


if __name__ == '__main__':
    unittest.main()