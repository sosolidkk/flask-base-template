from flask import render_template, flash
from app import app


@app.route("/")
def index():
    return render_template("index.html", title="Index page")


@app.route("/sign-in")
def sign_in():
    flash("Error login", "danger")
    flash("Success login", "success")
    flash("Notification login", "primary")
    return render_template("sign_in.html", title="Sign in page")


@app.route("/sign-up")
def sign_up():
    return render_template("sign_up.html", title="Sign up page")
