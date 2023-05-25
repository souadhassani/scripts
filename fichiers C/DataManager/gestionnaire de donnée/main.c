#include <stdio.h>
#include "university.h"

int main() {
    University university;
    initializeUniversity(&university);

    // Appel des fonctions pour effectuer des opérations spécifiques
    addStudents(&university);
    addCourses(&university);
    displayStudents(&university);
    displayCourses(&university);
    enrollStudentInCourse(&university);

    return 0;
}
