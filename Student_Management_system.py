import json
import os

class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade
    
    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.load_data()
    
    def load_data(self):
        if os.path.exists('students.json'):
            with open('students.json', 'r') as file:
                data = json.load(file)
                for student_data in data:
                    self.students.append(
                        Student(
                            student_data['student_id'],
                            student_data['name'],
                            student_data['age'],
                            student_data['grade']
                        )
                    )
    
    def save_data(self):
        data = []
        for student in self.students:
            data.append({
                'student_id': student.student_id,
                'name': student.name,
                'age': student.age,
                'grade': student.grade
            })
        with open('students.json', 'w') as file:
            json.dump(data, file, indent=4)
    
    def add_student(self):
        print("\nAdd New Student")
        student_id = input("Enter student ID: ")
        
        # Check if student ID already exists
        for student in self.students:
            if student.student_id == student_id:
                print("Student ID already exists!")
                return
        
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        grade = input("Enter student grade: ")
        
        new_student = Student(student_id, name, age, grade)
        self.students.append(new_student)
        self.save_data()
        print("Student added successfully!")
    
    def view_all_students(self):
        print("\nAll Students")
        if not self.students:
            print("No students in the system.")
        else:
            for student in self.students:
                print(student)
    
    def search_student(self):
        search_term = input("\nEnter student ID or name to search: ")
        found = False
        
        for student in self.students:
            if (search_term.lower() in student.name.lower()) or (search_term == student.student_id):
                print(student)
                found = True
        
        if not found:
            print("No matching students found.")
    
    def update_student(self):
        student_id = input("\nEnter student ID to update: ")
        found = False
        
        for student in self.students:
            if student.student_id == student_id:
                print("Current student details:")
                print(student)
                
                print("\nEnter new details (leave blank to keep current value):")
                name = input(f"Name [{student.name}]: ") or student.name
                age = input(f"Age [{student.age}]: ") or student.age
                grade = input(f"Grade [{student.grade}]: ") or student.grade
                
                student.name = name
                student.age = age
                student.grade = grade
                
                self.save_data()
                print("Student updated successfully!")
                found = True
                break
        
        if not found:
            print("Student not found!")
    
    def delete_student(self):
        student_id = input("\nEnter student ID to delete: ")
        for i, student in enumerate(self.students):
            if student.student_id == student_id:
                del self.students[i]
                self.save_data()
                print("Student deleted successfully!")
                return
        
        print("Student not found!")

    def display_menu(self):
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-6): ")
            
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.view_all_students()
            elif choice == '3':
                self.search_student()
            elif choice == '4':
                self.update_student()
            elif choice == '5':
                self.delete_student()
            elif choice == '6':
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    system = StudentManagementSystem()
    system.run()
