#include <stdio.h>
#include "student.h"

void addStudent(University* university, const char* name, int age) {
    // Ajouter un nouvel étudiant à l'université
    Student student;
    strcpy(student.name, name);
    student.age = age;
    // ...
}


void displayStudent(const Student* student) {
    
}

void enrollStudentInCourse(Student* student, const Course* course) {
   
}
