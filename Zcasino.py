############
#Code réalisé par Jérémy LARDENOIS 
#Dans le cadre du Mooc Openclassroom
#Apprenez a programmer en python
############
import random
dollar = 50
score = 0

while (dollar > 0):
    print("Vous avez "+str(dollar)+" $ \nCombien voulez vous miser ?")
    mise = int(input())
    
    if (mise <= dollar):
        mise_valable = True
    else :
        print("Vous ne pouvez pas miser plus que ce que vous possédez !\n")
        mise_valable = False

    if mise_valable:
        numero_valable = False
        while not numero_valable:
            print("Sur quel numéro voulez-vous misez?")
            numero_choisi = int(input())
            if ((0 > numero_choisi) or (numero_choisi > 49)):
                print("Vous devez rentrer un nombre entre 0 et 49\n")
            else:
                numero_valable = True
    
        if ((0 <= numero_choisi) and (numero_choisi <= 49)):
            numero_gagnant = random.randint(0,49)
            print ("Le numéro gagnant est ", numero_gagnant )
            
            if (numero_gagnant == numero_choisi):
                dollar += 3*mise
                score += 3*mise
                print ("BON NUMERO !\nVous gagnez donc",3*mise,"$\n")
            elif (numero_choisi%2==numero_gagnant%2):
                dollar += mise//2
                score += mise//2
                print ("MEME COULEUR !\nVous gagnez donc",mise//2,"$\n")
            else:
                dollar -= mise
                print ("Vous perdez donc",mise,"$\n")
    
    if (dollar <= 0):
         print ("Vous avez perdu !\nScore = ",score)