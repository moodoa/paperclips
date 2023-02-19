from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///paperclips.db"
db = SQLAlchemy(app)


class Clipsdb(db.Model):
    __tablename__ = "clips"
    id = db.Column(db.Integer, primary_key=True)
    clips = db.Column(db.String(30), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    messages = db.Column(db.String(100), nullable=False)
    datetime = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return "<clips %r>" % self.name


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=["POST", "GET"])
def submit():
    if request.method == "POST":
        clip = request.form["clip"]
        gender = request.form["gender"]
        message = request.form["message"]
        new_clip = Clipsdb(clips=clip, gender=gender, messages=message)
        try:
            db.session.add(new_clip)
            db.session.commit()
            return render_template("index.html")
        except:
            pass
    return render_template("submit.html")


@app.route("/find", methods=["POST", "GET"])
def find():
    if request.method == "POST":
        clip = request.form["clip"]
        wanted_gender = request.form["wanted_gender"]
        infos = (
            Clipsdb.query.filter_by(clips=clip, gender=wanted_gender)
            .order_by(Clipsdb.datetime.desc())
            .all()
        )
        return render_template("find.html", infos=infos)
    else:
        return render_template("find.html")


if __name__ == "__main__":
    app.run(debug=True)
