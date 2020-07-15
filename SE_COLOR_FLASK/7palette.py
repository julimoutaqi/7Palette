
# flask importieren
from flask import Flask, render_template, redirect , url_for, request
import requests, json, os

#  databse Sachen importieren
import sqlite3 as sql

PEOPLE_FOLDER = os.path.join('static', 'images')

# Flask App ...
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

@app.route('/')

# two decorators, same function

# Home Seite 
@app.route('/home')
def home():
    # Logo aus dem IMG folder bekommen
    logoUrl = os.path.join(app.config['UPLOAD_FOLDER'], 'logo.png')
    return render_template('home.html', logoUrl = logoUrl)

@app.route('/about')
def about():
    return render_template('about.html')

# Emotions Seite mit Suche als POST Methode und als GET Methode das Standart layout mit 9 grauen DIVs
@app.route("/emotions", methods=["GET","POST"])
def emotions():
    # lies die Farben aus der Datenbank
    if request.method == "POST":
       
        inputText = request.form['searchInput']
        
        # versucht die Farben anhand des Inputs aus der Datenbank zu finden
        # wenn es die Emotion(input) nicht gibt kommt kein Error sondern wird zur standart Seite geführt
        try:
            # mit der Datenbank verbinden ohhhh maan
            con = sql.connect("colors.db")
            # variable für Db erstellen
            cur = con.cursor()
            # die Anfrgae mit dem eingegebenen Namen erstellen
            query = "SELECT COLORS FROM colors WHERE EMOTIONS= '{}'".format(inputText)
            # anfrage an Datebank machen
            cur.execute(query )
            # speichern von dem Rückgabewert in "data" variable
            data = cur.fetchall(); 
            # für jede farbe in der 
            for colors in data[0]:
                colorlist = colors.split(",")
                
            # return processed_text
            return render_template("emotions.html", colors=colorlist)
        except:
            return render_template("emotions.html", colors=["lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey"] )




    else:
        # bei dem Laden der Seite ohne auf den Button geklickt zu haben wird die standart Seite geladen (GET-Methode)
        return render_template("emotions.html", colors=["lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey"] )


# Flask Appn starten (komisch)
if __name__ == '__main__':
    app.run(debug=True)


