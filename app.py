from flask import Flask, request, render_template

app = Flask(__name__)
app.secret_key = "una_llave_secreta_2021_esen"


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        user = request.form["username"]
        passwd = request.form["password"]
        return "<h1>posted</h1>"
    else:
        return "<h1>error</h1>"


if __name__ == "__main__":
    app.run(debug=True)
