#création de la fonctio nb_metres
def nb_metres(n,h):
    # Calcul de la distance parcourue par le gardien pour un aller aux toilettes
    distance = (n * h) / 100  # Conversion des cm en mètres

     # Calcul de la distance parcourue par le gardien pour un aller-retour aux toilettes
    distance_aller_retour= distance * 2 

    # Calcul de la distance parcourue par jour
    distance_par_jour = distance_aller_retour * 5 # Le gardien va aux toilettes 5 fois par jour
    
    # Calcul de la distance parcourue par semaine
    distance_par_semaine = distance_par_jour * 7  #une semaine comporte 7 jours 

    return round(distance_par_semaine, 2)

#initialisation des argument
nb_marches=int(input("Entrez le nombre de marches du phare au rez-de-chaussée :"))
hauteur_marche=float(input("Entrez la hauteur d'une marche en cm : "))

#affichage de résultat
distance=(nb_metres(nb_marches,hauteur_marche))
print("Pour", nb_marches ,"marches de",hauteur_marche,"cm, le gardien parcourt",distance,"m par semaine.")