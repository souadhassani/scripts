#include <stdio.h>
#include <stdlib.h>
#include "ordinateur.h"

void myMain;
int main() {
    int choix;
    float prixTotal = 0.0;

    while (1) {
        printf("1. Ajouter un nouvel ordinateur\n");
        printf("2. Consulter les details d'un ordinateur\n");
        printf("3. Mettre a jour les stocks\n");
        printf("4. Quitter\n");
        printf("Choix : ");
        scanf("%d", &choix);

        switch (choix) {
            case 1:
                ajouterOrdinateur();
                break;
            case 2:
                consulterDetails();
                break;
            case 3:
                mettreAJourStocks();
                break;
            case 4:
                exit(0);
            default:
                printf("Choix invalide\n");
                break;
        }
    }

    return 0;
}
