# Julia-s-sets
Algorithme which generates Julia's sets

## Operation

You have to choose first a complex number, called *c = x + iy* where *x* and *y* are real numbers. This complex won't be changed for the rest of the Julia's set generation.

Then, for all complex number $z_0$, we define the following complex sequence $(z_n)$ :
```math
z_{n+1} = z_n^2 + c
```
If the sequence diverges, we colour the point $z_0$ of complex plan with black for example. If the sequence converges, we colour the point $z_0$ of complex plan with white.
If if want to add colors to our Julia's set, we have to colour $z_0$ with shades of blue (for example) and the more the sequence quickly diverges, the more the blue is dark.

We consider that while the magnitude of $z_n$ is less than 2, the sequence isn't diverging.

## Algorithm (black and white generation)

```
Packages import

Input : name of picture which is going to be generated
Input : real and imaginary part of the complex c
Var declaration : width and height of picture (4001x4001)
Var declaration : origin of the plan in image

Var declaration : image object

Var declaration : complex c

For each point (z0) of the complex plan with coordinates i, j : (/!\ That's not the i of i² = -1)
    Var declaration : complex z (with represents z0) with Re(z) = i/1000 et Im(z) = j/1000
    Var declaration : counter = 0

    While the magnitude of z < 2 and the counter < 30
        Increment : counter + 1
        z = z² + c

    If counter is equal to 30:
        Put the color black to the coordinates of (origin_x + i, origin_y + j)
```
