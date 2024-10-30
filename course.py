from dataclasses import dataclass, field

@dataclass
class Course():
    """
    A class to store all courses that are provided
    """
    course_name: str
    course_code: str
    instructor: str
    students: list[str] = field(default_factory=list)

    # Add a student to the course
    def add_student(self, student_id):
        if student_id in self.students:
            return False
        self.students.append(student_id)
        return True          
            

    # Display course details and list of enrolled students
    def display_course_info(self):
        print("Course Information:")
        print(f"Course Name: {self.course_name}")
        print(f"Code: {self.course_code}")
        print(f"Instructor: {self.instructor}")
        return self.students