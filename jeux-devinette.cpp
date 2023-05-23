#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int nombre, chiffre, attempts = 0;
    srand(time(NULL));
    nombre = rand() % 100 + 1;

    printf("Bienvenue dans le jeu de devinette !\n");

    while (1) {
        printf("Devinez le nombre (entre 1 et 100) : ");
        scanf("%d", &chiffre);
        attempts++;

        if (chiffre < nombre) {
            printf("C'est plus grand !\n");
        } else if (chiffre > nombre) {
            printf("C'est plus petit !\n");
        } else {
            printf("Félicitations ! Vous avez trouvé le nombre en %d tentatives.\n", attempts);
            break;
        }
    }

    return 0;
}
