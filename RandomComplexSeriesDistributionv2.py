import numpy as np
import matplotlib.pyplot as plt
from scipy.special import zeta
fig, ax = plt.subplots()
# Amount of terms to add up
n = 10**4
# Exponent
s = 3/2
plotlimval = zeta(s)
# Amount of points to plot
num = 10**6
pointset = np.array([])
integer_list = np.arange(1, n+1, dtype=float)
recip = 1/(integer_list**s)

array_length = 10**3
weights = np.exp(2*np.pi*1j*np.random.rand(array_length, n))
terms = np.multiply(weights, recip)
pointset = terms.sum(axis=1)

for i in range(num//array_length - 1):
    weights = np.exp(2*np.pi*1j*np.random.rand(array_length, n))
    terms = np.multiply(weights, recip)
    vals = terms.sum(axis=1)
    pointset = np.append(pointset, vals)

plt.plot(np.real(pointset), np.imag(pointset), 'r,', markersize=0.5)
# Draw circle with radius zeta(s)
draw_circle1 = plt.Circle((0, 0), plotlimval, fill=False)
draw_circle2 = plt.Circle((0, 0), max(2-plotlimval, 0), fill=False)
ax.add_artist(draw_circle1)
ax.add_artist(draw_circle2)
# Set size for plot
ax.set_aspect('equal', adjustable='box')
ax.set_xlim(-plotlimval, plotlimval)
ax.set_ylim(-plotlimval, plotlimval)
ax.set_title(f"$n=${n}, num$=${num}, $s=${s}")

fig.savefig("Complex_Random_Harmonic_Series_Dist2_3_2.png", dpi=1000,
            bbox_inches='tight', pad_inches=0.0)
