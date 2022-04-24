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
        l, r = mixer.advanced_mix(x, y)
        xs.append(x)
        ys.append(y)
        ls.append(l)
        rs.append(r)
    # plt.plot(xs, ys)
    # plt.plot(ls, rs)
    # plt.show()
    plt.plot(angles, ls)
    plt.plot(angles, rs)
    plt.axvline(0, color='red', linestyle=':', label='Right')
    plt.axvline(math.pi, color='red', linestyle=':', label='Left')
    plt.axvline(math.pi/2, color='red', linestyle=':', label='Forward')
    plt.axvline(3*math.pi/2, color='red', linestyle=':', label='Backward')
    plt.title("Mapping outputs as joystick is rolled around the perimeter")
    plt.xlabel("Angle the joystick is pointed towards (radians)")
    plt.ylabel("Motor power")
    plt.show()
