from database import connectToDB

def create(idName, idAnimal, commentaire) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # Créer le commentaire
    sql = f'''
        INSERT INTO commentaires VALUES 
        (
            NULL,
            "{idName}",
            {idAnimal},
            "{commentaire}"
        )
    '''
    myCursor.execute(sql)
    myDb.commit()

    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

def get(idCommentaire) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # On récupère les informations de l'animal
    sql = f'''SELECT * FROM commentaires WHERE idCommentaire = {idCommentaire}'''
    myCursor.execute(sql)
    data = myCursor.fetchall()

    if(data):
        response = {
            "commentaire": {
                "idCommentaire" : data[0][0],
                "idName" : data[0][1],
                "idAnimal" : data[0][2],
                "commentaire" : data[0][3],
            },
            "code" : 200
        }
    
    else :
        response = {
            "message" : "Commentaire non trouvé",
            "code" : 404
        }

    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

    return response

def update(idCommentaire, commentaire) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # Mise à jour de la fiche animal
    sql = f'''
        UPDATE commentaires SET 
        commentaire = "{commentaire}"
        WHERE idCommentaire = {idCommentaire}
    '''
    myCursor.execute(sql)
    myDb.commit()

    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

def delete(idCommentaire) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # Suppression de la fiche animal
    sql = f'''DELETE FROM commentaires WHERE idCommentaire = {idCommentaire}'''
    myCursor.execute(sql)
    myDb.commit()

    response = {
        "message" : "Commentaire supprimée",
        "code" : 200
    }

    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

    return response