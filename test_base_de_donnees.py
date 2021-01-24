

def manipulation_de_la_base_de_donnees () :

    # importer les modules de travail
    import sqlite3
    from fichier_de_travail_2 import menu_application
    from fichier_de_travail_2 import remplissage_cin
    from fichier_de_travail_2 import remplissage_nom
    from fichier_de_travail_2 import remplissage_prenom
    from fichier_de_travail_2 import remplissage_age
    from fichier_de_travail_2 import remplissage_numero
    from fichier_de_travail_2 import remplissage_mail
    from fichier_de_travail_2 import remplissage_nom_boutique



    # creation d'une base de donnees pour enregistrer les donnees des vendeurs
    fichier_vendeur = 'vendeur.db'     # initialiser le nom de fichier db pour le tableau vendeur
    fichier_client = 'client.db'       # intialiser le nom de fichier db pour le tableau client


    # creation d'une base de donnees pour enregistrer les donnees des vendeurs
    try :
        vendeur = sqlite3.connect("vendeur.db")
        vendeur_curseur = vendeur.cursor()
        vendeur_curseur.execute("""create table vendeur( 
                cin text primary key ,
                nom text ,
                prenom text ,
                age integer ,
                email text ,
                numero text ,
                boutique text);""")
        vendeur.commit()
    except sqlite3.OperationalError :
        print("LA TABLE VENDEUR EXISTE DEJA ")
    finally:
        vendeur.close()


    # creation d'une base de donnees pour enregistrer les donnees des clients
    try :
        client = sqlite3.connect("client.db")
        client_curseur = client.cursor()
        client_curseur.execute(""" create table client(
                cin text primary key ,
                nom text ,
                prenom text ,
                age integer ,
                email text ,
                numero text);""")
        client.commit()
    except sqlite3.OperationalError :
        print("LA TABLE CLIENT EXISTE DEJA ")
    finally:
        client.close()


    # lire le choix de l'utilisateur
    choix_utilisateur = menu_application()



    ######################################### ajouter client ###########################################
    if choix_utilisateur == 1 :
        cin = remplissage_cin()     # lire la cin du client
        nom = remplissage_nom()      # lire le nom du client
        prenom = remplissage_prenom()    # lire prenom du client
        age = remplissage_age()          # lire l'age du client
        email = remplissage_mail()          # lire l'mail du client
        numero = remplissage_numero()        # lire le numero tel du client
        try:
            conn = sqlite3.connect(fichier_client)
            cur = conn.cursor()
            print("CONNEXION RÉUSSIE A SQLITE")
            sql = "insert into client (cin,nom,prenom,age,email,numero) values (?,?,?,?,?,?)"
            value = (cin,nom,prenom,age,email,numero)
            cur.execute(sql,value)
            conn.commit()
            cur.close()
            conn.close()
            print("ENREGISTREMENT TERMINER ")

        except sqlite3.Error :
            print("ERREUR !!! INSERTION DANS LA TABLE CLIENT ")



    ######################################### ajouter vendeur ###########################################
    elif choix_utilisateur == 2 :
        cin = remplissage_cin()  # lire la cin du vendeur
        nom = remplissage_nom()  # lire le nom du vendeur
        prenom = remplissage_prenom()  # lire prenom du vendeur
        age = remplissage_age()  # lire l'age du vendeur
        email = remplissage_mail()  # lire l'mail du vendeur
        numero = remplissage_numero()  # lire le numero tel du vendeur
        boutique = remplissage_nom_boutique() # lire le nom de la marque du vendeur

        try:
            conn = sqlite3.connect(fichier_vendeur)
            cur = conn.cursor()
            print("CONNEXION RÉUSSIE A SQLITE")

            sql = "insert into vendeur (cin,nom,prenom,age,email,numero,boutique) values (?,?,?,?,?,?,?)"
            value = (cin,nom,prenom,age,email,numero,boutique)
            cur.execute(sql,value)
            conn.commit()
            print("ENREGIQTREMENT TERMINER ")
            cur.close()
            conn.close()
        except sqlite3.Error :
            print("ERREUR !!! INSERTION DANS LA TABLE VENDEUR ")



    ######################################### delete client ###########################################
    elif choix_utilisateur == 3 :
        try:
            cin = remplissage_cin()
            conn = sqlite3.connect(fichier_client)
            cur = conn.cursor()
            print("CONNEXION RÉUSSIE A SQLITE")

            sql = " DELETE FROM client WHERE cin = ?"
            cur.execute(sql,(cin, ))
            conn.commit()
            print("ENREGISTREMENTS SUPPRIMES AVEC SUCCES ")

            cur.close()
            conn.close()
        except sqlite3.Error :
            print("ERREUR LORS DU SUPPRESSION DANS LA TABLE CLIENT ")



    ######################################### delete vendeur  ###########################################
    elif choix_utilisateur == 4 :
        try :
            cin = remplissage_cin()
            conn = sqlite3.connect(fichier_vendeur)
            cur = conn.cursor()
            print("CONNEXION RÉUSSIE A SQLITE")

            sql = "delete from vendeur where cin = ?"
            cur.execute(sql,(cin, ))
            conn.commit()
            print("ENREGISTREMENTS SUPPRIMES AVEC SUCCÉS ")
            cur.close()
            conn.close()
        except sqlite3.Error :
            print("ERREUR LORS DU SUPPRESSION DANS LA TABLE VENDEUR ")



    ######################################### modifier client ###########################################
    elif choix_utilisateur == 5 :
        test = False
        liste_menu = [1,2,3,4,5]
        print("ENTRER VOTRE MODIFICATION : ")
        print("1) NOM")
        print("2) PRENOM")
        print("3) AGE")
        print("4) EMAIL")
        print("5) NUMERO TEL")
        while test != True :
            while True :
                try:
                    choix = int(input("---> "))
                    break
                except ValueError :
                    print("ERREUR ENTRER UN ENTIER ")
            if choix in liste_menu :
                test = True

        ########### modifier le nom de client #######################
        if choix == 1 :
            try:
                cin = remplissage_cin()
                nom = remplissage_nom()
                conn = sqlite3.connect(fichier_client)
                cur = conn.cursor()
                print("CONNEXION RÉUSSIE A SQLITE")
                sql = "UPDATE client SET nom = ? WHERE cin = ? "
                value = (nom,cin)
                cur.execute(sql , value)
                conn.commit()
                print("ENREGISTREMENT MIS A JOUR AVEC SUCCES ")
                cur.close()
                conn.close()
            except sqlite3.Error :
                print("ERREUR !!! LORS DU MISE A JOUR DANS LA TABLE")

        ########### modifier le prenom de client #######################
        elif choix == 2 :
            try:
                cin = remplissage_cin()
                prenom = remplissage_prenom()
                conn = sqlite3.connect(fichier_client)
                cur = conn.cursor()
                print("CONNEXION RÉUSSIE A SQLITE")
                sql = "UPDATE client SET prenom = ? WHERE cin = ? "
                value = (prenom,cin)
                cur.execute(sql, value)
                conn.commit()
                print("ENREGISTREMENT MIS A JOUR AVEC SUCCES")
                cur.close()
                conn.close()
            except sqlite3.Error:
                print("ERREUR !!! LORS DU MISE A JOUR DANS LA TABLE")

        ########### modifier l'age de client #######################
        elif choix == 3 :
            try:
                cin = remplissage_cin()
                age = remplissage_age()

                conn = sqlite3.connect(fichier_client)
                cur = conn.cursor()
                print("CONNEXION REUSSIE A SQLITE")
                sql = "update client set age = ? where cin = ? "
                value = (age,cin)
                cur.execute(sql,value)
                conn.commit()
                print("ENREGISTREMENT MIS A JOUR AVEC SUCCES ")
                cur.close()
                conn.close()
            except sqlite3.Error :
                print("ERREUR !!! LORS DU MIS A JOUR DANS LA TABLE ")

        ########### modifier e-mail' de client #######################
        elif choix == 4 :
            try:
                cin = remplissage_cin()
                email = remplissage_mail()

                conn = sqlite3.connect(fichier_client)
                cur = conn.cursor()
                print("CONNEXION REUSSIE A SQLITE")
                sql = "update client set email = ? where cin = ? "
                value = (email,cin)
                cur.execute(sql,value)
                conn.commit()
                print("ENREGISTREMENT MIS A JOUR AVEC SUCCES ")
                cur.close()
                conn.close()
            except sqlite3.Error :
                print("ERREUR LORS DU MIS A JOUR DANS LA TABLE ")

        ########### modifier le numero de client #######################
        elif choix == 5 :
            try:
                cin = remplissage_cin()
                numero = remplissage_numero()

                conn = sqlite3.connect(fichier_client)
                cur = conn.cursor()
                print("CONNEXION REUSSIE A SQLITE")
                sql = "update client set numero = ? where cin = ? "
                value = (numero,cin)
                cur.execute(sql,value)
                conn.commit()
                print("ENREGISTREMENT MIS A JOUR AVEC SUCCES ")
                cur.close()
                conn.close()
            except sqlite3.Error :
                print("ERREUR LORS DU MIS A JOUR DANS LA TABLE ")



    ######################################### modifier vendeur ###########################################
    elif choix_utilisateur == 6 :
        test = False
        liste_menu = [1, 2, 3, 4, 5 ,6]
        print("ENTRER VOTRE MODIFICATION : ")
        print("1) NOM")
        print("2) PRENOM")
        print("3) AGE")
        print("4) EMAIL")
        print("5) NUMERO TEL")
        print("6) NOM DE LA MARQUE")
        while test != True:
            while True:
                try:
                    choix = int(input("---> "))
                    break
                except ValueError:
                    print("ERREUR ENTRER UN ENTIER ")
            if choix in liste_menu:
                test = True


        ########### modifier le nom du vendeur #######################
        if choix == 1:
            try:
                cin = remplissage_cin()
                nom = remplissage_nom()

                conn = sqlite3.connect(fichier_vendeur)
                cur = conn.cursor()
                print("CONNEXION REUSSIE A SQLITE")
                sql = "update vendeur set nom = ? where cin = ?"
                value = (nom,cin)
                cur.execute(sql,value)
                conn.commit()
                print("ENREGISTREMENT MIS A JOUR AVEC SUCCES")
                cur.close()
                conn.close()
            except sqlite3.Error :
                print("ERREUR !!! LORS DE MIS A JOUR DANS LA TABLE ")


        ########### modifier le prenom du vendeur #######################
        elif choix == 2:
            try:
                cin = remplissage_cin()
                prenom = remplissage_prenom()

                conn = sqlite3.connect(fichier_vendeur)
                cur = conn.cursor()
                print("CONNEXION RÉUSSIE A SQLITE")
                sql = "update vendeur set prenom = ? where cin = ? "
                value = (prenom, cin)
                cur.execute(sql, value)
                conn.commit()
                print("ENREGISTREMENT MIS A JOUR AVEC SUCCES")
                cur.close()
                conn.close()
            except sqlite3.Error:
                print("ERREUR !!! LORS DU MISE A JOUR DANS LA TABLE")

        ########### modifier l'age du vendeur #######################
        elif choix == 3:
            try:
                cin = remplissage_cin()
                age = remplissage_age()

                conn = sqlite3.connect(fichier_vendeur)
                cur = conn.cursor()
                print("CONNEXION REUSSIE A SQLITE")
                sql = "update vendeur set age = ? where cin = ? "
                value = (age, cin)
                cur.execute(sql, value)
                conn.commit()
                print("ENREGISTREMENT MIS A JOUR AVEC SUCCES ")
                cur.close()
                conn.close()
            except sqlite3.Error:
                print("ERREUR !!! LORS DU MIS A JOUR DANS LA TABLE ")

        ########### modifier e-mail' du vendeur #######################
        elif choix == 4:
            try:
                cin = remplissage_cin()
                email = remplissage_mail()

                conn = sqlite3.connect(fichier_client)
                cur = conn.cursor()
                print("CONNEXION REUSSIE A SQLITE")
                sql = "update client set email = ? where cin = ? "
                value = (email, cin)
                cur.execute(sql, value)
                conn.commit()
                print("ENREGISTREMENT MIS A JOUR AVEC SUCCES ")
                cur.close()
                conn.close()
            except sqlite3.Error:
                print("ERREUR LORS DU MIS A JOUR DANS LA TABLE ")

        ########### modifier le numero du vendeur #######################
        elif choix == 5:
            try:
                cin = remplissage_cin()
                numero = remplissage_numero()

                conn = sqlite3.connect(fichier_vendeur)
                cur = conn.cursor()
                print("CONNEXION REUSSIE A SQLITE")
                sql = "update vendeur set numero = ? where cin = ? "
                value = (numero, cin)
                cur.execute(sql, value)
                conn.commit()
                print("ENREGISTREMENT MIS A JOUR AVEC SUCCES ")
                cur.close()
                conn.close()
            except sqlite3.Error:
                print("ERREUR LORS DU MIS A JOUR DANS LA TABLE ")

        ########### modifier le numero de client #######################
        elif choix == 6 :
            try:
                cin = remplissage_cin()
                marque = remplissage_nom_boutique()

                conn = sqlite3.connect(fichier_vendeur)
                cur = conn.cursor()
                print("CONNEXION REUSSIE A SQLITE")
                sql = "update vendeur set boutique = ? where cin = ? "
                value = (marque,cin)
                cur.execute(sql,value)
                conn.commit()
                print("ENREGISTREMENT MIS A JOUR AVEC SUCCES ")
                cur.close()
                conn.close()
            except sqlite3.Error:
                print("ERREUR LORS DU MIS A JOUR DANS LA TABLE ")


    ######################################### afficher les clients ###########################################
    elif choix_utilisateur == 7 :
        try:
            conn = sqlite3.connect(fichier_client)
            cur = conn.cursor()
            all = cur.execute(''' select * from client ;''')
            for c in all :
                print(c)
        except sqlite3.Error :
            print("ERREUR D'AFFICHER LA TABLE CLIENT")


    ######################################### afficher les vendeurs ###########################################
    elif choix_utilisateur == 8 :
        try:
            conn = sqlite3.connect(fichier_vendeur)
            cur = conn.cursor()
            all = cur.execute(''' select * from vendeur ;''')
            for v in all :
                print(v)
        except sqlite3.Error :
            print("ERREUR D'AFFICHER LA TABLE VENDEURS ")


def extraction_fichier_csv() :
    try:
        conn = sqlite3.connect(fichier_client)
        cur = conn.cursor()
        cur.execute("SELECT * FROM fichier_client")
        header = [row[0] for row in cur.description]
        rows = cur.fetchall()
        f = open('fichier_client.csv','w')
        f.write(','.join(header)+'\n')
        for row in rows :
            f.write(','.join(str(r) for r in row) + '\n')
        f.close()
        cur.close()
        conn.close()
    except FileExistsError or sqlite.Error :
        print("ERREUR !!! ")

    try:
        conn = sqlite3.connect(fichier_vendeur)
        cur = conn.cursor()
        cur.execute("SELECT * FROM fichier_vendeur")
        header = [row[0] for row in cur.description]
        rows = cur.fetchall()
        f = open('fichier_vendeur.csv','w')
        f.write(','.join(header)+'\n')
        for row in rows :
            f.write(','.join(str(r) for r in row) + '\n')
        f.close()
        cur.close()
        conn.close()
    except FileExistsError or sqlite.Error :
        print("ERREUR !!! ")

