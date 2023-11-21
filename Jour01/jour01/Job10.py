#creation des variables
Montant_initial = 3000.00
Taux_rendement_annuel = 10

#Affichage de Gain Annuel en fonction de taux de rendement
Gain_Annuel = (Montant_initial * Taux_rendement_annuel)/100
print("Le gain annuel est  de : ", f"{Gain_Annuel :.2f}  \n")


#Aprés l'augmentation
#mise à jour des variables
Montant_initial += 5000
Taux_rendement_annuel +=2

#Le nouveau gain anuelle
Gain_Annuel = (Montant_initial * Taux_rendement_annuel)/100
print("Le gain annuel (aprés l'augmentation)est  de : ", f"{Gain_Annuel :.2f} \n")


#Aprés la diminuation
#Mise à jour des variables
Montant_initial -= (Montant_initial * 0.1)
Taux_rendement_annuel -= 1

#Le nouveau gain anuelle
Gain_Annuel = (Montant_initial * Taux_rendement_annuel)/100
print("Le gain annuel (aprés l'diminution)est  de : ", f"{Gain_Annuel :.2f}")

