import csv
teams=[]
existingcombos=[]
with open('teaminfo.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
                l=[]
                l.append(row[0])
                l.append(row[1])
                teams.append(l)
                
with open('finalmodifiedpvspinfo.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
                l=[]
                l.append(row[0])
                l.append(row[1])
                existingcombos.append(l)
bowler={}
with open("pinfobowlcluster.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        bowler[row[1]]=row[0]

newcombos=[]
#get all combos
for player in teams:
    for otherplayer in teams:
        if(player[1]!=otherplayer[1]):
            temp=[]
            temp.append(player[0])
            temp.append(otherplayer[0])
            newcombos.append(temp)


actualcombos=[]
for combo in newcombos:
    if combo[1] in bowler.keys():
        if combo not in existingcombos:
            actualcombos.append(combo)


with open('rahulpillai.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for row in actualcombos:
                print "*"
                writer.writerow(row)
                print "##"
print len(actualcombos)


