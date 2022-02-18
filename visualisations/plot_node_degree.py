import os, sys, re
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("/home/nmf_results/LF5_node_degree_rlog.txt", sep="\t")
#print(df)

new_index = df['feature'].str[:2]
df["feature_type"] = new_index
df_cpg = df[df["feature_type"] == "cg"]
df_genes = df[~df['feature'].isin(df_cpg['feature'])]

average_deg = df_genes['degree'].median()
df_genes['ratio'] = df_genes['degree']
q90_genes = df_genes['degree'].quantile(0.90)
print(q90_genes)
df_genes_req = df_genes[df_genes['degree'] >= q90_genes]
df_genes_req.to_csv("/home/nmf_results/LF5_genes_node_degree_q90.txt", sep="\t")


df_cpg = df_cpg[df_cpg['degree'] > 1] #select only those cpgs who have greater than one node degree
q99_cpg = df_cpg['degree'].quantile(0.99)
average_deg_c = df_cpg['degree'].median()
df_cpg['ratio'] = df_cpg['degree']

#print(average_deg)
#print(df_genes.shape)
#print(average_deg_c)
#print(df_cpg.shape)

#df_genes.to_csv("/home/nmf_results/LF1_node_degree_rlog_sorted.txt", sep="\t", index=False)

#fig, ax = plt.subplots()
#N = np.arange(0, df_genes.shape[0], 1)
#s = sns.lineplot(x=N, y=df_genes["ratio"])
#plt.savefig("/home/nmf_results/LF5_node_ratio_plot_gene_rlog.pdf")
#
#fig1, ax1 = plt.subplots()
#N1 = np.arange(0, df_cpg.shape[0], 1)
#s = sns.lineplot(x=N1, y=df_cpg["ratio"])
#plt.savefig("/home/nmf_results/LF5_node_ratio_plot_cpg_rlog.pdf")
