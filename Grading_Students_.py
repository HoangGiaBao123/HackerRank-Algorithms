import math
import os
import sys

def gradingStudents(grades):
    grade = []
    for g in grades:
        if g < 38 or g % 5 < 3:
            grade.append(g)
        else:
            grade.append(g + (5 - g % 5))
    return grade

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    grades_count = int(input().strip())
    grades = []
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)
    result = gradingStudents(grades)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
