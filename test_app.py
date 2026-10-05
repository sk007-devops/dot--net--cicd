import unittest
from app import app


class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_home_page(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)

        self.assertIn(
            b"Hello from Automatic GitHub Jenkins CI/CD Pipeline! by sanket",
            response.data
        )


if __name__ == "__main__":
    unittest.main()