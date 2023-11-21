for i in range(1, 1001):

    #un nombre premier est supérieur à 1
    if i > 1:

        for j in range(2 , i):
            
            #si le nombre est divisible par un autre nombre que lui-même et 1, il n'est pas premier
            if (i % j) == 0 :
                break

        #si aucune division sans reste n'a été trouvée, le nombre est premier
        else:    
            print(i)
