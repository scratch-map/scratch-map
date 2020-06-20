import unittest

from scratch_map import app


class TestRoot(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_renders(self):
        response = self.app.get("/", follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        # Header
        self.assertIn(b"<h1>Scratch Map</h1>", response.data)
        # Input box
        self.assertIn(b'<input name="add_country">', response.data)


if __name__ == "__main__":
    unittest.main()
