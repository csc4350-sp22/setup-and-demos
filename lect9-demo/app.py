import os
import flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

app = flask.Flask(__name__)

# Point SQLAlchemy to your Heroku database
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
# Gets rid of a warning
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(120))
    priority = db.Column(db.String(80))
    due_date = db.Column(db.String(80))


db.create_all()


@app.route("/", methods=["GET", "POST"])
def index():
    if flask.request.method == "POST":
        data = flask.request.form
        new_todo = Todo(
            task=data["task"], priority=data["priority"], due_date=data["due_date"]
        )
        db.session.add(new_todo)
        db.session.commit()

    todos = Todo.query.all()
    num_todos = len(todos)
    return flask.render_template(
        "index.html",
        num_todos=num_todos,
        todos=todos,
    )


app.run(debug=True)
