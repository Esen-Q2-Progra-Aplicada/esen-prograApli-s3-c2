from flask import Flask, request, render_template, session, redirect, url_for
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "una_llave_secreta_2021_esen"
app.permanent_session_lifetime = timedelta(minutes=1)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        session["cart"] = []
        return render_template("index.html")
    elif request.method == "POST":
        # obtenemos la informacion del formulario
        user = request.form["username"]
        passwd = request.form["password"]

        # crear la sesion con valores especificos
        session["login_user"] = user
        session["login_passwd"] = passwd

        return redirect(url_for("dashboard"))
    else:
        return "<h1>error</h1>"


@app.route("/dashboard")
def dashboard():
    user = ""
    password = ""
    cart = []
    modify = False
    if session.get("login_user") is not None:
        if session.get("login_user") != "":
            user = session.get("login_user")
            password = session.get("login_passwd")

            session["cart"].append("bike")
            session.modified = True
            cart = session.get("cart")
            modify = session.modified
    return render_template(
        "dashboard.html", user=user, password=password, cart=cart, modify=modify
    )


@app.route("/logout")
def logout():
    if session.get("login_user") is not None:
        if session.get("login_user") != "":
            session.pop("login_user", default=None)
            session.pop("login_passwd", default=None)
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
