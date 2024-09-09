grades = [
    [85, 92, 78, 88],  # Student 1
    [45, 52, 38, 49],  # Student 2
    [99, 95, 100, 97],  # Student 3
    [70, 65, 72, 68]   # Student 4
]

excellent_count = 0
good_count = 0
average_count = 0
poor_count = 0

for student_grades in grades:
    category = ""
    avg_grade = sum(student_grades) / len(student_grades)
    if avg_grade >= 90:
        category = "Excellent"
    elif avg_grade >= 75:
        category = "Good"
    elif avg_grade >= 50:
        category = "Average"
    else:
        category = "Poor"

    if category == "Excellent":
        excellent_count += 1
    elif category == "Good":
        good_count += 1
    elif category == "Average":
        average_count += 1
    else:
        poor_count += 1

print(excellent_count, good_count, average_count, poor_count)

