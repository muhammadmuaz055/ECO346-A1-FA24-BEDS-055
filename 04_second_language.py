"""Q5: recompute the Q3 band table and redraw the Q3 figure in Python.
Run from the repository root:  python scripts/04_second_language.py
Needs: pandas, numpy, matplotlib."""
import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, FixedFormatter

PROV, AREA = 4, 2            # variant 7 = Balochistan urban (edit for your variant)
os.makedirs("figures", exist_ok=True); os.makedirs("tables", exist_ok=True)

persons = pd.read_csv("data/pslm_person_subset.csv", usecols=["hhid", "age", "earn_annual"])
hh = pd.read_csv("data/pslm_hh_subset.csv", usecols=["hhid", "hhweight", "prov_code", "urban_rural"])
d = persons.merge(hh, on="hhid", how="left")
e = d[(d.prov_code == PROV) & (d.urban_rural == AREA) & d.age.between(15, 64) & (d.earn_annual > 0)].copy()

def w_mean(x, w):
    return (w * x).sum() / w.sum()

def w_quantile(x, w, p):
    """Smallest x whose cumulative weight share reaches or exceeds p (the brief's definition)."""
    o = np.argsort(x.values, kind="mergesort")
    xs, ws = x.values[o], w.values[o]
    cw = np.cumsum(ws) / ws.sum()
    return xs[np.argmax(cw >= p - 1e-12)]

e["band"] = 15 + 5 * ((e.age - 15) // 5)
e["mid"] = e.band + 2
rows = []
for b, g in e.groupby("band"):
    rows.append(dict(band=f"{b}-{b+4}", mid=b + 2, n=len(g),
                     wmean=round(w_mean(g.earn_annual, g.hhweight)), thin=len(g) < 30))
tab = pd.DataFrame(rows)
tab.to_csv("tables/band_table_python.csv", index=False)
print(tab.to_string(index=False))

# Compare with the R table when it exists
if os.path.exists("tables/band_table_R.csv"):
    r = pd.read_csv("tables/band_table_R.csv")
    print("R and Python band means identical:", (r.wmean.values == tab.wmean.values).all())

peak = tab.loc[tab.wmean.idxmax()]
print("Highest weighted-mean band:", peak.band, peak.wmean)

rng = np.random.default_rng(346)   # jitter by hand: uniform noise of at most 0.4 years
fig, ax = plt.subplots(figsize=(8, 5.5))
ax.scatter(e.age + rng.uniform(-0.4, 0.4, len(e)), e.earn_annual, s=14, alpha=0.30, color="#4C78A8", linewidths=0)
ax.plot(tab.mid, tab.wmean, color="#C0392B", lw=1.8, zorder=3)
solid, thin = tab[~tab.thin], tab[tab.thin]
ax.scatter(solid.mid, solid.wmean, s=70, color="#C0392B", zorder=4)
ax.scatter(thin.mid, thin.wmean, s=70, facecolors="white", edgecolors="#C0392B", linewidths=1.8, zorder=4)
ax.annotate(f"Highest mean: {peak.band}\nRs {int(peak.wmean):,} (thin band)", (peak.mid, peak.wmean),
            xytext=(0, 28), textcoords="offset points", ha="center", fontsize=9,
            arrowprops=dict(arrowstyle="-", color="grey"))
ax.set_yscale("log"); ax.set_ylim(1e4, 1e7); ax.set_xlim(14, 65)
ax.yaxis.set_major_locator(FixedLocator([1e4, 1e5, 1e6, 1e7]))
ax.yaxis.set_major_formatter(FixedFormatter(["Rs 10,000", "Rs 100,000", "Rs 1,000,000", "Rs 10,000,000"]))
ax.yaxis.set_minor_locator(FixedLocator([]))
ax.set_xlabel("Age (years)"); ax.set_ylabel("Annual earnings (log scale)")
ax.set_title("Mean earnings rise with age; the top band (60-64) rests on only 16 earners", loc="left", fontweight="bold", fontsize=11)
fig.text(0.01, 0.01, "Source: PSLM 2019-20 person file. Sample: earners aged 15-64, Balochistan urban. "
         "Weighted by hhweight. Hollow markers: band with fewer than 30 observations.", fontsize=7, color="grey", ha="left")
fig.tight_layout(rect=[0, 0.03, 1, 1])
fig.savefig("figures/fig_03_relationship_python.svg")
print("saved figures/fig_03_relationship_python.svg")
