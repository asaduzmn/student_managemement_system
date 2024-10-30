
from dataclasses import dataclass, field
from person import Person

@dataclass
class Student(Person):
    """
        A class to store all the information of a student
    """

    student_id: str
    grades: dict[str, str] = field(default_factory=dict)
    courses: list[str] = field(default_factory=list)

    
    
    # Add or update the grade for a specified subject
    def add_grade(self, subject, grade):
        if subject not in self.courses:
            print(f"{self.student_id} is not enrolled into this course")
            return False
        
        self.grades[subject] = grade
        return True

    # Enroll the student in a specified course
    def enroll_course(self, course):
        if course in self.courses:
            return False
        self.courses.append(course)
        return True

    # Display details of the student, including the enrolled course
    def display_student_info(self):
        self.display_person_info()
        print(f"ID: {self.student_id}")
        print("Enrolled Courses: ",", ".join(self.courses) if self.courses else None)
        print(f"Grades: {self.grades}")