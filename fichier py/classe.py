class Etudiant:
    def __init__(self, nom, prenom, numero_etudiant, age):
        self.nom = nom
        self.prenom = prenom
        self.numero_etudiant = numero_etudiant
        self.age = age

    def getNom(self):
        return self.nom

    def getPrenom(self):
        return self.prenom

    def estPlusAgeQue(self, age):
        if self.age > age:
            return True
        else:
            return False    
    
# déclaration d'un objet

unEtudiant = Etudiant("HASSANI", "souad", 22107137, 28)

print(Etudiant.getNom)
