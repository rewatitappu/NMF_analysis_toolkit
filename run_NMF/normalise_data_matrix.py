"""
Author - Rewati Tappu
This script takes in the mRNA and methylation data matrices and concatenates and normalises them
"""

import os, sys, re, pandas as pd, scipy.stats as stats, pylab as pl, matplotlib.pyplot as plt
import numpy as np, sklearn, seaborn as sns
from sklearn.metrics import roc_curve, auc

df = pd.read_csv("/home/nmf_results/concat_mat_norm_counts_varfil.txt", sep="\t")
df = df.set_index('feature')
df_norm = sklearn.preprocessing.normalize(df, norm='max')
print(df_norm.shape)
np.savetxt('/home/nmf_results/concat_mat_norm_counts_varfil_pynorm.txt', df_norm, delimiter='\t', fmt='%f')
