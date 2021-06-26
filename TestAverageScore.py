import unittest
from AverageScore import *

class TestAverageScore(unittest.TestCase):
    def test_calculate_avg_score(self):
        student_marks = AverageScore(50,60,70)
        self.assertEqual(student_marks.calculate_avg_score(),60,"Average Score Not Calculated Correctly")

if __name__ == '__main__':
    unittest.main()
