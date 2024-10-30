from dataclasses import asdict
import json
from course import Course
from student import Student


class University:
    """
    University student management system
    """
    def __init__(self) -> None:
        self.students = {}
        self.courses = {}
        self.options = {
            "1" : self.add_student,
            "2" : self.add_course,
            "3" : self.enroll_course,
            "4" : self.add_grade,
            "5" : self.display_student_info,
            "6" : self.display_course_info,
            "7" : self.save_data,
            "8" : self.load_data  
        }


    def add_student(self):
        """
        Take student info and pass it to the Stuent class
        """
        name = input("Enter Name: ")
        age = self.get_valid_age()
        address = input("Enter address: ")
        student_id = input("Enter Sudent Id: ")

        if self.is_student(student_id):
            print(f"Student ID ({student_id}) already exist.")
        else:
            student = Student(name,age, address,student_id)
            self.students[student_id] = student
            print(f"{student.name} (ID: {student.student_id}) added successfully.")
            

    def add_course(self):
        """
        Take course info and pass it to course class
        """
        course_name = input("Enter Course Name: ")
        course_code = input("Enter Course Code: ")
        instructor = input("Enter Instructor Name: ")

        if self.is_course(course_code):
            print(f"Course code ({course_code}) already exist.")
            return
        
        course = Course(course_name, course_code, instructor)
        self.courses[course_code] = course
        print(f"Course {course.course_name} (Code: {course.course_code}) created with instructor {course.instructor}.")
            

    def enroll_course(self):
        """
        enroll a student to a specific course
        """
        student_id = input("Enter Student ID: ")
        course_code = input("Enter Course Code: ")

        if not self.is_student(student_id):
            print(f"Student ID ({student_id}) does not exist.")
            return

        if not self.is_course(course_code):
            print(f"Course code ({course_code}) does not exist.")
            return

        student = self.students[student_id]
        course = self.courses[course_code]

        # Enrollment
        enrolled = student.enroll_course(course.course_name)
        added = course.add_student(student.student_id)

        if added and enrolled:
            print(f"{student.name} (ID: {student.student_id}) enrolled in {course.course_name} (Code: {course.course_code}).")
        else:
            print(f"{student.student_id} is already enrolled in the course {course.course_code}.")




    def add_grade(self):
        """
        Add grade for student
        """
        student_id = input("Enter Student ID: ")
        course_code = input("Enter Course Code: ")
        grade = input("Enter Grade: ")

        if not self.is_student(student_id):
            print(f"Student ID ({student_id}) is not exist.")
            return          

        if not self.is_course(course_code):
            print(f"Course code ({course_code}) is not exist.")
            return

        student = self.students[student_id]
        course = self.courses[course_code]
        added = student.add_grade(course.course_name, grade)
        if added:
            print(f"Grade {grade} added for {student.name} in {course.course_name}.")

    
    def display_student_info(self):
        """
        Show whole information of a student
        """
        student_id = input("Enter Student ID: ")

        if not self.is_student(student_id):
            print(f"Student ID ({student_id}) is not exist.")
            return
        
        student = self.students[student_id]
        student.display_student_info()
        
            
    def display_course_info(self):
        """
        show course info and course details
        """
        course_code = input("Enter Course Code: ")

        if not self.is_course(course_code):
            print(f"Course code ({course_code}) is not exist.")
            return
        
        course = self.courses[course_code]
        enrolled_st_id = course.display_course_info()
        print("Enrolled Students:", ", ".join(self.students[st_id].name for st_id in enrolled_st_id))
        
    
    def save_data(self):
        """
        Save students and courses info into json format
        """
        with open("courses.json", "w") as file:
            json.dump({key: asdict(value) for key, value in self.courses.items()}, file, indent=4)
        with open("students.json","w") as file:
            json.dump({key: asdict(value) for key, value in self.students.items()},file, indent=4)

        print("All student and course data saved successfully.")

    
    def load_data(self):
        """
        Load students and courses info
        """
        with open("courses.json", "r") as file:
            self.courses = json.load(file)
        with open("students.json", "r") as file:
            self.students = json.load(file)

        # Reconstruct the Course and Student instances
        self.courses = {key: Course(**value) for key, value in self.courses.items()}
        self.students = {key: Student(**value) for key, value in self.students.items()}
        
        print("Data loaded successfully.")

    
    def start_app(self):
        # Program starts with a display
        prompt ="""
        1. Add New Student
        2. Add New Course
        3. Enroll Student in Course
        4. Add Grade for Student
        5. Display Student Details
        6. Display Course Details
        7. Save Data to File
        8. Load Data from File
        0. Exit
        """
        while True:
            print(prompt)

            # c_option -> choosen option
            c_option = input("Select option: ")

            # while c_option:
            if(c_option in bup.options):
                bup.options[c_option]()
            elif c_option == "0":
                print("Exiting Student Management System. Goodbye!")
                break
            else:
                print("Please choose option 0-8")


    def is_student(self, student_id):
        """
        Check whether student is added
        """
        if student_id in self.students:
            return True
        else:
            False

    def get_valid_age(self):
        while True:
            age_input = input("Enter age: ")
            try:
                age = int(age_input)  
                if age < 0:
                    print("Age cannot be negative. Please enter a valid age.")
                else:
                    return age  
            except ValueError:
                print(f"Invalid input '{age_input}'. Please enter a valid integer for age.")


    def is_course(self, course_code):
        """
        Check whether course is added
        """
        if course_code in self.courses:
            return True
        else:
            False


if __name__ == "__main__":
    bup = University()
    bup.start_app()


