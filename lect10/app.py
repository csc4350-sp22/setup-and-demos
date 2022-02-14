import flask

app = flask.Flask(__name__)
app.secret_key = "I am a secret key!"


@app.route("/")
def index():
    return flask.render_template("index.html")


@app.route("/handle_form", methods=["POST"])
def handle_form():
    data = flask.request.form
    campus_id = data["campus_id"]
    if campus_id == "jmartin191":
        return flask.redirect(flask.url_for("welcome"))
    else:
        flask.flash("Wrong campus ID entered")
        return flask.redirect(flask.url_for("index"))


@app.route("/other_page")
def welcome():
    return "<h1>Welcome John!<\h1>"  # just saving time


app.run()
