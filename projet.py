# ECRIRE UN PROGRAMME QUI PERMET DE DEMANDER A L'UTILISATEUR D'ENTRER UN NOMBRE COMPRIS ENTRE 1 ET 4 
def demander_utilisateur(min,max):
    print("bienvenue sur le programme ")
    reponse = input("entrez un nombre compris entre "+str(min)+" et "+str(max)+":")
    try:
        reponse_int = int(reponse)
        if not min<=reponse_int<=max:
            print("ERREUR:veuillez saisir un nombre compris entre" ,min, "et",max)
            return demander_utilisateur(min,max)
        return reponse_int
    except:
        print("vous devez rentrez un nombre") 
        return demander_utilisateur(min,max)
choix = demander_utilisateur(1,4)    

print("le choix de l'utilisateur est :" ,choix)    