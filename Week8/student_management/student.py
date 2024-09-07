from person import Person 

class Student(Person):
    """
    A class to represent a student, inheriting from the Person class.
    
    Attributes:
    -----------
    student_id : str
        The unique ID of the student.
    courses : dict
        A dictionary containing course names as keys and their grade and attendance as values.
    gpa : float
        The GPA of the student based on enrolled courses.
    
    Methods:
    --------
    add_course(course_name: str) -> None:
        Adds a course to the student's list of courses.
    
    update_grade(course_name: str, grade: float) -> None:
        Updates the grade for a specific course.
        
    update_attendance(course_name: str, attendance: float) -> None:
        Updates the attendance for a specific course.
    
    calculate_gpa() -> None:
        Calculates and updates the student's GPA.
    
    get_details() -> str:
        Returns a string with the student's details.
    """

    def __init__(self, name: str, age: int, student_id: str):
        super().__init__(name, age)
        self.student_id = student_id
        # Dictionary with course names as keys and (grade, attendance) as values
        self.courses = {}
        self.gpa = 0.0

    def add_course(self, course_name: str) -> None:
        """
        Adds a course to the student's course list.
        
        Args:
        course_name (str): The name of the course to add.
        """
        if course_name not in self.courses:
            self.courses[course_name] = {"grade": None, "attendance": 0.0}
            print(f"{self.name} has been enrolled in {course_name}.")
        else:
            print(f"{self.name} is already enrolled in {course_name}.")

    def update_grade(self, course_name: str, grade: float) -> None:
        """
        Updates the grade for a specific course.
        
        Args:
        course_name (str): The course to update.
        grade (float): The grade to assign.
        """
        if course_name in self.courses:
            self.courses[course_name]["grade"] = grade
            print(f"Updated {self.name}'s grade in {course_name} to {grade}.")
            self.calculate_gpa()
        else:
            print(f"{self.name} is not enrolled in {course_name}.")

    def update_attendance(self, course_name: str, attendance: float) -> None:
        """
        Updates the attendance for a specific course.
        
        Args:
        course_name (str): The course to update attendance for.
        attendance (float): The percentage attendance to assign.
        """
        if course_name in self.courses:
            self.courses[course_name]["attendance"] = attendance
            print(f"Updated {self.name}'s attendance in {
                  course_name} to {attendance}%.")
        else:
            print(f"{self.name} is not enrolled in {course_name}.")

    def calculate_gpa(self) -> None:
        """
        Calculates the GPA based on the grades of the enrolled courses.
        """
        total_grades = 0
        course_count = 0
        for course, info in self.courses.items():
            if info["grade"] is not None:
                total_grades += info["grade"]
                course_count += 1
        self.gpa = total_grades / course_count if course_count > 0 else 0.0

    def get_details(self) -> str:
        """
        Returns a string with the student's details, including enrolled courses, grades, attendance, and GPA.
        
        Returns:
        str: A formatted string with student details.
        """
        course_details = "\n".join([f"{course}: Grade={info['grade']}, Attendance={
                                   info['attendance']}%" for course, info in self.courses.items()])
        return f"Student Name: {self.name}\nStudent ID: {self.student_id}\nCourses:\n{course_details}\nGPA: {self.gpa:.2f}"
