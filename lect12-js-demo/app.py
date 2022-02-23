import flask

app = flask.Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/")
def main():
    return flask.render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    val = flask.request.form["campus_id"]
    if val == "jmartin191":
        return flask.redirect("welcome")
    else:
        flask.flash("Wrong campus ID!")
        return flask.redirect("/")
    
@app.route("/welcome")
def the_welcome():
    return flask.render_template("welcome.html")

app.run(debug=True)