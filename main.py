


from test_base_de_donnees import manipulation_de_la_base_de_donnees
from fichier_de_travail_2 import choix_2


if __name__ == '__main__':
    resultat = False
    print("BIENVENUE")
    while resultat != True :
        manipulation_de_la_base_de_donnees()
        choix = choix_2()
        if choix == 1 :
            resultat = False
        else :
            resultat = True
            print("AU REVOIR")


