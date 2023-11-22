#creation de la fonction calcule()
def calcule(num1,operator,num2):
    if operator=='+' :
        return num1+num2
    
    elif operator=='-' :
        return num1-num2
    
    elif operator=='*' :
        return num1*num2
    
    elif operator=='/' :
        return num1/num2
    
    elif operator =='%':
        return num1%num2
    
    else:
        return "le operateur n'est pas correct"
    

#Appele à la fonction calcule()
print(calcule(5, '+', 3))
print(calcule(8, '-', 4))
print(calcule(7, '*', 6))
print(calcule(10, '/', 2))
print(calcule(9, '%', 3))
print(calcule(1 , '3' , 4))