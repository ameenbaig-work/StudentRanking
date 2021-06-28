# StudentRanking

# Main:
    1. Imports all attributes from the classes AverageScore and ProgressScore
    2. Code responsible for taking user input and calculating the AverageScore and Average Progress score is structured in a while loop, where:
      a) The user is asked for the Mock result and actual score in all three subjects.
      b) An instance of class AverageScore and class ProgressScore is created respectively.
      c) The AverageScore and Average Progress score is calculated and output to the user.


# AverageScore:
  # A Template defining Average Score for the Actual scores for the 3 subjects which contains: 
    1. Initializing method for class AverageScore, this method defines the properties (ie. Actual scores for the 3 subjects) and populates them
    2. Method for calling the three testing methods below:
      a) Raises an error if any of the properties are negative
      b) Raises an error if any of the properties are greater than 100
      c) Raises an error if any of the properties are a string
    3. Calculates the average score for the 3 subjects
    
# TestAverageScore:
    1. Imports all attributes from the class AverageScore
    2. TestCase for AverageScore: inheriting the class unittest.TestCase which contains methods for checking if:
      a) Any of the properties are negative
      b) The calculated AverageScore is correct to 2 decimal places, which raises an error if the calculated value is incorrect
      c) Any of the properties exceed 100 marks
      d) Any of the properties are of datatype "string"
    
  
# ProgressScore:
  # A Template defining Average Progress Score for the Actual scores and the Mock scores for the 3 subjects which contains: 
    1. Initializing method for class ProgressScore, this method defines the properties (ie. Actual scores and Progress scores for the 3 subjects) and populates them
    2. Method for calling the two testing methods below:
      a) Raises an error if any of the properties are greater than 100
      b) Raises an error if any of the properties are a string
    3. Calculates the Average ProgressScore for the 3 subjects
    
# TestProgressScore:
    1. Imports all attributes from the class ProgressScore
    2. TestCase for ProgressScore: inheriting the class unittest.TestCase which contains methods for checking if:
      a) The calculated Average ProgressScore is correct to 2 decimal places, which raises an error if the calculated value is incorrect
      b) Any of the properties exceed 100 marks
      c) Any of the properties are of datatype "string"
