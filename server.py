"""Server file for Hidden Gems."""

# Import necessary modules, etc.
# Utilize Jinja for HTML templates
from jinja2 import StrictUndefined
# Utilize Flask libraries
from flask import Flask, render_template, request, flash, redirect, session, jsonify
#Use toolbar for debugging
# from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db, Places
# Access local env variables
import os
import psycopg2
import sys
# Tells Flask where to find files / dirs
app = Flask(__name__, static_url_path='/static')
# Set a secret key to enable the flask session cookies and the debug toolbar
app.config['SECRET_KEY'] = os.environ.get("FLASK_SECRET_KEY", "seKriTz")
# Ensures undefined variables in jinja raise an error
app.jinja_env.undefined = StrictUndefined
# allows html to reload without restarting server
app.jinja_env.auto_reload = True


###################### Core Routes ###########################

@app.route('/')
# Routes app index page to homepage
def index():
    """Homepage."""

    places = Places.query.all()

    return render_template("index.html", places=places)


################### Helper Functions #######################


# Listening or requests
if __name__ == "__main__":

    connect_to_db(app)
    db.create_all(app=app)
    #Set debug=True in order to invoke the DebugToolbarExtension
    # app.debug = True

    # app.config['TRAP_HTTP_EXCEPTIONS'] = True
    # app.config['Testing'] = True
    #Use of debug toolbar
    # DebugToolbarExtension(app)

    # Run app locally
    app.run(host='0.0.0.0')

    #Run app via Heroku
    # PORT = int(os.environ.get("PORT", 5000))
    # app.run(host="0.0.0.0", port=PORT)
