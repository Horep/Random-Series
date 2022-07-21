import numpy as np
import matplotlib.pyplot as plt
from scipy.special import zeta
import seaborn as sns

# Number of terms in summation
n = 10**4
# Number of points
num = 10**6
# Exponent in sum
s = 3
plotlimval = zeta(s)
# defines the function for calculation of eqn 5.13


def mag(X):
    scale_X = 2*np.pi*X
    w_sin = np.sum(np.sin(scale_X)*recip_int)
    w_cos = np.sum(np.cos(scale_X)*recip_int)
    val = np.sqrt(w_cos**2 + w_sin**2)
    return val


# plots the histogram


def PlotDistributionSmooth(data):
    sns.distplot(data, hist=True, kde=True,
                 color="darkblue",
                 kde_kws={"linewidth": 3})


recip_int = 1/(np.arange(1, n+1, dtype=float)**s)
mag = [mag(np.random.uniform(0, 1, n)) for i in range(num)]
fig, ax = plt.subplots()

PlotDistributionSmooth(mag)
# Set size for plot
ax.set_xlim(max(2-plotlimval, 0), plotlimval)
ax.set_title(f"$n=${n}, num$=${num}, $s=${s}")

fig.savefig(f"Radial_Distribution_s={s}.pdf",
            bbox_inches='tight', pad_inches=0.0)
