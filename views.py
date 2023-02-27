from flask import Blueprint, render_template

views = Blueprint(__name__, "views")

@views.route("/home")
@views.route("/")
def home():
    return render_template("index.html", name="stef")

@views.route("/game")
def game():
    