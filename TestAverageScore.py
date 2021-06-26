import unittest
from AverageScore import *

class TestAverageScore(unittest.TestCase):

    def test__init__(self):
        self.assertRaises(TypeError, AverageScore.__init__(-50, 60, 70), )

    def test_calculate_avg_score(self):
        student_marks = AverageScore(50,60,70)
        self.assertEquals(student_marks.calculate_avg_score(), 60, "Average Score Not Calculated Correctly")
        self.assertAlmostEquals(student_marks.calculate_avg_score(), 60, 1, "Average Score Not Calculated Correctly")
    #   self.assertNotEqual(student_marks.calculate_avg_score(),60,"")

if __name__ == '__main__':
    unittest.main()
