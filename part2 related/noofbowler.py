import csv

bowlcount={}
with open('pinfobowlcluster.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        if(row[2] not in bowlcount.keys()):
            bowlcount[row[2]]=0
        else:
            bowlcount[row[2]]+=1
            

print bowlcount
