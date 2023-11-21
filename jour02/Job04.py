Entier=int(input("Entrez un entier supérieur à zéro (N) :")) 

#verifier si le input verifier les conditions
while Entier<=0:
    print("Le nombre que vous avez saisie  n'est pas superieur à 0!!!!")
    Entier=int(input("Entrez un entier supérieur à zéro (N) :")) 
    if Entier>0 :
        break

#table de multiplication
print("Table de multiplication de ", Entier ," :")
i=1
while i<=10 :
    result= (Entier * i)
    print( Entier ," * ", i ," = ", result)
    i+=1

