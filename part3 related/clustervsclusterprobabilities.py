import random
import csv


import csv

glo=[]

with open('clustervsclusterstats5.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
                r2=float(row[2])
                r3=float(row[3])
                r4=float(row[4])
                r5=float(row[5])
                r6=float(row[6])
                r7=float(row[7])
                r8=float(row[8])
                r12=float(row[12])
                r9=float(row[9])
                r2/=r9
                r3/=r9
                r4/=r9
                r5/=r9
                r6/=r9
                r7/=r9
                r8/=r9
                r12/=r9
                l=[]
                l.append(str(row[0]))
                l.append(str(row[1]))
                l.append(str(r2))
                l.append(str(r3))
                l.append(str(r4))
                l.append(str(r5))
                l.append(str(r6))
                l.append(str(r7))
                l.append(str(r8))
                l.append(str(r12))
                l.append(str(row[9]))
                glo.append(l)
                



with open('clustervsclusterprobabilities5.csv', 'w') as csvfile:
	writer = csv.writer(csvfile, delimiter=',')
	for row in glo:
		writer.writerow(row)



'''
print "s"
f=open("clustervsclusterprobabilities.csv", "w+")
with f:
    writer=csv.writer(f)
    for row in w:
        writer.writerow(row)
        print "aat!"
print "done!"
'''
