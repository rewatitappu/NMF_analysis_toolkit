"""
Author - Rewati Tappu
"""

import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df_t = pd.read_csv("home/nmf_results/norm_counts.txt", sep="\t")
diag = pd.read_csv("home/nmf_results/pheno_counts.txt", sep="\t")
df_t['diag'] = diag['diag'].tolist()

feature = df_t
print(feature)

#import dataframe with columns as variables and a column with the phenotype

def run_KMeans(df_feature):
    feature = df_feature.drop(['diag'], axis=1)
    Sum_of_squared_distances = []
    K = range(1, 15)
    for k in K:
        km = KMeans(n_clusters=k)
        km = km.fit(feature)
        Sum_of_squared_distances.append(km.inertia_)

        print(Sum_of_squared_distances)

        plt.plot(K, Sum_of_squared_distances, 'bx-')
        plt.xlabel('k')
        plt.ylabel('Sum_of_squared_distances')
        plt.title('Elbow Method For Optimal k')
        plt.savefig("/Users/ngsmac7/Documents/lhp_backup/NMF_rank5_old_kim_2/optimalK_elbow_lf.pdf")


kmeans = KMeans(n_clusters=7, random_state=0).fit(feature)
print(kmeans.labels_)
