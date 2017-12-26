import random
import csv
batsman={}
bowler={}
cvsc={}
with open("pinfobatcluster5.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        batsman[row[1]]=row[0]
			
with open("pinfobowlcluster5.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        bowler[row[1]]=row[0]

with open("clustervsclusterprobabilities5.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        k=(row[0],row[1])
        cvsc[k]=row[2:]

print "batsman ,bowler,cvs dictionaries created!"
glo=[]

with open('finalmodifiedpvspinfo.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
                r2=int(row[2])
                r3=int(row[3])
                r4=int(row[4])
                r5=int(row[5])
                r6=int(row[6])
                r7=int(row[7])
                r8=int(row[8])
                r12=int(row[12])
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

print  "existing pvsp combinations ka probablities are done at this point!"
with open('rahulpillai.csv', 'rb') as csvfile:#this file is a csv file with all new unseen player pairs which are not available from ball by ball data
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
                l=[]
                l.append(row[0])
                l.append(row[1])
                for x in cvsc[(batsman[row[0]],bowler[row[1]])]:
                        l.append(x)
                glo.append(l)

print "pillai ka additional players ka combo done!"
with open('FinalTotalProbabilities5.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for row in glo:
                print "*"
                writer.writerow(row)
                print "##"
print "final probabilities calculated!!"
#later you should append all the ones pillai sends you ie all the other legal uncalculated stuffs
