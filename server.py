from flask import Flask,request,render_template,jsonify,abort
from flask_cors import CORS

import services.utilisateur as userService
import services.fiche_animal as fiche_animalService

app = Flask(__name__)
CORS(app)

@app.route("/utilisateur", methods=["POST", "GET", "PUT", "DELETE"])
def utilisateur():
    json = request.get_json()

    if(request.method == "POST") :
        response = userService.createUtilisateur(json["idName"], json["username"], json["pwd"])
        return response

    if(request.method == "GET") :
        response = userService.getUtilisateur(json["idName"])
        return response
    
    if(request.method == "PUT") :
        response = userService.updateUtilisateur(json["previousIdName"], json["idName"], json["username"], json["pwd"])
        return response

    if(request.method == "DELETE") :
        response = userService.deleteUtilisateur(json["idName"])
        return response

@app.route("/fiche_animal", methods=["POST", "GET", "PUT", "DELETE"])
def fiche_animal():
    json = request.get_json()

    if(request.method == "POST") :
        response = fiche_animalService.createFiche_animal()
        return response

    if(request.method == "GET") :
        response = fiche_animalService.getFiche_animal(json["idAnimal"])
        return response
    
    if(request.method == "PUT") :
        response = fiche_animalService.updateFiche_animal()
        return response

    if(request.method == "DELETE") :
        response = fiche_animalService.deleteFiche_animal(json["idAnimal"])
        return response
