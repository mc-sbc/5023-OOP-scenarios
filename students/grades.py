# Create a class called Student
class Student:
  
    # # Initialiser method with 5 attributes and their type hint
    def __init__(self, name: str, english_mark: int, science_mark: int, mathematics_mark: int, completed_assessments: bool, ):
        self.name = name
        self.english_mark = english_mark
        self.science_mark = science_mark
        self.mathematics_mark = mathematics_mark
        self.completed_assessments = completed_assessments

    # Function that calculates average of the three student marks and rounds result to 2 decimal places 
    def ave_marks(self):
        ave = (self.english_mark + self.science_mark + self.mathematics_mark) / 3
        return round(ave)