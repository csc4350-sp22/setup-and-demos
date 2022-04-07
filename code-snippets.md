# Databases
Adding a database to a Heroku app:

```
heroku addons:create heroku-postgres:hobby-dev
```

Basic DB setup in a Flask app:
```
app = flask.Flask(__name__)

# Point SQLAlchemy to your Heroku database
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
# Gets rid of a warning
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
```

Fetching all objects from a database:
```
todos = Todo.query.all()  # assuming we have a db.Model class called Todo
# same as SELECT * FROM todo;
```

Fetching all objects from a database matching a certain column name:
```
todos = Todo.query.filter_by(due_date="tomorrow")
# same as SELECT * FROM todo WHERE due_date='tomorrow'
```

Deleting everything from a table: run `heroku pg:psql`, then
```
DROP TABLE <table_name>;
```

# Flask

Setting HTTP methods an app route accepts:
```
@app.route("/my_page", methods=["GET", "POST"])  # could also be just ["POST"], willl be ["GET"] by default
def my_page_function():
    ...
```

Redirecting:
```
return flask.redirect(flask.url_for("index"))  # using the name of the function
return flask.redirect("/")  # using what's in @app.route()
```

Showing messages to the user:
```
# in Python
flask.flash("message")

# in HTML template
{% with messages = get_flashed_messages() %}
    {% if messages %}
        {% for message in messages %}
            <b>{{message}}</b>
        {% endfor %}
    {% endif %}
{% endwith %}
```

# Deploying a Flask + React app
The following assumes that you are using `npm run build` to generate static React resources that Flask sends down along with HTML. If you're following the Milestone 3 starter code, this applies to you.

1. Create a Heroku app: `heroku create --buildpack heroku/python`
2. Add nodejs buildpack: `heroku buildpacks:add --index 1 heroku/nodejs`
3. Push to Heroku: `git push heroku main`
