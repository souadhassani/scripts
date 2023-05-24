import random

nombreToChiffre = random.randint(1, 100)
attempts = 0

print("Bienvenue dans le jeu de devinette !")

while True:
    chiffre = int(input("Devinez le nombreToChiffre (entre 1 et 100) : "))
    attempts += 1

    if chiffre < nombreToChiffre:
        print("C'est plus petit !")
    elif chiffre > nombreToChiffre:
        print("C'est plus grand !")
    else:
        print("Félicitations ! Vous avez trouvé le nombre en", attempts, "tentatives.")
        break
