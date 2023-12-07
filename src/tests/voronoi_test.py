import unittest
import voronoi


class TestVoronoi(unittest.TestCase):

    def test_single_point_voronoi_diagram(self):
        expected_diagram = [[1]*10]*10
        points = [(4,7)]
        output = voronoi.jump_flood(points, 10)
        self.assertEqual(output, expected_diagram)


    def test_simple_voronoi_diagram_uneven(self):
        points = [(4,0),(4,8)]
        expected_diagram = [
        [1,1,1,1,1,2,2,2,2],
        [1,1,1,1,1,2,2,2,2],
        [1,1,1,1,1,2,2,2,2],
        [1,1,1,1,1,2,2,2,2],
        [1,1,1,1,1,2,2,2,2],
        [1,1,1,1,1,2,2,2,2],
        [1,1,1,1,1,2,2,2,2],
        [1,1,1,1,1,2,2,2,2],
        [1,1,1,1,1,2,2,2,2]]
        output = voronoi.jump_flood(points, 9)
        self.assertEqual(output, expected_diagram)


    def test_simple_voronoi_diagram_even(self):
        points = [(4,0),(4,8)]
        expected_diagram = [
        [1,1,1,1,1,2,2,2,2,2],
        [1,1,1,1,1,2,2,2,2,2],
        [1,1,1,1,1,2,2,2,2,2],
        [1,1,1,1,1,2,2,2,2,2],
        [1,1,1,1,1,2,2,2,2,2],
        [1,1,1,1,1,2,2,2,2,2],
        [1,1,1,1,1,2,2,2,2,2],
        [1,1,1,1,1,2,2,2,2,2],
        [1,1,1,1,1,2,2,2,2,2]]
        output = voronoi.jump_flood(points, 10)
        self.assertEqual(output, expected_diagram)
