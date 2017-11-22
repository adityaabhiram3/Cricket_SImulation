# https://github.com/nilay1024/Cricket_project.git

import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import tkinter
import random
import numpy as np
import os
# import matplotlib.pyplot as plt
import time

# Color codes (Unicode values)
heading = "\033[1;32;50m{0}\033[00m"
red="\033[1;37;31m{0}\033[00m"
blue="\033[1;34;49m{0}\033[00m"
green="\033[1;32;47m{0}\033[00m"
magenta="\033[1;35;47m{0}\033[00m"

os.system('clear') # clears the terminal window
print("\n                           ", end = " ")
print(heading.format("CRICKET MATCH SCORECARD\n"))
overs = int(input("The total no. of overs :"))
balls = overs*6
over_rate = [] # contains runs scored in every over
over_rate1 = []
score_rate = []
score_rate1 = []
wickets = 0
wickets1 = 0
total_score = 0 # Total score of team 1
total_score1 = 0 #Total score of team 2
individual_runs = []
individual_runs1 = []
fow = [] # fall of wickets
fow1 = []
e = list() # has the record for every run scored
e1 = list()
team = ['Rohit','Dhawan','Kohli','Jadhav','Raina','Dhoni','Pandya','Bhuveneshwar','Bumrah','Chahal','Kuldeep']
team1 = ['Guptil','Munro','Williamson','Tailor','Latham','DeGrandhome','Southee','Santner','Bolt','Sodhi','Henry']
for i in range(12) :
    individual_runs.append([])
strike = -1
pitch_end1 = 0
pitch_end2 = 1
for i in range(1,balls+1):
    if pitch_end2 > 10: # if more than 10 wickets fell, it breaks out of the loop
        # pitch_end2 -= 1
        break
    if pitch_end1 > 10:
        # pitch_end1 -= 1
        break
    time.sleep(0.1)  # time delay
    run = random.randrange(-1,7)
    while run == 5 :  # run should not be equal to 5
        run = random.randrange(-1,7)
    if run == -1 :  # condition of wicket
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
    if i%6 == 0 : # condition of over completion
        strike = strike*(-1) # strike rotates after every over
        for q in score_rate:
            if q == 'w':
                print(red.format(q), end = " ") # wickets are printed in red
            else:
                print(q, end =" ")
        print(" runs scored in this over is :-",sum(over_rate))
        if strike == 1 :
            print("{0} is on strike".format(team[pitch_end2]) )
        else :
            print("{0} is on strike".format(team[pitch_end1]) )
        total_score += sum(over_rate)
        e.append(sum(over_rate))
        over_rate = []
        score_rate = []
        print("{0} and {1} are playing".format(team[pitch_end1],team[pitch_end2]))
    if wickets == 10:
        for p in range((i//6)+1, overs+1):
            e.append(0)
        overs_played = "{0}.{1}".format((i//6), i%6)
        break
print('__________________________________')
print(red.format("\nTotal Score: "),total_score)
print(red.format('Wickets:' ),wickets)
print(red.format("Net run rate: "),total_score/overs)
print()

# For printing stats of every player along with S/R
if wickets != 10 :
    for i in range(wickets+2) :
        if i != pitch_end1 and i != pitch_end2 :
            fow.append(team[i])
        if len(individual_runs[i]) != 0:
            print(blue.format("{0}: {1} ({2})  Strike rate = {3}".format(team[i], sum(individual_runs[i]), len(individual_runs[i]),round((sum(individual_runs[i])/len(individual_runs[i]))*100, 2 ))))
if wickets == 10:
     for i in range(wickets+1) :
        if i != pitch_end1 and i != pitch_end2 :
            fow.append(team[i])
        if len(individual_runs[i]) != 0:
            print(blue.format("{0}: {1} ({2})  Strike rate = {3}".format(team[i], sum(individual_runs[i]), len(individual_runs[i]),round((sum(individual_runs[i])/len(individual_runs[i]))*100, 2 ))))
# fow.pop(-1)
print()
print("fall of wickets :",fow)
graph1 = list()
graph1.append(0)
for k in range(1, overs+1): # creates a list to be plotted for graph (values of y = list(function(x)))
    graph1.append(sum(e[0:k]))
if wickets == 10:
    print("Overs Played", overs_played)
# print(graph1)
print("__________________________________")

choice1 = input("Press Enter to start second innings")

for i in range(12):
    individual_runs1.append([])
strike = -1
pitch_end1 = 0
pitch_end2 = 1
for i in range(1, balls+1):
    if pitch_end2 > 10:
        # pitch_end2 -= 1
        break
    if pitch_end1 > 10:
        # pitch_end1 -= 1
        break
    time.sleep(0.1)  # time delay
    run = random.randrange(-1, 7)
    while run == 5:  # run should not be equal to 5
        run = random.randrange(-1, 7)
    if run == -1:  # condition of wicket
        wickets1 += 1
        score_rate1.append('w')
    if run != -1:
        score_rate1.append(run)
        over_rate1.append(run)
    if strike == -1:
        if run == -1:
            individual_runs1[pitch_end1].append(0)
            pitch_end1 = pitch_end2
            strike = 1
            run = 7
        if run % 2 == 0:
            individual_runs1[pitch_end1].append(run)
        if run % 2 != 0 and run < 6:
            individual_runs1[pitch_end1].append(run)
    if strike == 1:
        if run == -1 or run == 7:
            pitch_end2 += 1
            run = 7
        if run % 2 == 0:
            individual_runs1[pitch_end2].append(run)
        if run % 2 != 0 and run < 6:
            individual_runs1[pitch_end2].append(run)
    if run % 2 != 0 and run < 6:
        strike = strike*(-1)
    if i % 6 == 0:
        strike = strike*(-1)
        for q in score_rate1:
            if q == 'w':
                print(red.format(q), end=" ")
            else:
                print(q, end =" ")
        print(" runs scored in this over is :-", sum(over_rate1))
        # print(score_rate1,"runs scored in this over is :-",sum(over_rate1))
        if strike == 1:
            print("{0} is on strike".format(team1[pitch_end2]))
        else:
            print("{0} is on strike".format(team1[pitch_end1]))
        total_score1 += sum(over_rate1)
        e1.append(sum(over_rate1))
        over_rate1 = []
        score_rate1 = []
        print("{0} and {1} are playing".format(team1[pitch_end1], team1[pitch_end2]))
    if wickets1 == 10:
        for p in range((i//6)+1, overs+1):
            e1.append(0)
        overs_played1 = "{0}.{1}".format((i//6), i % 6)
        break
print('__________________________________')
print(red.format("\nTotal Score: "), total_score1)
print(red.format('Wickets:'), wickets1)
print(red.format("Net run rate: "), total_score1/overs)
print()
if wickets1 != 10:
    for i in range(wickets1+2) :
        if i != pitch_end1 and i != pitch_end2 :
            fow1.append(team1[i])
        if len(individual_runs1[i]) != 0:
            print(blue.format("{0}: {1} ({2})  Strike rate = {3}".format(team1[i], sum(individual_runs1[i]), len(individual_runs1[i]), round((sum(individual_runs1[i])/len(individual_runs1[i]))*100, 2 ))))
if wickets1 == 10:
    for i in range(wickets1+1) :
        if i != pitch_end1 and i != pitch_end2 :
            fow1.append(team1[i])
        if len(individual_runs1[i]) != 0:
            print(blue.format("{0}: {1} ({2})  Strike rate = {3}".format(team1[i], sum(individual_runs1[i]), len(individual_runs1[i]), round((sum(individual_runs1[i])/len(individual_runs1[i]))*100, 2 ))))
# fow.pop(-1)
print()
print("fall of wickets :", fow1)
graph2 = list()
graph2.append(0)
for k in range(1, overs+1):
    graph2.append(sum(e1[0:k]))
if wickets1 == 10:
    print("Overs Played", overs_played1)
if total_score > total_score1:  # To check which team won
    winner = 'India'
elif total_score1 > total_score:
    winner = 'New Zealand'
else:
    winner = 'noone'
if winner == 'noone':
    print("Match tied")
else:
    print("\n\n {0} WON".format(winner))

# Highest scoring batsman of the winning team gets the man of the match

highest = 0
teamwon = 0

if total_score > total_score1:
    # highest = 0
    for i in range(len(individual_runs)):
        if sum(individual_runs[highest]) < sum(individual_runs[i]):
            highest = i
    print("Man of the match is: ", team[highest])
    # highest = max(sum(individual_runs[i]))
    teamwon = 1
else:
    # highest = 0
    for i in range(len(individual_runs1)):
        if sum(individual_runs1[highest]) < sum(individual_runs1[i]):
            highest = i
    print("Man of the match is: ", team1[highest])
    teamwon = 2

print("__________________________________")

# GUI using TKinter

def graphs():
    plt.plot(graph1)
    plt.plot(graph2)
    plt.xlabel("OVERS")
    plt.ylabel("RUNS")
    plt.title("RUN ANALYSIS")
    # plt.xticks(range(0, overs+1))
    plt.show()
    # print() 
    t = np.arange(1, overs + 1)  # creates an array of integers from 1 to number of overs
    width = 0.35
    # if wickets != 10:
    plt.bar(t, e, width)  # for plotting bar graph
    plt.bar(t + width, e1, width)
    plt.title('Runs per over')
    plt.ylabel('Runs')
    plt.xlabel('Over')
    plt.show()

def motm(x1):
    highest = x1
    if teamwon == 1:
        man = team[highest]
        runs = sum(individual_runs[highest])
        balls = len(individual_runs[highest])
        if balls == 0:
            balls += 1
        strikerate = round((runs/balls)*100, 2)
        sixes = individual_runs[highest].count(6)
        fours = individual_runs[highest].count(4)
    elif teamwon == 2:
        man = team1[highest]
        runs = sum(individual_runs1[highest])
        balls = len(individual_runs1[highest])
        if balls == 0:
            balls += 1
        strikerate = round((runs/balls)*100, 2)
        sixes = individual_runs1[highest].count(6)
        fours = individual_runs1[highest].count(4)
    mainWindow1 = tkinter.Tk()
    mainWindow1.title("Man of the match details")
    mainWindow1.geometry('640x480')
    label = tkinter.Label(mainWindow1, text = "\n\nMan of the match is {0}\n\nRuns Scored: {1}\n Balls Played: {2}\nStrike Rate: {3}\nFours: {4}\nSixes: {5}".format(man, runs, balls, strikerate, fours, sixes))
    label.pack(side = 'top')
    mainWindow1.mainloop()

def playerstats(i, x):
    # highest = i
    if x == 1:
        man = team[i]
        runs = sum(individual_runs[i])
        balls = len(individual_runs[i])
        if balls == 0:
            strikerate = 0
        else:
            strikerate = round((runs/balls)*100, 2)
        sixes = individual_runs[i].count(6)
        fours = individual_runs[i].count(4)
    elif x == 2:
        man = team1[i]
        runs = sum(individual_runs1[i])
        balls = len(individual_runs1[i])
        if balls == 0:
            strikerate = 0
        else:
            strikerate = round((runs/balls)*100, 2)
        sixes = individual_runs1[i].count(6)
        fours = individual_runs1[i].count(4)
    mainWindow3 = tkinter.Tk()
    mainWindow3.title("Player Stats")
    mainWindow3.geometry('640x480')
    label = tkinter.Label(mainWindow3, text = "\n\nName: {0}\n\nRuns Scored: {1}\n Balls Played: {2}\nStrike Rate: {3}\nFours: {4}\nSixes: {5}".format(man, runs, balls, strikerate, fours, sixes))
    label.pack(side = 'top')
    mainWindow3.mainloop()

def getplayer():
    button2 = list()
    mainWindow2 = tkinter.Tk()
    mainWindow2.title("Player Stats")
    mainWindow2.geometry('640x480')
    label = tkinter.Label(mainWindow2, text = "Player Stats\n\n")
    label.pack(side = 'top')
    button11 = tkinter.Button(mainWindow2, text = team[0], command = lambda: playerstats(0, 1))
    button12 = tkinter.Button(mainWindow2, text = team[1], command = lambda: playerstats(1, 1))
    button13 = tkinter.Button(mainWindow2, text = team[2], command = lambda: playerstats(2, 1))
    button14 = tkinter.Button(mainWindow2, text = team[3], command = lambda: playerstats(3, 1))
    button15 = tkinter.Button(mainWindow2, text = team[4], command = lambda: playerstats(4, 1))
    button16 = tkinter.Button(mainWindow2, text = team[5], command = lambda: playerstats(5, 1))
    button17 = tkinter.Button(mainWindow2, text = team[6], command = lambda: playerstats(6, 1))
    button18 = tkinter.Button(mainWindow2, text = team[7], command = lambda: playerstats(7, 1))
    button19 = tkinter.Button(mainWindow2, text = team[8], command = lambda: playerstats(8, 1))
    button20 = tkinter.Button(mainWindow2, text = team[9], command = lambda: playerstats(9, 1))
    button21 = tkinter.Button(mainWindow2, text = team[10], command = lambda: playerstats(10, 1))
    
    button11.pack(side = 'top')
    button12.pack(side = 'top')
    button13.pack(side = 'top')
    button14.pack(side = 'top')
    button15.pack(side = 'top')
    button16.pack(side = 'top')
    button17.pack(side = 'top')
    button18.pack(side = 'top')
    button19.pack(side = 'top')
    button20.pack(side = 'top')
    button21.pack(side = 'top')

    # for i in range(len(team)):
    #     button2.append(i)
    #     button2[i] = tkinter.Button(mainWindow2, text = team[i], command = lambda: playerstats(i))
    #     button2[i].pack(side = 'top')
    mainWindow2.mainloop()

def getplayer1():
    # button2 = list()
    mainWindow4 = tkinter.Tk()
    mainWindow4.title("Player Stats")
    mainWindow4.geometry('640x480')
    label = tkinter.Label(mainWindow4, text = "Player Stats\n\n")
    label.pack(side = 'top')
    button11 = tkinter.Button(mainWindow4, text = team1[0], command = lambda: playerstats(0, 2))
    button12 = tkinter.Button(mainWindow4, text = team1[1], command = lambda: playerstats(1, 2))
    button13 = tkinter.Button(mainWindow4, text = team1[2], command = lambda: playerstats(2, 2))
    button14 = tkinter.Button(mainWindow4, text = team1[3], command = lambda: playerstats(3, 2))
    button15 = tkinter.Button(mainWindow4, text = team1[4], command = lambda: playerstats(4, 2))
    button16 = tkinter.Button(mainWindow4, text = team1[5], command = lambda: playerstats(5, 2))
    button17 = tkinter.Button(mainWindow4, text = team1[6], command = lambda: playerstats(6, 2))
    button18 = tkinter.Button(mainWindow4, text = team1[7], command = lambda: playerstats(7, 2))
    button19 = tkinter.Button(mainWindow4, text = team1[8], command = lambda: playerstats(8, 2))
    button20 = tkinter.Button(mainWindow4, text = team1[9], command = lambda: playerstats(9, 2))
    button21 = tkinter.Button(mainWindow4, text = team1[10], command = lambda: playerstats(10, 2))
    
    button11.pack(side = 'top')
    button12.pack(side = 'top')
    button13.pack(side = 'top')
    button14.pack(side = 'top')
    button15.pack(side = 'top')
    button16.pack(side = 'top')
    button17.pack(side = 'top')
    button18.pack(side = 'top')
    button19.pack(side = 'top')
    button20.pack(side = 'top')
    button21.pack(side = 'top')

    # for i in range(len(team)):
    #     button2.append(i)
    #     button2[i] = tkinter.Button(mainWindow2, text = team[i], command = lambda: playerstats(i))
    #     button2[i].pack(side = 'top')
    mainWindow4.mainloop()

mainWindow = tkinter.Tk() # initialization of a new TKinter window

mainWindow.title("Cricket SCORECARD")
mainWindow.geometry('640x480')
label = tkinter.Label(mainWindow, text = "Cricket SCORECARD\n\n")
label.pack(side = 'top')
B = tkinter.Button(text ="Click to display graphs", command = graphs, activeforeground="red",fg="green",relief="ridge", borderwidth = 2)
B.pack(side = 'top')
x1 = highest
button2 = tkinter.Button(text = "Man of the match stats", command = lambda: motm(x1))
button2.pack(side = 'top')

button3 = tkinter.Button(text = "Team 1 Player Stats", command = getplayer)
button3.pack(side = 'top')

button4 = tkinter.Button(text = "Team 2 Player Stats", command = getplayer1)
button4.pack(side = 'top')


mainWindow.mainloop()

