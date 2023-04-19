from sklearn.cluster import KMeans
import numpy as np

def process_input():
    m, s, c = list(map(int,input().strip().split()))
    x = []
    for i in range(c):
        xp = int(input())
        x.append(xp)
        
    return m, s, c, x



if __name__ == '__main__':
    m, s, c, x = process_input()
    x = np.array(x)
    print(x)
    x = x.reshape(-1, 1)
    
    # Use KMeans to cluster numbers to m clusters
    kmeans = KMeans(n_clusters=m, random_state=0, n_init='auto').fit(x)
    # print(kmeans.cluster_centers_)
    print(kmeans.labels_)
    
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
            print(f'i = {i}, l = {last_label}, sum = {summ}')
            last_label = l
            min_index = i
            
    summ += x[-1] - x[min_index] + 1
    print(summ)

