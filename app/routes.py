from app import app
from app.models import User
from app.forms import SignInForm, SignUpForm
from flask import flash, render_template, redirect, request, url_for
from flask_login import current_user, login_user, logout_user, login_required


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", title="Index page")


@app.route("/sign-in", methods=["GET", "POST"])
def sign_in():
    form = SignInForm(request.form)

    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
        print(form.remember_me.data)

        flash("Need to implement DB to perform sign in", "primary")
        return redirect(url_for("sign_in"))

    return render_template("sign_in.html", title="Sign in page", form=form)


@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    form = SignUpForm(request.form)

    if form.validate_on_submit():
        print(form.username.data)
        print(form.email.data)
        print(form.password.data)
        print(form.password_confirmation.data)
        print(form.user_role.data)

        flash("Need to implement DB to perform sign up", "primary")
        return redirect(url_for("sign_up"))
    return render_template("sign_up.html", title="Sign up page", form=form)


@app.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))
