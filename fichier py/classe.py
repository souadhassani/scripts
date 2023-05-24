class personne:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"hey, je m'appelle {self.name} ,j'ai {self.age} years old.")

class etudiant(personne):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def introduce(self):
        super().introduce()
        print(f"je suis etudiant en {self.grade}.")

class prof(personne):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        super().introduce()
        print(f"je suis prof de {self.subject}.")

class AFORP:
    def __init__(self, name):
        self.name = name
        self.etudiants = []
        self.profs = []

    def add_etudiant(self, etudiant):
        self.etudiants.append(etudiant)

    def add_prof(self, prof):
        self.profs.append(prof)

    def list_etudiants(self):
        print(f"etudiants en {self.name}:")
        for etudiant in self.etudiants:
            print(etudiant.name)

    def list_profs(self):
        print(f"profs en {self.name}:")
        for prof in self.profs:
            print(prof.name)

# Exemple d'utilisation des classes

# Création d'objets personne
personne1 = personne("souad", 25)
personne2 = personne("Alice", 30)

personne1.introduce()
personne2.introduce()

# Création d'objets etudiant
etudiant1 = etudiant("amine", 18, 12)
etudiant2 = etudiant("saadi", 17, 11)

etudiant1.introduce()
etudiant2.introduce()

# Création d'objets prof
prof1 = prof("Mr. Yoan", 40, "C")
prof2 = prof("Ms. SAS", 35, "réseau")

prof1.introduce()
prof2.introduce()

# Création d'un objet AFORP
AFORP = AFORP("AFORP")

# Ajout des étudiants et des enseignants à l'école
AFORP.add_etudiant(etudiant1)
AFORP.add_etudiant(etudiant2)
AFORP.add_prof(prof1)
AFORP.add_prof(prof2)

# Liste des étudiants et des enseignants dans l'école
AFORP.list_etudiants()
AFORP.list_profs()
