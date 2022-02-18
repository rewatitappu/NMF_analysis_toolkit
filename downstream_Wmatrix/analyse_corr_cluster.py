import os, sys, re, matplotlib.pyplot as plt, numpy as np, pandas as pd, seaborn as sns, scipy.stats as stats

#this script takes as input the correlations of the genes and cpg features, all and sig ones. and analyses the output.
#we want to know the distribution of p-values and the top most correlations.

df_corr_all = pd.read_csv("/home/nmf_results/LF_1_corr_eqtl.txt_padj.txt", sep="\t")

fig, ax = plt.subplots()
ax.set_xlim([-1.0, 1.0])
ax = sns.distplot(df_corr_all['t_statistic'], color='sandybrown')
df_corr_all = df_corr_all.dropna(axis=0)
mean_corr = np.mean(np.abs(df_corr_all['t_statistic'].tolist()))
plt.savefig("/home/nmf_results/new_strategy/LF_8_corr_distribution.pdf")


df_corr_sig_sorted = df_corr_all.sort_values(by='padj') #change according to which matrix you want to work on.

#take the significant p-values
df_corr_sig_sorted = df_corr_sig_sorted[df_corr_sig_sorted['padj'] <= 0.05]

cpg_list = df_corr_sig_sorted['cpg'].tolist()
#print(cpg_list)

Dict = {}
with open("/home/nmf_results/mapping_cpg_gene.txt", "r") as File:
	for f in File:
		f = f.rstrip()
		if ":" in f:
			temp = f.split(",:,")
			if len(temp) == 2:
				Dict.update({temp[0] : temp[1]})

##print(Dict)
cpg_list_genes = []
counter = 0
for c in cpg_list:
	if c in Dict:
		cpg_list_genes.append(Dict[c])
	else:
		counter = counter+1
		V = c + "_NA"
		cpg_list_genes.append(V)
		
df_corr_sig_sorted['cpg_genes'] = cpg_list_genes
print(df_corr_sig_sorted)

##output significant sorted correlations with the gene names and genes associated with CpGs
df_corr_sig_sorted.to_csv("/home/nmf_results/gene_names_merged_corr_padj.txt", sep="\t", index=False)
