from AverageScore import *
from ProgressScore import *

# Loop responsible for taking input and calculating AverageScore and Average ProgressScore
run = "Yes"
while run == "Yes":
    # Ask for input from user
    student_code = str(input("Enter student code:"))
    mock_Maths_marks = float(input("Enter Mock result achieved in Maths:"))
    actual_Maths_marks = float(input("Enter Actual marks achieved in Maths:"))
    mock_English_marks = float(input("Enter Mock result achieved in English:"))
    actual_English_marks = float(input("Enter Actual marks achieved in English:"))
    mock_Science_marks = float(input("Enter Mock result achieved in Science:"))
    actual_Science_marks = float(input("Enter Actual marks achieved in Science:"))

    # Instantiation of AverageScore
    average_score = AverageScore(actual_Maths_marks, actual_English_marks, actual_Science_marks)
    # Instantiation of ProgressScore
    average_progress_score = ProgressScore(mock_Maths_marks, actual_Maths_marks, mock_English_marks,
                                           actual_English_marks, mock_Science_marks, actual_Science_marks)
    print(" ")
    # Calculation of AverageScore and Average Progress score and printing the result
    print("Average score for student-" + student_code + " is", average_score.calculate_avg_score(),
          "and their average progress score is", average_progress_score.calculate_avg_progress_score())
    print(" ")
    # Asks user to continue or end the loop
    run = str(input("Do you want to continue with another student? Yes/No: "))
    print(" ")