from sklearn.cluster import KMeans
import numpy as np


matrix1 =  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

tensor1 = np.array(matrix1)
tensor2 = np.array(matrix2)

combinedData = np.vstack((tensor1, tensor2))

kmeans = KMeans(n_clusters=2, random_state=0)
kmeans.fit(combinedData)

labels = kmeans.labels_
print(labels)
