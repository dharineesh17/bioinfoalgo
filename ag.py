
import numpy as np

from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram
from sklearn.cluster import AgglomerativeClustering


def plot_dendrogram(models, **kwargs):
    # Create linkage matrix and then plot the dendrogram

    # create the counts of samples under each node
    counts = np.zeros(models.children_.shape[0])
    n_samples = len(models.labels_)
    for i, merge in enumerate(models.children_):
        current_count = 0
        for child_idx in merge:
            if child_idx < n_samples:
                current_count += 1  # leaf node
            else:
                current_count += counts[child_idx - n_samples]
        counts[i] = current_count

    linkage_matrix = np.column_stack([models.children_, models.distances_,
                                      counts]).astype(float)

    # Plot the corresponding dendrogram
    dendrogram(linkage_matrix, **kwargs)


X = np.array([
            [0,1,2,2,3],   
            [1,0,2,5,3],
            [2,2,0,1,6],
            [2,5,1,0,3], 
            [3,3,6,3,0]  ])
# setting distance_threshold=0 ensures we compute the full tree.
models = AgglomerativeClustering(distance_threshold=0, n_clusters=None)

models = models.fit(X)
plt.title('''Hierarchical Clustering Dendrogram
               0-E 1-A 2-C 3-B 4-D ''')
# plot the top three levels of the dendrogram
plot_dendrogram(models, truncate_mode='level', p=3)
plt.xlabel("nodes")
plt.show()
