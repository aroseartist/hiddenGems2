"""Utility file to seed database"""

from sqlalchemy import func
from model import Popos

from model import connect_to_db, db
from server import app


##################### SEED FUNCTIONS ######################


def load_popos():
    """Load places from places.csv into database."""

    print "Publicly Owned"

    # Delete all rows in table, so if we need to run this a second time,
    # we won't be trying to add duplicate users
    Placess.query.delete()

    # Read legislator file and insert data
    for row in open("data/places.csv"):
        row = row.rstrip()
        name,address,year_built,description,features,indoor_outdoor,
        wifi,seating,restroom,coord,hours,neighborhood,wheelchair_accessible,
        url,place_photo = row.split(",")

        places = Places(name=name,
                      address=address,
                      year_built=year_built,
                      description=description,
                      features=features,
                      indoor_outdoor=indoor_outdoor,
                      wifi=wifi,
                      seating=seating,
                      restroom=restroom,
                      coord=coord,
                      place_photo=place_photo,
                      hours=hours,
                      neighborhood=neighborhood,
                      wheelchair_accessible=wheelchair_accessible,
                      url=url)


        # We need to add to the session or it won't ever be stored
        db.session.add(popos)

    # Once we're done, we should commit our work
    db.session.commit()


################################################################


if __name__ == "__main__":
    connect_to_db(app)

    # In case tables haven't been created, create them
    db.create_all()

