#include <stdio.h>
#include "ordinateur.h"

Ordinateur ordinateurs[10];
int nombreOrdinateurs = 0;

void ajouterOrdinateur() {
    if (nombreOrdinateurs >= 10) {
        printf("Le nombre maximal d'ordinateurs a été atteint.\n");
        return;
    }

    printf("Ajout d'un nouvel ordinateur\n");
    printf("Marque : ");
    scanf("%s", ordinateurs[nombreOrdinateurs].marque);
    printf("Stock : ");
    scanf("%d", &ordinateurs[nombreOrdinateurs].stock);
    printf("Prix : ");
    scanf("%f", &ordinateurs[nombreOrdinateurs].prix);

    nombreOrdinateurs++;
    printf("L'ordinateur a été ajouté avec succès.\n");
}

void consulterDetails() {
    int index;
    printf("Numero de l'ordinateur : ");
    scanf("%d", &index);

    if (index >= 0 && index < nombreOrdinateurs) {
        printf("Détails de l'ordinateur\n");
        printf("Marque : %s\n", ordinateurs[index].marque);
        printf("Stock : %d\n", ordinateurs[index].stock);
        printf("Prix : %.2f\n", ordinateurs[index].prix);
    } else {
        printf("Numero d'ordinateur invalide.\n");
    }
}

void mettreAJourStocks() {
    int index, composant, quantite;
    printf("Numero de l'ordinateur : ");
    scanf("%d", &index);

    if (index >= 0 && index < nombreOrdinateurs) {
        printf("Composant (0: Processeur, 1: Carte graphique, 2: RAM, 3: Stockage) : ");
        scanf("%d", &composant);

        if (composant >= 0 && composant <= STOCKAGE) {
            printf("Quantite : ");
            scanf("%d", &quantite);

            if (quantite >= 0) {
                ordinateurs[index].stock += quantite;
                printf("Les stocks ont été mis à jour avec succès.\n");
            } else {
                printf("Quantite invalide.\n");
            }
        } else {
            printf("Composant invalide.\n");
        }
    } else {
        printf("Numero d'ordinateur invalide.\n");
    }
}
