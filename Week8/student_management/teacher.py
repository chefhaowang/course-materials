from person import Person
from student import Student

class Teacher(Person):
    """
    A class to represent a teacher, inheriting from the Person class.
    
    Attributes:
    -----------
    teacher_id : str
        The unique ID of the teacher.
    department : str
        The department the teacher belongs to.
    courses : list
        A list of courses the teacher teaches.
    
    Methods:
    --------
    assign_course(course: Course) -> None:
        Assigns a course to the teacher.
    
    view_students(course: Course) -> None:
        Views students in the teacher's course.
    
    update_student_grade(student: Student, course_name: str, grade: float) -> None:
        Updates the grade of a student for a specific course.
    
    update_student_attendance(student: Student, course_name: str, attendance: float) -> None:
        Updates the attendance of a student for a specific course.
    """

    def __init__(self, name: str, age: int, teacher_id: str, department: str):
        super().__init__(name, age)
        self.teacher_id = teacher_id
        self.department = department
        self.courses = []

    def assign_course(self, course) -> None:
        """
        Assigns a course to the teacher.
        
        Args:
        course (Course): The course to assign to the teacher.
        """
        self.courses.append(course)
        print(f"{self.name} has been assigned to teach {course.course_name}.")

    def view_students(self, course) -> None:
        """
        Views the students enrolled in the teacher's course.
        
        Args:
        course (Course): The course to view students for.
        """
        print(f"Students in {course.course_name}:")
        for student in course.students:
            print(f"{student.name} (ID: {student.student_id})")

    def update_student_grade(self, student: Student, course_name: str, grade: float) -> None:
        """
        Updates the grade of a student for a specific course.
        
        Args:
        student (Student): The student whose grade is to be updated.
        course_name (str): The course to update the grade for.
        grade (float): The grade to assign.
        """
        student.update_grade(course_name, grade)

    def update_student_attendance(self, student: Student, course_name: str, attendance: float) -> None:
        """
        Updates the attendance of a student for a specific course.
        
        Args:
        student (Student): The student whose attendance is to be updated.
        course_name (str): The course to update the attendance for.
        attendance (float): The attendance percentage to assign.
        """
        student.update_attendance(course_name, attendance)
