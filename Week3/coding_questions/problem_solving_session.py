grades = [
    [85, 92, 78, 88],  # Student 1
    [45, 52, 38, 49],  # Student 2
    [99, 95, 100, 97],  # Student 3
    [70, 65, 72, 68],   # Student 4
    [52, 65, 72, 99]    # student 5
]

excellent_count = 0
good_count = 0
average_count = 0
poor_count = 0

excellent_students = []
good_students = []
average_students = []
poor_students = []

# Iterate over each student's grades
for student_grades in grades:

    highest_grade = max(student_grades)
    lowest_grade = min(student_grades)

    average_grade = sum(student_grades) / len(student_grades)

    # Classify students based on average grade
    if average_grade >= 90:
        excellent_count += 1
        excellent_students.append(
            [student_grades, highest_grade, lowest_grade])
    elif 75 <= average_grade < 90:
        good_count += 1
        good_students.append([student_grades, highest_grade, lowest_grade])
    elif 50 <= average_grade < 75:
        average_count += 1
        average_students.append([student_grades, highest_grade, lowest_grade])
    else:
        poor_count += 1
        poor_students.append([student_grades, highest_grade, lowest_grade])


print("Excellent Students:")
print(f"Count: {excellent_count}")
for student in excellent_students:
    print(f"Grades: {student[0]}, Highest: {student[1]}, Lowest: {student[2]}")

print("\nGood Students:")
print(f"Count: {good_count}")
for student in good_students:
    print(f"Grades: {student[0]}, Highest: {student[1]}, Lowest: {student[2]}")

print("\nAverage Students:")
print(f"Count: {average_count}")
for student in average_students:
    print(f"Grades: {student[0]}, Highest: {student[1]}, Lowest: {student[2]}")

print("\nPoor Students:")
print(f"Count: {poor_count}")
for student in poor_students:
    print(f"Grades: {student[0]}, Highest: {student[1]}, Lowest: {student[2]}")
