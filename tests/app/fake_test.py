import unittest


class TestInfo(unittest.TestCase):
    def fake_test(self):
        self.assertEqual(True, False)

    def fake_test2(self):
        self.assertEqual(True, True)
