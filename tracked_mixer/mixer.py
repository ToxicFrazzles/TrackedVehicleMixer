import math


class Mixer:
    def __init__(self, square_input: bool = False, axes_range = 1.0):
        self.square_input = square_input
        self.axes_range = axes_range

    def _preprocess_inputs(self, x: float, y: float):
        if self.square_input:
            raise NotImplementedError("Square input spaces are not yet supported")
        if x > self.axes_range or x < -self.axes_range or y > self.axes_range or y < -self.axes_range:
            raise ValueError(f"Axes value is out of range. ({x}, {y}) should be between -{self.axes_range} and {self.axes_range}")
        if self.axes_range == 1.0:
            return x, y
        return x/self.axes_range, y/self.axes_range

    def simple_mix(self, x: float, y: float):
        return self._mix(*self._preprocess_inputs(x, y))

    def _mix(self, x: float, y: float):
        # Simple mixing is actually pretty close to acceptable
        l = max(min(y+x, 1.0), -1.0)
        r = max(min(y-x, 1.0), -1.0)
        return l, r

    def advanced_mix(self, x: float, y: float):
        return self._mix2(*self._preprocess_inputs(x, y))

    def _mix2(self, x: float, y: float):
        theta = math.atan2(y, x) % (2*math.pi)
        while theta < 0:
            theta += 2*math.pi
        m = math.sqrt(x**2 + y**2)
        if 0 <= theta <= math.pi/2:
            return m, m * -math.cos(2*theta)
        elif math.pi/2 < theta <= math.pi:
            return m * -math.cos(2*theta), m
        elif math.pi < theta <= 3*math.pi/2:
            return -m, m * math.cos(2*theta)
        elif 3*math.pi/2 < theta <= 2*math.pi:
            return m*math.cos(2*theta), -m
        return self._mix(x, y)      # Something went very wrong in the maths. Fallback to the simple mixing
