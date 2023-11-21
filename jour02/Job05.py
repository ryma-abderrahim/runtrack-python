i=1
while i<=100 :
    #si le nombre et un multipe de 3 et 5 
    if ((i%3)==0) and ((i%5)==0):
        print("FizzBuzz")
        
    #si le nombre est multiple de 3
    elif (i%3)==0:
        print("Fizz")

    #si le nombre est multiple de 5
    elif (i%5)==0 :
        print("Buzz")
    else:
        print(i)
        
    i+=1
    