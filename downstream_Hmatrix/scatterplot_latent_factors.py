"""
Author - Rewati Tappu
This script takes as input the H matrix and does a preliminary analysis/visualisation of the latent factors.
"""

import os, sys, re, pandas as pd, scipy.stats as stats, pylab as pl, matplotlib.pyplot as plt, numpy as np, sklearn, seaborn as sns
from sklearn.metrics import roc_curve, auc
from matplotlib.patches import Patch

sns.set_style("white")

def importH(path, pheno_path):
	df = pd.read_csv(path, sep="\t")
	df = df.set_index(['LF']).T
	df = df * 10
	df['samples'] = df.index
	samples = df['samples'].tolist()
	pheno = pd.read_csv(pheno_path, sep="\t")
	df_merged = df.merge(pheno, how='inner', left_on='samples', right_on = 'PID_Tissue')
	print(df_merged)

	df_merged.to_csv("/home/nmf_results/nmf_h_T.txt", sep="\t")
	df_merged = df_merged.drop(['samples', 'PID_Tissue'], axis=1)


#For preparing a scatterplot matrix for 5 latent factors

def plot_scatter():
	for df in df_merged:
   		if df.startswith("LF"):
       		fig, ax = plt.subplots()
       sns.set(font_scale=0.9)
       s = sns.pairplot(data=df_merged, vars=['LF1','LF2', 'LF3', 'LF4', 'LF5'], hue='diag', palette=(sns.diverging_palette(220, 20, n=3)))
       plt.savefig("/home/nmf_results/scatterplot_2.pdf")
    
def mann_whitney():
	df_control = df_merged[df_merged['DCM'] == 0]
	df_dcm = df_merged[df_merged['DCM'] == 1]

	print(df_control)
	print(df_dcm)

	for df in df_control:
    	if df in df_dcm:
        	print(df)
        	T = stats.mannwhitneyu(df_control[df], df_dcm[df])
        	print(T[0], T[1], df_control[df].mean(axis=0), df_dcm[df].mean(axis=0))
