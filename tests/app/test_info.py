import unittest

from scratch_map import app


class TestInfo(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_info_with_git_info(self):
        response = self.app.get("/info", follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn('"version": "0.0.0"'.encode(), response.data)
