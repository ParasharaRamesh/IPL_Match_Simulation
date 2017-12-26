'''
current format 
playername
M,Inn,NO,Runs,HS,Avg,BF,SR,100,200,50,4s,6s
M,Inn,B,Runs,Wkts,BBI,BBM,Econ,Avg,SR,5W,10W
'''

'''
playername,team,mode,M,Inn,NO,Runs,HS,Avg,BF,SR,100,200,50,4s,6s
playername,team,mode,M,Inn,B,Runs,Wkts,BBI,BBM,Econ,Avg,SR,5W,10W
for now no team
'''
#EANF
import csv
l=[]
bat=[]
bowl=[]
with open("pinfoteam.csv",'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        if(len(row)!=0):
            if(row[2]=="bat"):
                print ("bat",row)
                bat.append(row)
            elif(row[2]=="bowl"):
                print ("bowl",row)
                bowl.append(row)
print "done"

with open("pinfobat.csv", "w+") as f:
    writer=csv.writer(f)
    for row in bat:
        writer.writerow(row)

with open("pinfobowl.csv", "w+") as fa:
    writer2=csv.writer(fa)
    for row in bowl:
        writer2.writerow(row)
print "everything put!"
