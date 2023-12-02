import unittest
import perlin


class TestPerlin(unittest.TestCase):

    def test_single_product(self):
        random_grad = (1,1)
        distance_vector = (5,6)
        self.assertEqual(perlin.single_product(random_grad, distance_vector),11)
