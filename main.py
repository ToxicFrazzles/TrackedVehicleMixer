from tracked_mixer import Mixer
import matplotlib.pyplot as plt
import math


if __name__ == "__main__":
    # Test output when moving joystick around the circumference
    xs, ys, ls, rs = [], [], [], []
    angles = []
    mixer = Mixer()
    for i in range(360):
        theta = math.radians(i)
        angles.append(theta)
        x = math.cos(theta)
        y = math.sin(theta)
        l, r = mixer.mix(x, y)
        xs.append(x)
        ys.append(y)
        ls.append(l)
        rs.append(r)
    plt.plot(xs, ys)
    plt.plot(ls, rs)
    plt.show()
    plt.plot(angles, ls)
    plt.plot(angles, rs)
    plt.axvline(0)              # Full right
    plt.axvline(math.pi)        # Full left
    plt.axvline(math.pi/2)      # Backward
    plt.axvline(3*math.pi/2)    # Forward
    plt.show()