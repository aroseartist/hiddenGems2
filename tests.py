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
        Popos.query.delete()
        User.query.delete()

        # Add places
        self.popos = Popos(wifi='Yes', coord='37.795335, -122.401836', seating='Yes',
                           neighborhood='Financial District')
        self.popos = Popos(wifi='no', coord='37.794511, -122.403843', seating='Yes',
                           neighborhood='Financial District/Chinatown')

        self.popos_1 = SavedPopos(user_id=self.user_1.user_id,
                                        petition_id=2310776,
                                        date_signed='2016-08-18 21:25:03.300194')
        self.popos_2 = SavedPopos(user_id=self.user_1.user_id,
                                        petition_id=2298061)


        # add all to the database
        db.session.add_all([self.user_1, self.user_2, self.user_3, self.petition_1,
                            self.petition_2, self.petition_3, self.petition_4])
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
