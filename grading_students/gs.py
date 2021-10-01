import math

def grading_students(grades):
    """
    Given a list of grades, return a list of grades with the next standard
    If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
    If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.
    """
    new_grades = []
    for grade in grades:
        if grade < 38:
            new_grades.append(grade)
        else:
            multiple = math.ceil(grade / 5) * 5
            new_grades.append(multiple) if (multiple-grade) < 3 else new_grades.append(grade)
    return new_grades

if __name__ == "__main__":
    print(grading_students([73, 67, 38, 33]))