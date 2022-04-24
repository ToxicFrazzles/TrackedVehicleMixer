import math
import unittest
from .mixer import Mixer


class CircularInputTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.mixer = Mixer(square_input=False, axes_range=1.0)

    def test_known_directions(self):
        directions = {
            "Forward": (0.0, 1.0, 1.0, 1.0),
            "Backward": (0.0, -1.0, -1.0, -1.0),
            "Left": (-1.0, 0.0, -1.0, 1.0),
            "Right": (1.0, 0.0, 1.0, -1.0),
            "None": (0.0, 0.0, 0.0, 0.0),
        }
        for direction, (x, y, l, r) in directions.items():
            with self.subTest(direction=direction):
                left, right = self.mixer.advanced_mix(x, y)
                self.assertAlmostEqual(l, left)
                self.assertAlmostEqual(r, right)

    def test_output_domain(self):
        for i in range(360):
            theta = math.radians(i)
            x = math.cos(theta)
            y = math.sin(theta)
            l, r = self.mixer.simple_mix(x, y)
            self.assertLessEqual(l, 1.0)
            self.assertLessEqual(r, 1.0)
            self.assertGreaterEqual(l, -1.0)
            self.assertGreaterEqual(r, -1.0)


if __name__ == '__main__':
    unittest.main()
