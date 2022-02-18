import pandas as pd, numpy as np, networkx as nx, seaborn as sns, os, re, sys
import matplotlib.pyplot as plt
import matplotlib as mpl
from operator import itemgetter
from collections import defaultdict
import matplotlib.cm as cm
from networkx.drawing.nx_agraph import graphviz_layout

import matplotlib as mpl
mpl.rcParams['font.family'] = 'Arial'

#Here you import the file with all the correlations, between genes and cpgs filtered by any threshold (e.g. P<0.001)
df_corr = pd.read_csv("/home/nmf_results/LF_1_corr_merged_means.txt", sep="\t")
df_corr['combi'] = df_corr_merged['cpg'] + "_" + df_corr_merged['cpg_genes']

df_lfc_genes = pd.read_csv("/home/nmf_results/lfc_dcm_control.txt", sep="\t")
df_lfc_cpg = pd.read_csv("/home/nmf_results/differentially_methylated_regions.txt", sep="\t")

df_corr_merged = df_corr.merge(df_lfc_genes, left_on="ENSG", right_on="geneid", how="inner")
df_corr_merged = df_corr_merged.merge(df_lfc_cpg, left_on='cpg', right_on='cpg', how='inner')

cpgs = df_corr_merged['combi'].tolist()
cpgs_modified_names = []
Dict = {}

for c in cpgs:
    temp = c.split("_")
    #print(temp)
    Dict.setdefault(temp[0], []).append(temp[1])

#print(Dict)
for c in cpgs:
    temp = c.split("_")
    if temp[0] in Dict:
        cpgs_modified_names.append(Dict[temp[0]][0])
#print(cpgs_modified_names)

df_corr_merged['cpg_name'] = cpgs_modified_names

#print(df_corr_merged.columns)
fig, ax = plt.subplots()
G=nx.from_pandas_edgelist(df_corr_merged, 'gene_name', 'cpg_name')

size = []
colors = []


for node in G:
    #print(node)
    if node in df_corr_merged["gene_name"].values:
        l = df_corr_merged.loc[df_corr_merged['gene_name'] == node, 'log2FoldChange'].iloc[0]
        p = df_corr_merged.loc[df_corr_merged['gene_name'] == node, 'padj_lfc'].iloc[0]
		
		if l < 0:
			size.append(abs(l)*3000)
		else:
			size.append(abs(l)*6000)
		
        if p < 0.05: #if its sig
            colors.append("midnightblue")
        else:
            colors.append("cornflowerblue")
    else:

        l = df_corr_merged.loc[df_corr_merged['cpg_name'] == node, 'logFC(DCM/Control)'].iloc[0]
        p = df_corr_merged.loc[df_corr_merged['cpg_name'] == node, 'adj.P.Val'].iloc[0]
        if l < 0:
			size.append(abs(l)*3000)
		else:
			size.append(abs(l)*6000)
		
        if p < 0.05: #if its sig
            colors.append("indianred")
        else:
            colors.append("lightsalmon")

#print(nx.info(G))
ax = nx.draw_networkx(G, pos=graphviz_layout(G), with_labels=True, node_size=sizes, node_color=colors, font_color='black', font_size=8, font_weight='bold', edge_color='darkslategrey', edge_length=30, edge_weight=0.4, alpha=0.6, scale=3, width=2)
fig.set_size_inches(12.5, 8.5)
plt.savefig("/home/nmf_results/LF1_top_network.pdf")
