#define STUDENT_H
#define STUDENT_H

typedef struct {
    char name[50];
    int age;
} Student;

void addStudent(university* university, const char* name, int age);
void displayStudent(const Student* student);
void enrollStudentInCourse(Student* student, const course* course);

#endif
