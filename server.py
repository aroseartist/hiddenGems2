"""Server file for Hidden Gems."""

# Import necessary modules, etc.

# Utilize Jinja for HTML templates
import jinja2
# Access local env variables
import os
import sys

# Utilize Flask libraries
from flask import (Flask, render_template, redirect, request, flash, jsonify)
# Use toolbar for debugging
# from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
from sys import argv


app = Flask(__name__, static_url_path='/static')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# Required to use Flask sessions and debug toolbar
app.secret_key = 'FLASK_SECRET_KEY'

# Ensures undefined variables in jinja raise an error
app.jinja_env.undefined = StrictUndefined
# allows html to reload without restarting server
app.jinja_env.auto_reload = True


###################### Core Routes ###########################



@app.route('/')
# Routes app index page to homepage
def index():
    """Homepage."""
    return render_template("base.html", input_box_name_here=None)



################### Helper Functions #######################

# Listening or requests
if __name__ == "__main__":
    
    # Set debug=True in order to invoke the DebugToolbarExtension
    # app.debug = True

    # app.config['TRAP_HTTP_EXCEPTIONS'] = True
    # app.config['Testing'] = True
    # Use of debug toolbar
    # DebugToolbarExtension(app)
   
    # connect_to_db(app)

    # Run app locally
    app.run(host='0.0.0.0')
    
    #  Run app via Heroku
    # PORT = int(os.environ.get("PORT", 5000))
    # app.run(host="0.0.0.0", port=PORT)

