import json
import unittest
from unittest import TestCase
import server
from server import app


class FlaskRouteTests(TestCase):
    """Flask tests."""


################# Testing Necessities #################

    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True


##################### Test Routes ######################

    def test_home_route(self):
        """Test route to homepage."""

        result = self.client.get("/")
        self.assertEqual(result.status_code, 200)
        self.assertIn('Connect!', result.data)




#################  #################


if __name__ == "__main__":
    unittest.main()
