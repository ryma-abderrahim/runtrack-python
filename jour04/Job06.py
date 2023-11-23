#création de la list 
L=[ 1 , 2 , 3 , 4 , 5 ]

#afficher la liste L
print (L)

#échanger la première valeur et la dernière valeur de la liste à l'aide d'une variable intermédiaire
def echange(list):
    inter= list[0]
    list[0] = list[len(L)-1]
    list[len(list)-1] = inter
    return L

L=[1,2,3, 4,5]
#affiher la liste aprés l'échange
print(echange(L))