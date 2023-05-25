class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)

    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def display_courses(self):
        print("Enrolled courses:")
        for course in self.courses:
            print(f"Course: {course.name}, Code: {course.code}")
