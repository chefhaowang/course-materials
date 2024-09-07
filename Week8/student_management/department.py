from teacher import Teacher
from course import Course

class Department:
    """
    A class to represent a department in the school.
    
    Attributes:
    -----------
    dept_name : str
        The name of the department.
    teachers : list
        A list of teachers in the department.
    courses : list
        A list of courses in the department.
    
    Methods:
    --------
    add_course(course: Course) -> None:
        Adds a course to the department.
    
    add_teacher(teacher: Teacher) -> None:
        Adds a teacher to the department.
    
    list_all_courses() -> None:
        Lists all courses offered by the department.
    
    list_all_students() -> None:
        Lists all students enrolled in the department.
    """

    def __init__(self, dept_name: str):
        self.dept_name = dept_name
        self.teachers = []
        self.courses = []

    def add_course(self, course: Course) -> None:
        """
        Adds a course to the department.
        
        Args:
        course (Course): The course to add to the department.
        """
        self.courses.append(course)
        print(f"{course.course_name} has been added to the {
              self.dept_name} department.")

    def add_teacher(self, teacher: Teacher) -> None:
        """
        Adds a teacher to the department.
        
        Args:
        teacher (Teacher): The teacher to add to the department.
        """
        self.teachers.append(teacher)
        print(f"{teacher.name} has been added to the {
              self.dept_name} department.")

    def list_all_courses(self) -> None:
        """
        Lists all the courses offered by the department.
        """
        print(f"Courses in the {self.dept_name} department:")
        for course in self.courses:
            print(course.course_name)

    def list_all_students(self) -> None:
        """
        Lists all students enrolled in the department by iterating over all courses.
        """
        all_students = set()
        for course in self.courses:
            for student in course.students:
                all_students.add(student.name)

        print(f"Students enrolled in the {self.dept_name} department:")
        for student in all_students:
            print(student)
