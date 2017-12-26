steps to do for ipl part 4 simulation:

1.we firstly need to "fake" that we loaded all the csv files are loaded from hbase.
2.we need a csv file of this format:
	player name,team,role     (role is just either batsman or bowler)
	this file should have only the playing 11 of each team (either do it manually or pick it up from the other files from before)
3.so we when simulating we can only select those rows from this csv file with the players of the 2 playing teams.
4.we simulate the match as per the flow chart shown in the slide by maintaining a datastructure for scoreboard and all the other match information.
5.for each ball we have to make 2 different calculations and then make a final prediction:
	a.simulating wickets
	b.simulating runs

5a:SIMULATING WICKETS:

for each batsman,bowler pairs we only need the pdissmissals for this.
firstly we need to access the batting average of each batsman say BAi and store it somewhere and the use this to compute the (1-threshold value) for each batsman BTi.
(where BTi=(BAi/BAmax)-0.01) so for a good batsman like kohli has a high batting average so his (1-threshold) value will be close to 1 therefore his threshold will be close to 0 but not exactly 0.
so for good batsman like him that would mean that he takes a very long time to get out as it would take many balls for his survival probability to go below the threshold value.

(NOTE IF SIMULATION FAILS THEN WE DONT HAVE ENOUGH ROWS IN FinalTotalProbabilities!!!!)
(NOTE PROVIDE OPTION TO GO BALL BY BALL OR SIMULATE 1 OR 5 OVERS)
(NOTE FOR FAIR SIMULATION REASSIGN THE PROBABILITIES PROPERLY)
refer the slides for understanding how this is calculated


5b:SIMULATING RUNS:
for each batsman,bowler pair we have row of probabilities ie (p0,p1,p2......p6)
so we first generate a random probability number between 0 and 1 say x.we then bucketize all the probabilities using a cummulative probability and then see in which bucket does x fall in . that is the run being scored eg
kohli vs dalesteyn
prob       cummulativeprob
p0=0.1      0.1
p1=0.2      0.3
p2=0.15     0.45
p3=0.15     0.6
p4=0.1      0.7
p5=0.2      0.9
p6=0.1      1.0

 so if the random number x=0.5 ==> a 3 has been scored!


FINAL PREDICTION:
we give higher priority to a fall of a wicket when compared to scoring runs. ie the moment the survival probability goes below the threshold then immeadiately our prediction will be that a wicket has fallen
 if this threshold is not yet met then we compute the probability of scoring runs as usual)
 
6.Extra things which will make the simulation look good.

	.have a list of predetermined  commentries and choose one at random when a batsman hits a 4 or a 6 or becomes out.
	eg "thats a cracking shot through the covers and it has gone all the way to the boundary" or " that has gone through the gates and bowled him clean! thats a cracker of a delivery  " etc
	.let the user select 2 teams and the home ground
	. add a dummy pitch analysis , in pretty much the same way as we add commentriesie by hard coding the values.
	.the state of the scoreboard should be printed after each ball.
	.have a MOM ceremony where we select the best player from the winning team with either the highest runs or best bowling figures. and simulate a small conversation of 4 sentences between them in the same way as we did for commentries.
	
7. to do all this i think it wont take more than 2.5 days so since the submission is on the week of Nov 27 till Dec 2 . so i propose we start this on say 19th or 20th  and finish it off or If i do it alone i can finish it in 2 days tops and then i can explain it to you guys.either way works
8. make them play in pes and have 2 bowling ends as KVS end and Dinkar end 
