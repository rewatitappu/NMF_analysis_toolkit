"""
Author - Rewati Tappu
This script takes as input the matrix of normalised counts and performs rank optimisation
"""

import os, re, sys, pandas as pd, numpy as np, seaborn as sns, matplotlib.pyplot as plt
from typing import TextIO
from sklearn.decomposition import NMF
from sklearn.metrics import explained_variance_score

#Import the dataframe of the normalised counts
df = pd.read_csv("/home/Documents/concat_mat_norm_counts_varfil_pynorm.txt", sep="\t")

#For the optimization of the factorization rank:
outfile = open("/home/Documents/nmf_rank_optimization.txt", "w")
for x in np.arange(2, 100, 1):
    for y in np.arange(0, 29, 1):
        df_N = np.matrix(df)
        model = NMF(n_components=x, init='random', random_state=y)
        W0 = model.fit_transform(df)
        H0 = model.components_

        if x > 2:
            model_comp = NMF(n_components=x-1, init='random', random_state=y)
            W1 = model_comp.fit_transform(df)
            H1 = model_comp.components_

            rss1 = np.sum(np.square(df_N - np.dot(W0, H0)))
            rss2 = np.sum(np.square(df_N - np.dot(W1, H1)))
            evar1 = explained_variance_score(df_N, np.dot(W0, H0))
            evar2 = explained_variance_score(df_N, np.dot(W1, H1))
            evar_diff = (evar1-evar2)
            print(x, rss2, rss1, evar1, evar_diff)
            outfile.write(str(x) + "\t" + str(rss2) + "\t" + str(rss1) + "\t" + str(evar1) + "\t" + str(evar_diff) + "\n")

outfile.close()
