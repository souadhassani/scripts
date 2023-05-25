#include <stdio.h>
#include "university.h"

void initializeUniversity(University* university) {
    university->studentCount = 0;
    university->courseCount = 0;
}


void addStudents(University* university) {
    Student student1 = {"John", 20};
    Student student2 = {"Alice", 22};
    // ...
}
