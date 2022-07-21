import numpy as np
import matplotlib.pyplot as plt
from scipy.special import zeta
import seaborn as sns
fig, ax = plt.subplots()
# Amount of terms to add up
n = 10**4
# Exponent
s = 2
plotlimval = zeta(s)
# Amount of points to plot
num = 10**2
pointset = []
integer_list = np.arange(1, n+1)
recip = 1/(integer_list**s)
for i in range(num):
    t_n = np.random.uniform(0, 1, n)
    weights = np.exp(2*np.pi*1j*t_n)
    terms = weights*recip
    val = np.sum(terms)
    pointset.append(val)
    print(f"{100*i/num}%")



def PlotDistributionSmooth(data):
    sns.distplot(data, hist=False, kde=True,
                 color="darkblue",
                 kde_kws={"linewidth": 3})


magnitudes = np.abs(pointset)


# weights = np.ones_like(magnitudes)/len(magnitudes)
# plt.hist(magnitudes, bins=100, weights=weights, color="blue")

PlotDistributionSmooth(magnitudes)
# Set size for plot
ax.set_xlim(2-plotlimval, plotlimval)
ax.set_title(f"$n=${n}, num$=${num}, $s=${s}")

fig.savefig("Complex_Random_Harmonic_Series_Radial_Dist.pdf",
            bbox_inches='tight', pad_inches=0.0)
