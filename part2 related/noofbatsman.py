import csv

batcount={}
with open('pinfobatcluster.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        if(row[2] not in batcount.keys()):
            batcount[row[2]]=0
        else:
            batcount[row[2]]+=1
            

print batcount
