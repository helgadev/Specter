from flask import Flask, jsonify
from flask import render_template
from flask_cors import CORS, cross_origin
from mongo_db_script import MongoDB
#from . import app

app = Flask(__name__)
IP = '0.0.0.0'
PORT = 3333
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

mdb = MongoDB()

def prepare_data(coursor):
    for i, item in enumerate (coursor):
        del item ["_id"]
        coursor [i] = item
    return jsonify (coursor)

@app.route("/classic/")
@cross_origin()
def classic():
    # return render_template("classic.html")
    coursor = list (mdb.classic_collection.find({}))
    return prepare_data(coursor)

@app.route("/mystic/")
@cross_origin()
def mystic():
    # return render_template("mystic.html")
    coursor = list (mdb.mystic_collection.find({}))
    return prepare_data(coursor)

@app.route("/fantasy/")
@cross_origin()
def fantasy():
    # return render_template("fantasy.html")
    coursor = list (mdb.fantasy_collection.find({}))
    return prepare_data(coursor)

@app.route("/romance/")
@cross_origin()
def romance():
    # return render_template("romance.html")
    coursor = list (mdb.romance_collection.find({}))
    return prepare_data(coursor)

@app.route("/detectiv/")
@cross_origin()
def detectiv():
    # return render_template("detectiv.html")
    coursor = list (mdb.detectiv_collection.find({}))
    return prepare_data(coursor)

@app.route("/kids/")
@cross_origin()
def kids():
    # return render_template("kids.html")
    coursor = list (mdb.kids_collection.find({}))
    return prepare_data(coursor)

if __name__== '__main__':
    app.run(IP, port=PORT, debug=True)
