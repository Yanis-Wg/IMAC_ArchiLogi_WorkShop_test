from database import connectToDB

def create(idName, idAnimal,note) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # Créer la note
    sql = f'''
        INSERT INTO notes VALUES 
        (
            NULL,
            "{idName}",
            {idAnimal},
            {note}
        )
    '''
    myCursor.execute(sql)
    myDb.commit()

    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

def get(idName, idAnimal) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # On récupère les informations de la note
    sql = f'''SELECT idNote, idName, idAnimal, note FROM notes WHERE idName = "{idName}" AND idAnimal ={idAnimal}'''
    myCursor.execute(sql)
    data = myCursor.fetchall()

    if(data):
        response = {
            "note": {
                "idNote" : data[0][0],
                "idName" : data[0][1],
                "idAnimal" : data[0][2],
                "note" : data[0][3],
            },
            "code" : 200
        }
    
    else :
        response = {
            "message" : "Note non trouvée",
            "code" : 404
        }

    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

    return response

def update(idNote, idName, idAnimal,note) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # Mise à jour de la note
    sql = f'''
        UPDATE notes SET 
        idNote = "{idNote}",
        idName = "{idName}",
        idAnimal = "{idAnimal}",
        note = {note}
        WHERE idNote = "{idNote}"
    '''
    myCursor.execute(sql)
    myDb.commit()

    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

def delete(idNote) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # Suppression de la note
    sql = f'''DELETE FROM notes WHERE idNote = "{idNote}"'''
    myCursor.execute(sql)
    myDb.commit()

    response = {
        "message" : "Note supprimée",
        "code" : 200
    }

    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

    return response