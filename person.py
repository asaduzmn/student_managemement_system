from dataclasses import dataclass


@dataclass
class Person:
    """
    A class to manage all the information of a single person
    """
    name : str
    age : int
    address : str

  
    # Display all the info of a person
    def display_person_info(self):
        print("Student Information: ")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")




