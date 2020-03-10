from flask import render_template, flash
from app import app


@app.route("/")
def index():
    return render_template("index.html", title="Index page")


@app.route("/sign-in")
def sign_in():
    flash("Error sign in", "danger")
    flash("Success sign in", "success")
    flash("Message sign in", "primary")

    return render_template("sign_in.html", title="Sign in page")


@app.route("/sign-up")
def sign_up():
    flash("Error sign up", "danger")
    flash("Success sign up", "success")
    flash("Message sign up", "primary")

    return render_template("sign_up.html", title="Sign up page")
