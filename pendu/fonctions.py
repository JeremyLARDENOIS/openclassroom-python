############
#Code réalisé par Jérémy LARDENOIS 
#Dans le cadre du Mooc Openclassroom
#Apprenez a programmer en python 
#Fichier de fonction
############

#tested
def mot_codé(mot_a_deviner):
    return (len(mot_a_deviner)-1)*'_ '+'_'

def afficher_mot(mot):
    for i in range(len(mot)):
        print(mot[i].upper()+' ', end="")
    print("")

def ask_name():
    print('Quel est votre nom?')
    return input()

def verifier_lettre(lettre, mot):
    for lettre_mot in mot:
        if lettre == lettre_mot:
            return True
    return False

def reveler_lettre(lettre_a_reveler, mot, mot_code):
    new_mot_code = str()
    for i in range(len(mot)):
        lettre = mot[i]
        if lettre == lettre_a_reveler:
            new_mot_code+=lettre
        else:
            new_mot_code+= mot_code[i]
    return new_mot_code

#in developpement
def ajouter_scores(scores):
    import pickle
    with open("./scores","wb") as scores:
        mon_pickler = pickle.Pickler(scores)
        mon_pickler.dump(scores)

def recuperer_scores(name):
    import pickle
    with open("scores","rb") as scores:
        scores_recupere = pickle.Unpickler(scores).load()
    score = 0
    for name_score in scores.score.keys():
        if name == name_score:
            score = score.score[name]
    print("Votre score est de",points,"points")