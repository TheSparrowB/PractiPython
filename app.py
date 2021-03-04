from flask import Flask, jsonify, request, redirect, url_for
from animal import animals

app = Flask(__name__)

@app.route('/servis/paiton/lmao')
def shout():
    return jsonify({ "mensaje": "BONK!" })


@app.route("/servis/paiton/animals", methods=['GET'])
def getAnimals():
    return jsonify(animals)


@app.route("/servis/paiton/animals/<string:name>", methods=["GET"])
def getAnimal(name):
    foundAnimals = [animal for animal in animals if animal["txt_name"].upper() == name.upper()]

    if len(foundAnimals)>0:
        return jsonify(foundAnimals[0])
    
    return jsonify({ "txt_message": "Animal not found."})


@app.route("/servis/paiton/animal/insert", methods=["POST"])
def insertAnimal():
    body = request.json

    animal = {
        "txt_name": body["txt_name"],
        "txt_race": body["txt_race"],
        "num_power": body["num_power"]
    }

    animals.append(animal)

    return jsonify({ "txt_message": "New animal added succesfully.", "animals": animals})


@app.route("/servis/paiton/animal/update", methods=["PUT"])
def updateAnimal():
    body = request.json

    animalFound = [animal for animal in animals if animal["txt_name"].upper() == body["txt_name"].upper()]

    if(len(animalFound)>0):
        animalFound[0]["txt_race"] = body["txt_race"]
        animalFound[0]["num_power"] = body["num_power"]

        return jsonify({ "txt_message": "Animal has been updated.", "animals": animals })
    else:
        return jsonify({ "txt_message": "Animal hasn't been found." })


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return redirect(url_for('shout')) 


if(__name__ == "__main__"):
    app.run(debug=True, port=5000)

