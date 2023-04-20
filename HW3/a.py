import numpy as np


def process_input():
    m, s, c = list(map(int, input().strip().split()))
    x = []
    for i in range(c):
        xp = int(input())
        x.append(xp)

    return m, s, c, x


class KMeans:
    def __init__(self, n_clusters, centers=None, max_iter=300):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.centers = centers

    def init_centers(self, X):
        n_samples, n_features = X.shape
        self.centers = X[np.random.choice(
            n_samples, self.n_clusters, replace=False), :]

    def fit(self, X):

        # Initialize cluster centers if not provided
        if self.centers is None:
            self.init_centers(X)

        for i in range(self.max_iter):
            # Assign samples to the nearest center
            distances = np.linalg.norm(
                X[:, np.newaxis, :] - self.centers, axis=2)
            cluster_ids = np.argmin(distances, axis=1)

            # Update centers to be the input points
            for j in range(self.n_clusters):
                if j in cluster_ids:
                    self.centers[j] = X[cluster_ids == j].mean(axis=0)

        self.labels_ = cluster_ids
        self.cluster_centers_ = self.centers


def get_distances(x):
    distances = []
    sum_dist = 0
    for i, num in enumerate(x):
        if i == 0:
            continue
        distances.append((abs(x[i]-x[i-1]), i))
        sum_dist += abs(x[i]-x[i-1])
    return distances, sum_dist


def print_subarr(x, start, end):
    for i in range(start, end+1):
        print(x[i])

def solve_kmeans():
    x = np.array(x)
    # print(x)
    x = x.reshape(-1, 1)

    # Use KMeans to cluster numbers to m clusters
    kmeans = KMeans(n_clusters=m)
    kmeans.fit(x)
    # print(kmeans.cluster_centers_)
    # print(kmeans.labels_)

    # # Select the best cluster centers from the input points
    # distances = kmeans.transform(x)
    # best_centers = x[np.argmin(distances, axis=0)]
    # best_centers = np.double( best_centers)
    # # print(best_centers)

    # kmeans.cluster_centers_ = best_centers
    # labels = kmeans.predict(x)
    # print(labels)

    last_label = 0
    min_index = 0
    summ = 0
    for i, l in enumerate(kmeans.labels_):
        if i == 0:
            last_label = l
            min_index = i
            continue

        if l != last_label:
            summ += x[i-1] - x[min_index] + 1
            # print(f'i = {i}, l = {last_label}, sum = {summ}')
            last_label = l
            min_index = i

    summ += x[-1] - x[min_index] + 1
    print(summ[0])


if __name__ == '__main__':
    m, s, c, x = process_input()
    x = sorted(x)
    distances, sum_dist = get_distances(x)
    distances = sorted(distances, key=lambda t: -t[0])
    
    m_most_distances = distances[:m-1]
    m_most_distances = sorted(m_most_distances, key=lambda t: t[1])
    # print(m_most_distances)
    # print(sum_dist)
    
    summ = 0
    last_index = 0
    for i, d in enumerate(m_most_distances):
        summ += x[d[1]-1] - x[last_index] + 1
        last_index = d[1]
        
    summ += x[-1] - x[last_index] + 1
    print(summ)
    

