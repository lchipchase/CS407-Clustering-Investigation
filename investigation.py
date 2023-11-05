import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from pabutools.election import parse_pabulib
from pabutools.election import ApprovalBallot, Ballot
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.manifold import TSNE




instance, profile = parse_pabulib("elections/poland_warszawa_2019_obszar-iii-powsin-kepa-latoszkowa-zamosc-latoszki.pb")
# instance, profile = parse_pabulib("elections/poland_wroclaw_2015_150-500.pb")

b = ApprovalBallot()
# for ballot in profile:
ballots = []
for ballot in profile:
    ballots.append(list(ballot))

print(instance)

mlb = MultiLabelBinarizer()
data = mlb.fit_transform(ballots)


tsne = TSNE(n_components=2, perplexity=30, n_iter=250, random_state=42)
data_2d = tsne.fit_transform(data)

# This is something you'd have to decide based on domain knowledge or techniques like the elbow method
k = 6

# Perform k-means clustering
kmeans = KMeans(n_clusters=k, random_state=42)
clusters = kmeans.fit_predict(data_2d)

# Plotting the clusters
plt.figure(figsize=(8, 6))

# Scatter plot of the data points, coloring them based on the cluster they belong to
for i in range(k):
    plt.scatter(data_2d[clusters == i, 0], data_2d[clusters == i, 1], label=f'Cluster {i}')

# Plot the centroids
centroids = kmeans.cluster_centers_
plt.scatter(centroids[:, 0], centroids[:, 1], s=100, c='black', marker='X', label='Centroids')

plt.title('K-Means Clustering on 2D Data')
plt.xlabel('Component 1')
plt.ylabel('Component 2')
plt.legend()
plt.show()
