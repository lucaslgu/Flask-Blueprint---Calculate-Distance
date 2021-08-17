# library imports
import unittest
from main import distance_location


class TestCalculateDistance(unittest.TestCase):
    # if you are not on the Moscow Ring Road
    def test_distance_different(self):
        result_message = 5884.31454512658
        self.assertEqual(distance_location("37.80558825214547, -122.4701961628206"), result_message)

    # if you are on the Moscow Rind Road
    def test_distance_equal(self):
        result_message = 0
        self.assertEqual(distance_location("55.690943504922814, 37.413014159169926"), result_message)

    # if the data has passed in an invalid way
    def test_distance_error(self):
        result_message = None
        self.assertEqual(distance_location("55.6909a35t4922814, 37.41a0141q916v926"), result_message)


if __name__ == "__main__":
    unittest.main()
