import unittest
from app import app


class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_home_page(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)

        self.assertIn(
            b"Version 2 - Automatically deployed to Kubernetes!",
            response.data
        )


if __name__ == "__main__":
    unittest.main()