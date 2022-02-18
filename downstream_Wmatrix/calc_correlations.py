"""
Author - Rewati Tappu
This script is for performing the correlation analyses between selected samples
"""

import os, sys, re, matplotlib.pyplot as plt, numpy as np, pandas as pd, seaborn as sns, scipy.stats as stats
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

def calc_corr(df_omics1, df_omics2, sig_omics1, sig_omics2, index_col):
	df_omics1 = pd.read_csv(df_omics1, sep="\t")
	df_omics2 = pd.read_csv(df_omics2, sep="\t")
	df_sig_omics1 = pd.read_csv(sig_omics1, sep="\t")
	omics1_list = df_sig_omics1[index_col].tolist()
	omics2_list = df_sig_omics2[index_col].tolist()
	df_omics1_req = df_omics1[df_omics1[index_col].isin(omics1_list)]
	df_omics2_req = df_omics2[df_omics2[index_col].isin(omics2_list)]
	df_omics1_req = df_omics1_req.set_index(index_col)
	df_omics2_req = df_omics2_req.set_index(index_col)
	out = open("corr_outfile.txt", "w")
	for index, row in df_omics1_req.iterrows():
	for index2, row2 in df_omics2_req.iterrows():
		S = stats.pearsonr(row, row2)
		W = index + "\t" + index2 + "\t" + str(S[0]) + "\t" + str(S[1]) + "\n"
		out.write(W)


