import random
overs = int(input("The desired game is of :"))
balls = overs*6
over_rate = []
score_rate = []
wickets = 0
total_score = 0
individual_runs = []
e = []
team = ['Rohit','Dhawan','Kohli','Jadhav','Raina','Dhoni','Pandya','Bhuveneshwar','Bumrah','Chahal','Kuldeep']
fow = []
for i in range(11) :
    individual_runs.append([])
strike = -1
pitch_end1 = 0
pitch_end2 = 1
for i in range(1,balls+1):
    run = random.randrange(-1,7)
    if run == 5 :
        run = random.randrange(-1,7)
    if run == -1 :
        wickets += 1
        score_rate.append('w')
    if run != -1 :
        score_rate.append(run)
        over_rate.append(run)
    if strike == -1 :
        if run == -1 :
            individual_runs[pitch_end1].append(0)
            pitch_end1 = pitch_end2
            strike = 1
            run = 7
        if run%2 == 0 :
            individual_runs[pitch_end1].append(run)
        if run%2 != 0 and run < 6 :
            individual_runs[pitch_end1].append(run)
    if strike == 1 :
        if run == -1 or run == 7 :
            pitch_end2 += 1
            run = 7
        if run%2 == 0 :
            individual_runs[pitch_end2].append(run)
        if run%2 != 0 and run < 6 :
            individual_runs[pitch_end2].append(run)
    if run%2 != 0 and run < 6 :
        strike = strike*(-1)
    if i%6 == 0 :
        strike = strike*(-1)
        print(score_rate,"runs scored in this over is :-",sum(over_rate))
        if strike == 1 :
            print("{0} is on strike".format(team[pitch_end2]) )
        else :
            print("{0} is on strike".format(team[pitch_end1]) )
        total_score += sum(over_rate)
        e.append(sum(over_rate))
        over_rate = []
        score_rate = []
for i in range(wickets+2) :
    print(team[i],':',sum(individual_runs[i]))
    if pitch_end1 != i or pitch_end2 != i :
        fow.append(team[i])
print('total no. of wickets are :',wickets)
print("the total score is :",total_score)
print(fow)   
graph1 = list()
for k in range(1, overs+1):
    graph1.append(sum(e[0:k]))
print(graph1)
plt.plot(graph1)
plt.show()
print()
t = range(1, overs+1)
plt.bar(t, e)
plt.show()
