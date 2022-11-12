from flask import Flask, render_template
from flask_frozen import Freezer

app = Flask(__name__)

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
    
@app.route("/resume")
def resume():
    return render_template("resume.html")