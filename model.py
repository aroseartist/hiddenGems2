""" Models and database functions. """

# Connection to PostgreSQL through Flask-SQLAlchemy helper library
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

##############################################################################
# Model definitions


class Places(db.Model):
    """Places"""

    # create table named places with appropriate columns
    __tablename__ = 'places'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(60), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    year_built = db.Column(db.Integer, nullable=True)
    description = db.Column(db.String(2000), nullable=True)
    features = db.Column(db.String(100), nullable=True)
    indoor_outdoor = db.Column(db.String(100), nullable=False)
    wifi = db.Column(db.String(100), nullable=True)
    seating = db.Column(db.String(100), nullable=True)
    restroom = db.Column(db.String(100), nullable=True)
    coord = db.Column(db.String(100), nullable=True)
    place_photo = db.Column(db.String(500), nullable=True)
    hours = db.Column(db.String(100), nullable=True)
    neighborhood = db.Column(db.String(100), nullable=True)
    wheelchair_accessible = db.Column(db.String(100), nullable=True)
    url = db.Column(db.String(100), nullable=True)



##################### Helper Functions ######################

def connect_to_db(app, db_uri="postgresql:///places"):
    """Connects database to Flask app"""

    # Configured for use of PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///places'
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # Allows for running of module interactively in order to work
    # with and access the db directly

    from server import app
    connect_to_db(app)
    db.create_all()
    print "Connected to DB"
