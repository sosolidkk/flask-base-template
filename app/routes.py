from app import app
from app import db
from app.models import User
from app.forms import SignInForm, SignUpForm
from app.models import User
from flask import flash, render_template, redirect, request, url_for
from flask_login import current_user, login_user, logout_user, login_required
from sqlalchemy.exc import SQLAlchemyError


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", title="Index page")


@app.route("/sign-in", methods=["GET", "POST"])
def sign_in():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))

    form = SignInForm(request.form)

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password", "danger")
            return redirect(url_for("sign_in"))

        login_user(user, remember=form.remember_me.data)
        flash(f"User {current_user.username} logged in successful", "success")
        return redirect(url_for("dashboard"))

    return render_template("sign_in.html", title="Sign in page", form=form)


@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    form = SignUpForm(request.form)

    if form.validate_on_submit():
        user = User(
            username=form.username.data, email=form.email.data, role=form.user_role.data
        )
        user.set_password(form.password.data)

        try:
            db.session.add(user)
            db.session.commit()

            flash(f"User {form.username.data} created successful", "success")
            return redirect(url_for("sign_in"))
        except SQLAlchemyError as err:
            db.session.rollback()

            flash(f"{err}", "danger")
            return redirect(url_for("sign_up"))
    return render_template("sign_up.html", title="Sign up page", form=form)


@app.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    user = User.query.filter_by(username=current_user.username).first()
    return render_template("dashboard.html", title="Dashboard page", user=user)


@app.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))
