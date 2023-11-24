#crétion de la fonction traverse_diagonale
def traverse_diagonale(n):
    print("+" + "-" * (n+1) + "+")
    for i in range(n+1):
        print("|"+ ("#" *(n-i) ) + " " +("#" * i) + "|")
    print("+" + "-" * (n+1) + "+")


#initialisation de input n
n = int(input("Entrer le nombre de cases de la diagonale :"))


#appel à la fonction traverse_diagonale
traverse_diagonale(n)
         
              