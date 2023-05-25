from student import Student
from course import Course

class University:
    def __init__(self):
        self.students = []
        self.courses = []

    def initialize_university(self):
        self.students = []
        self.courses = []

    def add_student(self, name, age):
        student = Student(name, age)
        self.students.append(student)

    def add_course(self, name, code):
        course = Course(name, code)
        self.courses.append(course)

    def display_students(self):
        print("Students:")
        for student in self.students:
            print(f"Name: {student.name}, Age: {student.age}")

    def display_courses(self):
        print("Courses:")
        for course in self.courses:
            print(f"Name: {course.name}, Code: {course.code}")

    def enroll_student_in_course(self, student, course):
        student.enroll(course)
        course.add_student(student)
