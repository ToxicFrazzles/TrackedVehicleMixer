# TrackedVehicleMixer
A control mixer for mapping a single joystick input to the movement of a tracked vehicle


### Why?
Mapping the input of a joystick to the output of left and right motor power levels is a non-trivial task and is sometimes confusing.
The goal of this is to produce a mapping where there are no sudden changes in direction of motors when the joystick input changes a small amount.

### How does this solve the problem?
The code provided uses 2 possible solutions:
1. Simple addition and subtraction (fast on low-end hardware) while limiting the maximum output to 1.0
2. Hand-created waveform that closely matches the simple solution but with smoother transitions in response to avoid sudden sensitivity changes.

### What are the solutions?
#### Simple
The equations to calculate the outputs are as follows:

`left = Y + X`
`right = Y - X`

This produces the following output when the joystick is rotated around the perimeter:
![](images/Simple%20Mixing.png)

#### Advanced
The advanced mapping method uses the cosine trigonometric function and if statements to provide output where the key values are identical but the output is smoother and more consistent
The following image shows the smoother output:
![](images/Advanced%20Mixing.png)
