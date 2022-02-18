import os, sys, re, matplotlib.pyplot as plt, numpy as np, pandas as pd, seaborn as sns, scipy.stats as stats
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

df_meth_biopsy = pd.read_csv("/home/nmf_results/meth_selected_features.txt", sep="\t")
df_mrna_biopsy = pd.read_csv("/home/nmf_results/mrna_selected_features.txt", sep="\t")

#plot the scatter of the features
gene_df = df_mrna_biopsy[df_mrna_biopsy.index.isin(['ENSG00000143549', 'ENSG00000183091', 'ENSG00000187672'])]
cpg = df_meth_biopsy.loc['cg03044444', : ]
gene = df_mrna_biopsy.loc['ENSG00000143549', : ]
gene_df = gene_df.T

D = {'gene' : gene, 'cpg' : cpg}
df = pd.DataFrame(D)

pd_pheno = pd.read_csv("/home/nmf_results/kmeans_k4.txt", sep="\t")
pd_pheno2 = pd.read_csv("/home/nmf_results/phenoData.txt", sep="\t")
#pids = pd_pheno['K'].tolist()
dcm = pd_pheno2['DCM'].tolist()

##df['K'] = pids
df['DCM'] = dcm
gene_df['DCM'] = dcm
gene_df['ENS3'] = pd_pheno2['LF_3_r5'].tolist()
print(gene_df)

fig, ax = plt.subplots()
##s = sns.boxplot(y='gene',x='DCM', data=df, palette=(sns.diverging_palette(220, 20, n=2)))
##s = sns.lmplot(x='gene', y='cpg', hue='DCM', palette=(sns.diverging_palette(220, 20, n=2)), data=df)
grid = sns.JointGrid(x='gene', y='cpg', data=df)
g = grid.plot_joint(sns.scatterplot, hue='DCM', palette=(sns.diverging_palette(220, 20, n=2)), data=df)
sns.kdeplot(df.loc[df['DCM']==1, 'gene'], ax=g.ax_marg_x, legend=False, color='#c3553a')
sns.kdeplot(df.loc[df['DCM']==0, 'gene'], ax=g.ax_marg_x, legend=False, color='#3f7f93')
sns.kdeplot(df.loc[df['DCM']==1, 'cpg'], ax=g.ax_marg_y, vertical=True, legend=False, color='#c3553a')
sns.kdeplot(df.loc[df['DCM']==0, 'cpg'], ax=g.ax_marg_y, vertical=True, legend=False, color='#3f7f93')
plt.savefig("/home/nmf_results//ENSG00000143549_TPM3_cg03044444_rlog.pdf")
