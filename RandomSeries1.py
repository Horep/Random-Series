import numpy as np
import seaborn as sns

def a(n):
    val = 4**-n
    return val


def RandomSum(n, Num):
    val = np.zeros(Num)
    for i in range(0, n + 1):
        rng = np.random.default_rng()
        rand = 2 * rng.integers(2, size=Num) - 1
        val += a(i) * rand
    return val


def PlotDistributionSmooth(data):
    sns.distplot(data, hist = False, kde = True, rug = True,
             color = "darkblue", 
             kde_kws={"linewidth": 3},
             rug_kws={'color': "black"})

#data = RandomSum(1000,50000)
#PlotDistributionSmooth(data)

def AnimatePlotDistributionSmooth(a, b, framenum):
    n = 1000
    Num = 500000
    Powers = np.linspace(a, b, framenum)
    for j in range(1,len(Powers)):
        val = np.zeros(Num)
        for i in range(0, n + 1):
            rng = np.random.default_rng()
            rand = 2 * rng.integers(2, size=Num) - 1
            val += (Powers[j])**-i * rand
        sns_plot = sns.distplot(val, hist = False, kde = True, rug = True,
                                color = "darkblue", 
                                kde_kws={"linewidth": 3},
                                rug_kws={'color': "black"})
        fig = sns_plot.get_figure()
        print(f"x = {Powers[j]}")
        fig.suptitle(f"x = {Powers[j]}")
        fig.savefig(f"frame{j}.pdf")
        fig.clf()


AnimatePlotDistributionSmooth(2, 2, 2)