import math
a=int(input("Entrez la longure de segment a:"))
b=int(input("Entrez la longure de segment b :"))
c=int(input("Entrez la longure de segment c :"))

#récupérer le segment par ordre
list=[ a, b , c]
list.sort()
hauteur=list[2]
segment1=list[1]
segment2=list[0]
print ("La hauteur est", hauteur)
print ("Le premier segment est ", segment1)
print ("le second segment est ", segment2)

#verifier si on peut constuire un triangle
if ((segment1 + segment2) >hauteur) :
     
     #verfier si le triangle est  équilatéral
    if ((a==b)and(b==c)and(a==c)):
         print ("On peut construire un triangle équilatéral")

        
    #verifier si le triangle est isocèle
    elif ((a==b)or(b==c)or(a==c)):

         #verfier si le triangle est rectangle
        if ((math.sqrt(segment1)) +(math.sqrt(segment2))) > (math.sqrt(hauteur)):
            print ("On peut construire un triangle isocèles et rectangulaire")
        
        else:
            print ("On peut construire un triangle isocèles mais pas rectangulaire") 
        

    #verfier si le triangle est rectangle
    elif ((math.sqrt(segment1)) +(math.sqrt(segment2))) == (math.sqrt(hauteur)):

        #verfier si le trinagle rectangle est isocèle
        if (a==b)or(b==c)or(a==c):
            print ("On peut construire un triangle  rectangulairse et isocèle")
        else:
            print("On peut construire un triangle rectangle mais pas isocèle")
    

    #sinon il s'agit d'un triangle quelconque
    else:
        print ("On peut construire un triangle , mais le triangle ne sera ni rectangle ni isocèle ni équilatéral")

#les 3segments ne peuvent pas construir un triangle
else:
    print ("Impossible de construire un triangle avec ces segments")
               
        
