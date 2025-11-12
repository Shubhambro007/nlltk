import pandas as pd
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import linkage, fcluster
from sklearn.preprocessing import StandardScaler

def kmeans(filepath, col, n_clusters=3):
    df = pd.read_csv(filepath)
    X = df[[col]].dropna().values
    Xs = StandardScaler().fit_transform(X)
    kmeans = KMeans(n_clusters=n_clusters, random_state=0)
    df['cluster'] = kmeans.fit_predict(Xs)
    return df[['cluster'] + [col]]

def hierarchical(filepath, col, n_clusters=3):
    df = pd.read_csv(filepath)
    X = df[[col]].dropna().values
    Xs = StandardScaler().fit_transform(X)
    Z = linkage(Xs, method='ward')
    df['cluster'] = fcluster(Z, n_clusters, criterion='maxclust')
    return df[['cluster'] + [col]]
