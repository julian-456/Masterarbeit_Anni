
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("home.html")

@app.route("/test")
def test():
    return render_template("test.html")

@app.route("/kontenübersicht")
def kontenübersicht():
    return render_template("kontenübersicht.html")

@app.route("/informationen_berechtigungen")
def informationen_berechtigungen():
    return render_template("informationen_berechtigungen.html")

@app.route("/in_arbeit")
def in_arbeit():
    return render_template("in_arbeit.html")
 
@app.route("/privacycenter")
def privacycenter():
    return render_template("Privacycenter_Anni.html")

@app.route("/privacycenter_and_overview")
def privacycenter_and_overview():
    return render_template("Privacycenter_overview_Anni.html")

@app.route("/privacyoverview")
def privacyoverview():
    return render_template("Privacyoverview_Anni.html")

@app.route("/akt_außerhalb_meta")
def akt_außerhalb_meta():
    return render_template("akt_außerhalb_meta.html")

@app.route("/künftige_aktivitäten")
def künftige_aktivitäten():
    return render_template("künftige_aktivitäten.html")

@app.route("/wrong_site")
def wrong_site():
    return render_template("wrong_site_1.html")

@app.route("/wrong_site2")
def wrong_site2():
    return render_template("wrong_site_2.html")

@app.route("/wrong_site3")
def wrong_site3():
    return render_template("wrong_site_3.html")

@app.route("/wrong_site4")
def wrong_site4():
    return render_template("wrong_site_4.html")

@app.route("/wrong_site5")
def wrong_site5():
    return render_template("wrong_site_5.html")

@app.route("/privacy_center")
def privacy_center():
    return render_template("privacy_center.html")

if __name__ == '__main__':
    app.run()