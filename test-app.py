import unittest
from app import tambah

class TestApp(unittest.TestCase):
    def test_tambah(self):
        self.assertEqual(tambah(5, 3), 8)
        self.assertEqual(tambah(-1, 1), 0)
        self.assertNotEqual(tambah(2, 2), 5)

if __name__ == "__main__":
    unittest.main()