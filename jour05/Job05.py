#creation de la fonction chiffrement_cesar
def chiffrement_cesar(message, decalage):
    message_decale = ""
    for lettre in message:

        #si le caractère est une lettre 
        if lettre.isalpha():

            #la lettre : si elle est en miniscule
            if lettre.islower():
                lettre_decale = chr((ord(lettre) - ord('a') + decalage) % 26 + ord('a'))
            
            #si elle est en majuscule
            else:
                lettre_decale = chr((ord(lettre) - ord('A') + decalage) % 26 + ord('A'))
            message_decale += lettre_decale
        
        #si le caractère ni pas une lettere en le garde 
        else:
            message_decale += lettre
    return message_decale


#initialisation de message et la clé de chiffrement
message_a_chiffrer=input("Entrze le message à chiffrer :")
cle_decalage=int(input("Entrez le décalage :"))

#appele à la fonction chiffrer
print(chiffrement_cesar(message_a_chiffrer,cle_decalage))