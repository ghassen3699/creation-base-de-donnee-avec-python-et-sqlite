



# le menu de l'application
#########################################################################################
def menu_application() :
    liste_choix = [1,2,3,4,5,6,7,8]                      # initialiser d'une liste pour les choix de la menu de l'application
    global choix                                 # creation d'un objet global qui s'appel choix
    resultat = False                         # initialisation d'un objet pour tester le choix de l'utilisateur
    # le menu de l'application
    print("1) AJOUTER CLIENT")
    print("2) AJOUTER VENDEUR")
    print("3) SUPPRIMER CLIENT")
    print("4) SUPPRIMER VENDEUR")
    print("5) METTRE A JOUR CLIENT")
    print("6) METTRE A JOUR VENDEUR")
    print("7) AFFICHER LA LISTE DES CLIENTS")
    print("8) AFFICHER LA LISTE DES VENDEURS")

    while resultat != True :                          # boucle while pour eviter les erreurs de l'utilisation
        while True :
            try:                                 # la vrai condition
                choix = int(input("---> "))                    # lire le choix de l'utilisateur
                break
            except ValueError :              # la fausse condition
                print("ERREUR !!! ENTRER UN ENTIER DE 1 A 8")
        if choix in liste_choix :                                     # tester si le choix appartient au menu ou non
            resultat = True                                     # si oui le teste va prendre TRUE

    return choix               # retourner le choix
###########################################################################################








# lire le nom de l'utilisateur
###########################################################################################
def remplissage_nom () :
    print("LE NOM : ")
    nom = input("---> ")
    return nom
###########################################################################################







# lire le prenom de l'utilisateur
###########################################################################################
def remplissage_prenom () :
    print("PRENOM : ")
    prenom = input("---> ")
    return prenom
###########################################################################################







# lire l'age de l'utilisateur
###########################################################################################
def remplissage_age () :
    print("L'AGE : ")
    while True :
        try:
            age = int(input("---> "))
            break
        except ValueError :
            print("ERREUR !!! ENTRER UN ENTIER ")

    return age
###########################################################################################






# lire l'e-mail de l'utilisateur
###########################################################################################
def remplissage_mail () :
    liste = ['@', '.']
    resultat = False
    compteur = 0
    print("ADRESSE E-MAIL : ")
    while resultat != True:
        email = input("---> ")
        for i in email:
            if i in liste:
                compteur += 1
        if compteur >= 2:
            resultat = True

    return email
############################################################################################






# lire le numero telephonique de l'utilisateur
###########################################################################################
def remplissage_numero () :
    test = False
    print("LE NUMERO TEL : ")
    while test != True :
        numero_tel = input("---> ")
        if len(numero_tel) == 8 :
            test = True
    return numero_tel
############################################################################################






# lire cin de l'utilisateur
############################################################################################
def remplissage_cin () :
    test = False
    print("CIN : ")
    while test != True :
        cin = input("---> ")
        if len(cin) == 8 :
            test = True
    return cin
#############################################################################################





# lire la marque de l'utilisateur
#############################################################################################
def remplissage_nom_boutique () :
    print("LE NOM DE VOTRE MARQUE  : ")
    marque = input("---> ")
    return marque
##############################################################################################




# lire le deuxieme choix
##############################################################################################
def choix_2 () :
    liste_choix = [1,2]
    test = False
    print("1) CONTINUE ")
    print("2) EXIT")
    while test == False :
        while True :
            try:
                choix = int(input("---> "))
                break
            except ValueError :
                print("ERREUR !!! ENTRER UN ENTIER ")
        if choix in liste_choix :
            test = True
    return choix
###############################################################################################