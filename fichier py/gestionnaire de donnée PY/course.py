class Course:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_details(self):
        print(f"Name: {self.name}, Code: {self.code}")

    def display_students(self):
        print("Enrolled students:")
        for student in self.students:
            print(f"Student: {student.name}, Age: {student.age}")
