def classify_student(grades: list[int]) -> str:
    avg_grade = sum(grades) / len(grades)
    if avg_grade >= 90:
        return "Excellent"
    elif avg_grade >= 75:
        return "Good"
    elif avg_grade >= 50:
        return "Average"
    else:
        return "Poor"


def analyze_grades(grades: list[list[int]]) -> list[int, int, int, int]:
    excellent_count = 0
    good_count = 0
    average_count = 0
    poor_count = 0

    for student_grades in grades:
        category = classify_student(student_grades)
        if category == "Excellent":
            excellent_count += 1
        elif category == "Good":
            good_count += 1
        elif category == "Average":
            average_count += 1
        else:
            poor_count += 1

    return excellent_count, good_count, average_count, poor_count


grades = [
    [85, 92, 78, 88],  # Student 1
    [45, 52, 38, 49],  # Student 2
    [99, 95, 100, 97],  # Student 3
    [70, 65, 72, 68]   # Student 4
]

output = analyze_grades(grades)
print(output)
