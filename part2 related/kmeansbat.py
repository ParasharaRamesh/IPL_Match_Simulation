import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import csv

#this is the list holding all the original data from the pinfobat.csv
actual=[]
#this is the list holding only the numeric data from each row ie from index 3 onwards
bat=[]
with open('pinfobat.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for row in reader:
		actual.append(row)
		bat.append(map(float,row[3:]))



X = np.array(bat)
kmeans = KMeans(verbose=False,n_clusters=5,init='k-means++',max_iter=1000)
kmeans.fit(X)
#these are numpy arrays
centroids = kmeans.cluster_centers_
labels = kmeans.labels_
#converting into python lists
cent=centroids.tolist()
lab=labels.tolist()

#prepending the cluster no for each row in these lists
for i in range(len(lab)):
	actual[i]=[str(lab[i])]+actual[i]


for i in range(len(cent)):
	cent[i]=[i]+cent[i]
	
print"we have all the neccessary information ready now!"
with open('pinfobatcluster5.csv', 'w') as csvfile:
	writer = csv.writer(csvfile, delimiter=',')
	for row in actual:
		writer.writerow(row)
print "done with the batsman cluster info!"
with open('batclusterinfo.csv', 'w') as csvfile:
	writer = csv.writer(csvfile, delimiter=',')
	for row in cent:
		writer.writerow(row)
print "finished cluster info!"
