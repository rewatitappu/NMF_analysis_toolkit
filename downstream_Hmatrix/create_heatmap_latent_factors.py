import os, sys, re, matplotlib.pyplot as plt
import seaborn as sns, pandas as pd
import scipy.stats as stats
from matplotlib.patches import Patch

#Import the dataframe of the normalised counts
def create_latent_var(df_path):
	df_h_mat = pd.read_csv(df_path, sep="\t")
	fig, ax = plt.subplots()
	lut = dict(zip(df_h_mat['diag'].unique(), [ '#3f7f93', '#c3553a']))
	row_colors = df_h_mat['diag'].map(lut)
	handles = [Patch(facecolor=lut[name]) for name in lut]
	s = sns.clustermap(df_h_mat.drop(['diag'], axis=1), z_score=1, row_colors=row_colors, row_cluster=True, cmap='vlag')
	plt.legend(handles, lut, title='diag',
           bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure, loc='upper right')
	plt.savefig("/home/nmf_results/h_matrix_heatmap.pdf")
