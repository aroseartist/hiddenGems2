import json
import unittest
from unittest import TestCase
import server
from server import app


class FlaskRouteTests(TestCase):
    """Flask tests."""


############### Testing Necessities ###############

    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True


################### Test Routes ##################

    def test_home_route(self):
        """Test route to homepage."""

        result = self.client.get("/")
        self.assertEqual(result.status_code, 200)
        # self.assertIn('Connect!', result.data)


################# Test Database #################

class FlaskTestDatabase(TestCase):
    """Flask tests that use the test database"""

    def setUp(self):
        """Things to do before each test"""

        # Get the Flask test client
        self.client = app.test_client()
        # Show Flask errors that happen during tests
        app.config['TESTING'] = True
        # Connect to test database
        connect_to_db(app, "postgresql:///testdb")
        # Create tables and add sample data
        db.create_all()
        # add example data to test database
        """Create some sample data."""

        # In case this is run more than once, empty out existing data
        Places.query.delete()

        # Add places
        self.places_1 = Places(name='Transamerica Pyramid Center',
                               address='600 Montgomery Street',
                               year_built=1972,
                               description='This urban park, located at the foot of the Transamerica Pyramid.',
                               features='Fountain, Bronze Sculptures',
                               indoor_outdoor='Outdoor',
                               wifi='no',
                               seating='Yes',
                               restroom='Yes',
                               coord='37.795494, -122.402185',
                               place_photo='/static/img/1.jpg',
                               hours='M-F 7am-5:30pm',
                               neighborhood='Financial District',
                               wheelchair_accessible='Yes',
                               url='https://www.yelp.com/biz/transamerica-redwood-park-san-francisco-2')
        self.places_2 = Places(name='Transamerica Redwood Park',
                               address='600 Montgomery Street',
                               year_built=1972,
                               description='This urban park, located at the foot of the Transamerica Pyramid.',
                               features='Fountain, Bronze Sculptures',
                               indoor_outdoor='Outdoor',
                               wifi='no',
                               seating='Yes',
                               restroom='Yes',
                               coord='37.795494, -122.402185',
                               place_photo='/static/img/1.jpg',
                               hours='M-F 7am-5:30pm',
                               neighborhood='Financial District',
                               wheelchair_accessible='Yes',
                               url='https://www.yelp.com/biz/transamerica-redwood-park-san-francisco-2')

        # add all to the database
        db.session.add_all([self.places_1, self.places_2])
        # commit changes
        db.session.commit()


    def tearDown(self):
        """Things to do at end of every test"""

        # close the session
        db.session.close()
        # drop database
        db.drop_all()




if __name__ == "__main__":
    unittest.main()
