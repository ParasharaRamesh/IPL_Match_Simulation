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
for x in range(335982,336041): 
    l.append(x)
for x in range(392181,392240): 
    l.append(x)
for x in range(419106,419166): 
    l.append(x)
for x in range(501198,501272): 
    l.append(x)
for x in range(548306,548382): 
    l.append(x)
for x in range(597998,598074): 
    l.append(x)
for x in range(729279,734050): 
    l.append(x)
for x in range(829705,829824): 
    l.append(x)
for x in range(980901,981020): 
    l.append(x)
for x in range(1082591,1082651): 
    l.append(x)
err=[]
for i in l:
    try:
        print "infile no"+str(i)
        with open(str(i)+".csv", 'r') as csvfile:#335932-336040,392181-392239,419106
            csvreader = csv.reader(csvfile, delimiter=',')#[20:50]ie only from the 21st line you start
            for row in csvreader:
                if(row[0]!="ball"):
                    continue
                #if(count==50):
                #    break
                key=row[4]+","+row[6]
                #print key
                run=row[7]
                if(key not in pvp.keys()):
                    pvp[key]={}#dictionary initialization for the bowler he sees the first ball he faces
                    pvp[key]["balls"]=1
                    pvp[key]["0"]=0
                    pvp[key]["1"]=0
                    pvp[key]["2"]=0
                    pvp[key]["3"]=0
                    pvp[key]["4"]=0
                    pvp[key]["5"]=0
                    pvp[key]["6"]=0
                    pvp[key]["dismissals"]=0
                    pvp[key][str(run)]+=1 
                    if(row[10]==row[4]):#if the batsman dismissed is the striker
                        pvp[key]["dismissals"]+=1
                else:
                    pvp[key]["balls"]+=1#for no of runs scored
                    pvp[key][str(run)]+=1
                    if(row[10]==row[4]):
                        pvp[key]["dismissals"]+=1
            print "all mappings done here!"
    except IOError:
        print "this file is not found so trying next one"
        err.append(i)
        continue
			
			
for v in pvp.values():
    v["runs"]=v["1"]+(2*v["2"])+(3*v["3"])+(4*v["4"])+(5*v["5"])+(6*v["6"])
    v["strikerate"]=(v["runs"]*100)/float(v["balls"])

for e in err:
    print "error"+str(e)
f=open("pvspinfo.csv", "w+")
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
