#ifndef UNIVERSITY_H
#define UNIVERSITY_H

#include "student.h"
#include "course.h"

typedef struct {
    Student students[100];
    int studentCount;
    Course courses[20];
    int courseCount;
} University;

void initializeUniversity(University* university);
void addStudents(University* university);
void addCourses(University* university);
void displayStudents(const University* university);
void displayCourses(const University* university);
void enrollStudentInCourse(University* university);

#endif
