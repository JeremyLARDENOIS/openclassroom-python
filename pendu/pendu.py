############
#Code réalisé par Jérémy LARDENOIS 
#Dans le cadre du Mooc Openclassroom
#Apprenez a programmer en python
#Main
############
import fonctions
import donnee

#Main
mot_a_deviner = donnee.mot_a_deviner
mot_code = fonctions.mot_codé(mot_a_deviner)


######################
mon_fichier = open("./scores", "w")
mon_fichier.write("Ceci est joli")
mon_fichier.close()

mon_fichier = open("./scores", "r")
print(mon_fichier.read())
#fonctions.ajouter_scores({"Jeremy":50})

import os 
print(os.getcwd())


###########################


'''
name = fonctions.ask_name()
score = donnee.nb_essai_max
'''


