"""

Student Management System
==========================

1. Add Student
2. View Student -> All and One
3. Update Student
4. Delete Student
5. Exit

"""


class Student:
    def __init__(self, name: str, age: int, address: str, marks: int) -> None:
        self.name = name
        self.age = age
        self.address = address
        self.marks = marks

class StudentManagementSystem:
    def __init__(self):
        self.students = []
        
    def add_student(self):
        while True:
            name = input("Enter your name: ")
            if name.replace(" ", "").isalpha():
                break
            else:
                print("It's a invalid input. Enter only alphabets.")
        age = int(input("Enter your age: "))
        address = (input("Enter your address: "))
        marks = int(input("Enter your marks: "))

        student = Student(name, age, address, marks)
        self.students.append(student)
        print("Student Successfully Added..!")
        return student
    
    def view_students(self):
        if len(self.students) == 0:
            print("No Students found")
        else:
            view_type = input("All Students or One Student? (all/one): ")
            if view_type == "all":
                for student in self.students:
                    print(f"name: {student.name}\n age: {student.age}\n address: {student.address}\n marks: {student.marks}")

            if view_type == "one":
                name = input("Enter the name of the student you want to see: ")
                for student in self.students:
                    if student.name == name:
                        print(f"name: {student.name}\n age: {student.age}\n address: {student.address}\n marks: {student.marks}") 

    def delete_student(self):
        name = input("Enter the student you want to delete: ")
        for student in self.students:
            if student.name == name:
                 self.students.remove(student)
            print("Student Successfully Deleted..!")
            return self.students

    def update_student(self):
        name = input("Enter the student you want to update: ")
        for student in self.students:
            if student.name == name:
                print(f"Student found: {student.name}\n Age: {student.age}\n Address: {student.address}\n Marks: {student.marks}")
                print("What do you want to update?")
                print("1. Name")
                print("2. Age")
                print("3. Address")
                print("4. Marks")
                print("5. Exit Update")
            
        while True:
            option = input("Enter your choice (1-5): ")
            if option == "1":
                new_name = input("Enter the new name: ")
                if all(char.isalpha() or char.isspace() for char in new_name): 
                    student.name = new_name
                    print("Name updated successfully!")
                else:
                    print("Invalid name. Please use only alphabets and spaces.")
            elif option == "2":
                student.age = int(input("Enter the new age: "))
                print("Age updated successfully!")
            elif option == "3":
                student.address = input("Enter the new address: ")
                print("Address updated successfully!")
            elif option == "4":
                student.marks = int(input("Enter the new marks: "))
                print("Marks updated successfully!")
            elif option == "5":
                print("Exiting update.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
            print("Student Successfully Updated..!")
            break
        return student
        print("Student not found")

print("Welcome to the Student Management System.")
system = StudentManagementSystem()

while True:
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Update Student")
    print("4. View Student")
    print("5. Exit the System")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
         system.add_student()
    elif choice == 2:
         system.delete_student()
    elif choice == 3:
         system.update_student()
    elif choice == 4:
         system.view_students()
    elif choice == 5:
         break
    else:
         print("Invalid Choice")
         


                         

         
