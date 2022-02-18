"""
Author: Rewati Tappu
This is a script for checking the datasets that will be used as an input for matrix factorisation.
The script checks basic statistics of the individual OMICS dataset and removes features with variance lower than a given threshold.
"""


import os, re, scipy.stats as stats, pandas as pd, numpy as np, matplotlib.pyplot as plt, seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

#Check if the columns are samples and the rows are features.
#Input is the path to the dataframe, the sample list and the subset of the sample list and name
#of column that should be the index.
def import_dataset(df_path, samples, req_samples, ind):
	df_dataset = pd.read_csv(df_path, sep="\t", skiprows=1, names = samples)
	df_dataset = pd.DataFrame(df_dataset, columns=req_samples)
	df_dataset = df_dataset.set_index(ind)
	print(df_dataset.shape)
	print(df_dataset.describe())
	return df_dataset

#Calculating the min, max, mean and standard deviations for all the features present in the dataframes.
def stats(df_dataset):
	df_stats = pd.DataFrame()
	df_stats["mean"]=df_dataset.mean(axis=1)
	df_stats["Std.Dev"]=df_dataset.std(axis=1)
	df_stats["variance"]=df_dataset.var(axis=1)
	df_stats.index = df_dataset.index
	print(df_stats.describe())

#plot the mean and variance
#input is the dataframe of statistics
def plot_stats(df_stat, variable):
	fig, ax = plt.subplots()
	s = sns.distplot(df_stat[variable], color='red')
	plt.savefig("home/variance_distplot.pdf")

#filter based on mean and variance
#df_stats_fil = df_stats[(df_stats['mean'] > 0.40) & (df_stats['variance'] > 0.005)]
def filter(df_stat, df_dataset, threshold, var):
	df_stats_fil = df_stat[df_stat[var] > threshold]
	print(df_stats_fil.describe())
	df_dataset_fil = df_dataset[df_dataset[df_dataset.index.isin(df_stats_fil.index)]
	return df_dataset_fil

df_meth = import_dataset()

