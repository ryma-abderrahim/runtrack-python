#création de la fonction multiple3 
def multiple3 (list):
    count =0
    for i in list:
        if i % 3 == 0:
            count +=1
    return count

#initialisation de la list 
L=[8 , 24 , 48 , 2 , 16 ]

#compter le nombre de multiple de la liste  avec la fonction multiple3
print(multiple3(L))