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

    def test_input(self):
        # Check first value is added
        response1 = self.app.post("/", data={"add_country": "Wales"})
        self.assertEqual(response1.status_code, 200)
        self.assertIn(b"<p>Wales</p>", response1.data)
        self.assertNotIn(b"<p>But I prefer England</p>", response1.data)

        # Check second value is added and the first is still there
        response2 = self.app.post("/", data={"add_country": "But I prefer England"})
        self.assertEqual(response2.status_code, 200)
        self.assertIn(b"<p>Wales</p>", response2.data)
        self.assertIn(b"<p>But I prefer England</p>", response2.data)


if __name__ == "__main__":
    unittest.main()
