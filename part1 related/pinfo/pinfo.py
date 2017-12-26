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
with open("profiles.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        temp=[]
        if(row[1]==''):
            name=row[0]
        elif(row[12]==''):
            alleanf=True
            for i in range(0,13):
                if(row[i]!="#EANF#"):
                    alleanf=False
                    break
            if(alleanf==False):
                temp.append(name)
                temp.append("bowl")
                for i in range(0,12):
                    temp.append(row[i])
                print temp
                l.append(temp)
                temp=[]
            else:
                continue
        else:
            alleanf=True
            for i in range(0,13):
                if(row[i]!="#EANF#"):
                    alleanf=False
                    break
            if(alleanf==False):
                temp.append(name)
                temp.append("bat")
                for i in range(0,13):
                    temp.append(row[i])
                print temp
                l.append(temp)
                temp=[]
            else:
                continue
			
			

f=open("pinfofinal.csv", "w+")
with f:
    writer=csv.writer(f)
    for row in l:
        writer.writerow(row)
