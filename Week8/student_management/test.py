from course import Course
from department import Department
from student import Student
from teacher import Teacher

# Create students
student1 = Student("John Doe", 20, "S001")
student2 = Student("Jane Smith", 22, "S002")

# Create teachers
teacher1 = Teacher("Dr. Alan", 40, "T001", "Mathematics")
teacher2 = Teacher("Prof. Marie", 45, "T002", "Physics")

# Create department
math_dept = Department("Mathematics")

# Create courses
course1 = Course("Calculus", "MATH101", teacher1)
course2 = Course("Algebra", "MATH102", teacher1)

# Add courses to department
math_dept.add_course(course1)
math_dept.add_course(course2)

# Enroll students in courses
course1.enroll_student(student1)
course1.enroll_student(student2)
course2.enroll_student(student1)

# Teacher updates grades and attendance
teacher1.update_student_grade(student1, "Calculus", 90.0)
teacher1.update_student_attendance(student1, "Calculus", 95.0)

# Get student details
print(student1.get_details())

# List all courses in a department
math_dept.list_all_courses()

# List all students in a department
math_dept.list_all_students()
