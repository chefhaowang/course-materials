
def classify_student(grades: list[int]) -> str:
    """
      Classifies a student based on their average grade.

      Args:
      grades (list[int]): A list of integers representing the grades of a student.

      Returns:
      str: A string representing the classification of the student.
          - "Excellent" if the average grade is 90 or above.
          - "Good" if the average grade is between 75 and 89.
          - "Average" if the average grade is between 50 and 74.
          - "Poor" if the average grade is below 50.
      """
    pass


def analyze_grades(grades: list[list[int]]) -> list[int, int, int, int]:
    """
      Analyzes the grades of multiple students and categorizes them into four groups:
      "Excellent", "Good", "Average", and "Poor".

      Args:
      grades (list[list[int]]): A two-dimensional list where each inner list contains the grades of a student.

      Returns:
      list[int, int, int, int]: A list of four integers representing the count of students in each category:
          - The first integer is the count of "Excellent" students.
          - The second integer is the count of "Good" students.
          - The third integer is the count of "Average" students.
          - The fourth integer is the count of "Poor" students.
      """
    pass


grades = [
    [85, 92, 78, 88],  # Student 1
    [45, 52, 38, 49],  # Student 2
    [99, 95, 100, 97],  # Student 3
    [70, 65, 72, 68]   # Student 4
]

output = analyze_grades(grades)
print(output)
