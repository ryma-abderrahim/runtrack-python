
#Récuperer ma chaine de caractère depuis le terminal 
ma_chaine= input("Veulliez saisire une chaine de caractère :")

#vérification de l'existance de la chaine 
if  len(ma_chaine)==0 :
    print ("La chaine est vide ! ")
    ma_chaine=input("Veulliez bien saisir une chaine de caractère : ")
else:
    if 'e' in ma_chaine:
        print("la chaine de caractère ' ", ma_chaine ," ' contient le caractère 'e'")
    else:
         print("la chaine de caractère ' ", ma_chaine ," ' ne contient pas de caractère 'e'")