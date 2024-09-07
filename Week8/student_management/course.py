from student import Student

class Course:
    """
    A class to represent a course.
    
    Attributes:
    -----------
    course_name : str
        The name of the course.
    course_code : str
        The unique code of the course.
    teacher : Teacher
        The teacher assigned to the course.
    students : list
        A list of students enrolled in the course.
    
    Methods:
    --------
    enroll_student(student: Student) -> None:
        Enrolls a student in the course.
    
    list_students() -> str:
        Returns a formatted string of students enrolled in the course.
    """

    def __init__(self, course_name: str, course_code: str, teacher):
        self.course_name = course_name
        self.course_code = course_code
        self.teacher = teacher
        self.students = []

    def enroll_student(self, student: Student) -> None:
        """
        Enrolls a student in the course.
        
        Args:
        student (Student): The student to enroll in the course.
        """
        if student not in self.students:
            self.students.append(student)
            student.add_course(self.course_name)
            print(f"{student.name} has been enrolled in {self.course_name}.")
        else:
            print(f"{student.name} is already enrolled in {self.course_name}.")

    def list_students(self) -> str:
        """
        Lists all the students enrolled in the course.
        
        Returns:
        str: A formatted string of students' names enrolled in the course.
        """
        student_names = [student.name for student in self.students]
        return f"Students enrolled in {self.course_name}:\n" + "\n".join(student_names)
