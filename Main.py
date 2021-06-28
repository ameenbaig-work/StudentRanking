from AverageScore import *
from ProgressScore import *

run = "Yes"
while run == "Yes":
    student_code = str(input("Enter student code:"))
    mock_Maths_marks = int(input("Enter mock marks achieved in Maths:"))
    actual_Maths_marks = int(input("Enter actual marks achieved in Maths:"))
    mock_English_marks = int(input("Enter mock marks achieved in English:"))
    actual_English_marks = int(input("Enter actual marks achieved in English:"))
    mock_Science_marks = int(input("Enter mock marks achieved in Science:"))
    actual_Science_marks = int(input("Enter actual marks achieved in Science:"))

    average_score = AverageScore(actual_Maths_marks, actual_English_marks, actual_Science_marks)
    average_progress_score = ProgressScore(mock_Maths_marks, actual_Maths_marks, mock_English_marks,
                                           actual_English_marks, mock_Science_marks, actual_Science_marks)
    print(" ")
    print("Average score for student-" + student_code + " is", average_score.calculate_avg_score(),
          "and their average progress score is", average_progress_score.calculate_avg_progress_score())
    print(" ")
    run = str(input("Go again? Yes/No: "))
    print(" ")