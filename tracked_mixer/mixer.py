import math


class Mixer:
    def __init__(self, square_input: bool = False, axes_range = 1.0):
        self.square_input = square_input
        self.axes_range = axes_range

    def mix(self, x: float, y: float):
        if self.square_input:
            raise NotImplementedError("Square input spaces are not yet supported")
        if x > self.axes_range or x < -self.axes_range or y > self.axes_range or y < -self.axes_range:
            raise ValueError(f"Axes value is out of range. ({x}, {y}) should be between -{self.axes_range} and {self.axes_range}")
        if self.axes_range == 1.0:
            return self._mix(x, y)
        return self._mix(x/self.axes_range, y/self.axes_range)

    def _mix(self, x: float, y: float):
        # x**2 + y**2 = 1
        theta = math.atan2(y, x)
        r = math.sqrt(x**2 + y**2)
        theta -= math.pi/4
        return r*math.cos(theta)/math.sqrt(0.5), r*math.sin(theta)/math.sqrt(0.5)

    def _mix2(self, x: float, y: float):
        pass

