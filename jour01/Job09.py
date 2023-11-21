#création des variable (nom, prix unitaire , quantité en stock)
Nom =" SmartPhone "
Prix_unitaire = 200.00
Quantite_en_stock = 560


#Afficher les informations du produit en console
print("Informations sur le produit:")
print("Nom: ", Nom) 
print("Prix unitaire: ", Prix_unitaire ) 
print("Quantité en stock: ", Quantite_en_stock ,"\n")



#Ajouter des produits en stock
Quantite_achetee = int(input("Combien de produits souhaitez-vous acheter ? ")) 
Quantite_en_stock -= Quantite_achetee

#Augmentation de prix de prpduit
Prix_unitaire *=1.1

#Afficher les informations du produit en console
print("\nInformations sur le produit (Mise à jour):")
print("Nom: ", Nom) 
print("Prix unitaire: ", f"{Prix_unitaire:.2f}" ) 
print("Quantité en stock: ", Quantite_en_stock)
