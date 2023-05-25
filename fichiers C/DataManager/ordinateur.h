#ifndef ORDINATEUR_H
#define ORDINATEUR_H

typedef struct {
    char marque[20];
    int stock;
    float prix;
    float prixTotal;
} Ordinateur;

enum Composant {
    PROCESSEUR,
    CARTE_GRAPHIQUE,
    RAM,
    STOCKAGE
};

void ajouterOrdinateur();
void consulterDetails();
void mettreAJourStocks();

#endif
