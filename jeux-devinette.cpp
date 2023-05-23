#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int nombreToChiffre, chiffre, attempts = 0;
    srand(time(NULL));
    nombreToChiffre = rand() % 100 + 1;

    printf("Bienvenue dans le jeu de devinette !\n");

    while (1) {
        printf("Devinez le nombreToChiffre (entre 1 et 100) : ");
        scanf("%d", &chiffre);
        attempts++;

        if (chiffre < nombreToChiffre) {
            printf("C'est plus grand !\n");
        } else if (chiffre > nombreToChiffre) {
            printf("C'est plus petit !\n");
        } else {
            printf("Félicitations ! Vous avez trouvé le nombre en %d tentatives.\n", attempts);
            break;
        }
    }

    return 0;
}
