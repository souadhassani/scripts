from university import University

def main():
    university = University()
    university.initialize_university()

    # Ajout d'étudiants
    university.add_student("Souad HASSANI", 28)
    university.add_student("Ines MENAI", 29)

    # Ajout de cours
    university.add_course("Mathematics", "MATH101")
    university.add_course("Computer Science", "CS101")

    # Affichage des étudiants
    university.display_students()

    # Affichage des cours
    university.display_courses()

    # Inscription d'un étudiant à un cours
    student = university.students[0]
    course = university.courses[0]
    university.enroll_student_in_course(student, course)

    # Affichage des détails de l'étudiant
    student.display_details()

    # Affichage des cours auxquels l'étudiant est inscrit
    student.display_courses()

if __name__ == "__main__":
    main()
