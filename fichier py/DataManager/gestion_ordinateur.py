from ordinateur import Ordinateur

ordinateurs = []
nombreOrdinateurs = 0

def ajouterOrdinateur():
    global nombreOrdinateurs
    if nombreOrdinateurs >= 10:
        print("Le nombre maximal d'ordinateurs a été atteint.")
        return

    print("Ajout d'un nouvel ordinateur")
    marque = input("Marque : ")
    stock = int(input("Stock : "))
    prix = float(input("Prix : "))

    ordinateur = Ordinateur(marque, stock, prix)
    ordinateurs.append(ordinateur)
    nombreOrdinateurs += 1
    print("L'ordinateur a été ajouté avec succès.")

def consulterDetails():
    index = int(input("Numéro de l'ordinateur : "))

    if index >= 0 and index < nombreOrdinateurs:
        ordinateur = ordinateurs[index]
        print("Détails de l'ordinateur")
        print("Marque :", ordinateur.marque)
        print("Stock :", ordinateur.stock)
        print("Prix :", ordinateur.prix)
    else:
        print("Numéro d'ordinateur invalide.")

def mettreAJourStocks():
    index = int(input("Numéro de l'ordinateur : "))

    if index >= 0 and index < nombreOrdinateurs:
        composant = int(input("Composant (0: Processeur, 1: Carte graphique, 2: RAM, 3: Stockage) : "))

        if composant >= 0 and composant <= 3:
            quantite = int(input("Quantité : "))

            if quantite >= 0:
                ordinateurs[index].stock += quantite
                print("Les stocks ont été mis à jour avec succès.")
            else:
                print("Quantité invalide.")
        else:
            print("Composant invalide.")
    else:
        print("Numéro d'ordinateur invalide.")

def main():
    while True:
        print("1. Ajouter un nouvel ordinateur")
        print("2. Consulter les détails d'un ordinateur")
        print("3. Mettre à jour les stocks")
        print("4. Quitter")
        choix = int(input("Choix : "))

        if choix == 1:
            ajouterOrdinateur()
        elif choix == 2:
            consulterDetails()
        elif choix == 3:
            mettreAJourStocks()
        elif choix == 4:
            break
        else:
            print("Choix invalide.")

if __name__ == "__main__":
    main()
