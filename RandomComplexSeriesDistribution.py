import numpy as np
import matplotlib.pyplot as plt
from scipy.special import zeta
fig, ax = plt.subplots()
# Amount of terms to add up
n = 10**4
# Exponent
s = 2
plotlimval = zeta(s)
# Amount of points to plot
num = 10**6
pointset = []
integer_list = np.arange(1, n+1)
recip = 1/(integer_list**s)
for i in range(num):
    t_n = np.random.uniform(0, 1, n)
    weights = np.exp(2*np.pi*1j*t_n)
    terms = weights*recip
    val = np.sum(terms)
    pointset.append(val)

plt.plot(np.real(pointset), np.imag(pointset), 'r,', markersize=0.5)
# Draw circle with radius zeta(s)
draw_circle1 = plt.Circle((0, 0), plotlimval, fill=False)
draw_circle2 = plt.Circle((0, 0), 2-plotlimval, fill=False)
ax.add_artist(draw_circle1)
ax.add_artist(draw_circle2)
# Set size for plot
ax.set_aspect('equal', adjustable='box')
ax.set_xlim(-plotlimval, plotlimval)
ax.set_ylim(-plotlimval, plotlimval)
ax.set_title(f"$n=${n}, num$=${num}, $s=${s}")

fig.savefig("Complex_Random_Harmonic_Series_Dist.png", dpi=1000,
            bbox_inches='tight', pad_inches=0.0)
