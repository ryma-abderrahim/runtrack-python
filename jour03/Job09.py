#creation de la fonction moyenne
def moyenne(n1,n2,n3):
    moyenne= ((n1+n2+n3) / 3)
    return moyenne

#Récupération des notes
print("Entrer les 3 notes")
note1=float(input("la premiere note :"))
note2=float(input("La deuxieme note :"))
note3=float(input("La troisieme note :"))

#Appel à la fonction moyenne 
moyenne_etudiant= moyenne(note1,note2,note3)

#vérification de néveau de l'étudiant 
if moyenne_etudiant < 8 :
    print("Élève devant faire des efforts")

elif moyenne_etudiant <11 :
    print("Élève moyen")

elif moyenne_etudiant <15 :
    print("Bon élève")

elif moyenne_etudiant <20:
    print("Très bon élève")

else: print("Erreur vos notes sont incorrecte")

