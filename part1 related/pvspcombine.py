'''
batsman,bowler,0s,1s,2s,3s,4s,5s,6s,#dismissals,total_runs,balls,strikerate
'''

'''
key:batsman
value:list of lists (where each list is for vs one partiicular bowler)
each list in that list of lists let it have the following format
[bowler_name,0s,1s,2s,3s,4s,5s,6s,#balls,#dismissals]
'''

'''
csv format
0    1         2     3           4       5          6      7      8     9                    10
ball,inningsno,over,battingteam,striker,nonstriker,bowler,runs,extras,mode_of_dismissal,batsman_out
'''
import csv
pvp={}
l=[]
with open("pvspinfo.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        key=row[0]+","+row[1]
        print key
        if(key not in pvp.keys()):
            pvp[key]={}
            pvp[key]["balls"]=row[9]
            pvp[key]["0"]=row[2]
            pvp[key]["1"]=row[3]
            pvp[key]["2"]=row[4]
            pvp[key]["3"]=row[5]
            pvp[key]["4"]=row[6]
            pvp[key]["5"]=row[7]
            pvp[key]["6"]=row[8]
            pvp[key]["runs"]=row[10]
            pvp[key]["dismissals"]=row[12]
        else:
            pvp[key]["balls"]+=row[9]
            pvp[key]["0"]+=row[2]
            pvp[key]["1"]+=row[3]
            pvp[key]["2"]+=row[4]
            pvp[key]["3"]+=row[5]
            pvp[key]["4"]+=row[6]
            pvp[key]["5"]+=row[7]
            pvp[key]["6"]+=row[8]
            pvp[key]["runs"]+=row[10]
            pvp[key]["dismissals"]+=row[12]
            
			
			
for v in pvp.values():
    v["strikerate"]=(float(v["runs"])*100)/float(v["balls"])

f=open("pvspinfofinal.csv", "w+")
with f:
    writer=csv.writer(f)
    for k,v in pvp.iteritems():
        row=[]
        temp=k.split(",")
        row=temp[:]
        row.append(v["0"])
        row.append(v["1"])
        row.append(v["2"])
        row.append(v["3"])
        row.append(v["4"])
        row.append(v["5"])
        row.append(v["6"])
        row.append(v["balls"])
        row.append(v["runs"])
        row.append(v["strikerate"])
        row.append(v["dismissals"])
        writer.writerow(row)
