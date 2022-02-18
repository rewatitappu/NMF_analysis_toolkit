"""
Author - Rewati Tappu
This script takes as input the H matrix and does a preliminary analysis/visualisation of the latent factors.
"""

import os, sys, re, pandas as pd, scipy.stats as stats, pylab as pl, matplotlib.pyplot as plt, numpy as np, sklearn, seaborn as sns
from sklearn.metrics import roc_curve, auc

#import the loadings file.
df_loadings = pd.read_csv("/home/nmf_results/nmf_rank8_w.txt", sep="\t")
df_loadings = df_loadings.set_index('features')

for df in df_loadings:
   print(df)
   df_loadings_sorted = df_loadings.sort_values(by=df, ascending=False)
   q90 = df_loadings_sorted[df].quantile(0.9)
   q95 = df_loadings_sorted[df].quantile(0.95)
   q99 = df_loadings_sorted[df].quantile(0.99)
   q10 = df_loadings_sorted[df].quantile(0.1)
   q75, q25 = np.percentile(df_loadings[df], [75, 25])
   df_high25 = df_loadings_sorted[(df_loadings_sorted[df] <= q25) & (df_loadings_sorted[df] >= q10)]
   df_high75 = df_loadings_sorted[df_loadings_sorted[df] >= q75]
   df_high90 = df_loadings_sorted[df_loadings_sorted[df] >= q90]
   df_high95 = df_loadings_sorted[df_loadings_sorted[df] >= q95]
   df_high99 = df_loadings_sorted[df_loadings_sorted[df] >= q99]
   new_index = df_loadings.index.to_series().str[:2]
   df_loadings["feature_type"] = new_index
   df_loadings_genes = df_loadings[df_loadings["feature_type"] == "EN"]
   df_loadings_cpg = df_loadings[df_loadings["feature_type"] == "cg"]
   df_high99.to_csv("/home/nmf_results/" + df + "_q99_features.txt", sep="\t")
   fig, ax = plt.subplots()
   s1 = sns.distplot(df_loadings_genes[df], color='dodgerblue', label="genes")
   s2 = sns.distplot(df_loadings_cpg[df], color='slategray', label="cpg")
   ax.legend(loc='best')
   plt.savefig("/home/nmf_results/" + df + "_distplot.pdf")
