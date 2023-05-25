#include <stdio.h>
#include "student.h"

void addStudent(University* university, const char* name, int age) {
    Student student;
    strcpy(student.name, name);
    student.age = age;
    // ...
}