import pandas as pd, numpy as np, networkx as nx, seaborn as sns, os, re, sys
import matplotlib.pyplot as plt
from operator import itemgetter

#Here you import the file with all the correlations, between genes and cpgs within 99 percentile rank, and p-value less than 0.05.

def get_node_degree(path_corr_file):
	df_corr_merged = pd.read_csv(path_corr_file, sep="\t")
	out = open("/home/nmf_results/node_degree.txt", "w")
	df_corr_merged['combi'] = df_corr_merged['cpg'] + "_" + df_corr_merged['cpg_genes']
	df_corr_merged_req = pd.DataFrame(df_corr_merged, columns=['genes', 'padj', 'combi'])
	G=nx.from_pandas_edgelist(df_corr_merged_req, 'genes', 'combi')
	Edges = G.number_of_edges()
	degree_dict = dict(G.degree(G.nodes()))
	nx.set_node_attributes(G, degree_dict, 'degree')
	sorted_degree = sorted(degree_dict.items(), key=itemgetter(1), reverse=True)
	for d in sorted_degree:
    	out.write(str(d[0]))
    	out.write(str("\t"))
    	out.write(str(d[1]))
    	out.write(str("\n"))
    
