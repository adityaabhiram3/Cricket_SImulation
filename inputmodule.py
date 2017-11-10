<<<<<<< HEAD
=======
#test, test successfull
>>>>>>> 213cc8b0c9150833c49b661e18a5eaf474992a2a
import random
import matplotlib.pyplot as plt
overs = int(input("Enter number of overs: "))
balls = 6*overs
wicket = 0
player_names = ['Rohit', 'Dhawan', 'Kohli', 'Jadhav', 'Raina', 'Dhoni', 'Pandya', 'Bhubneswar', 'Bumrah', 'Chahal', 'yadav']
l = list()
e=list()
d=list()
strike = -1
p1pointer = -1
p2pointer = 1
gapcount = 2
player = list()
for q in range(11):
    player.append([])
overlist = list()
p1 = 1
p2 = 2

for i in range(1,balls+1):
    a = random.randrange(-1, 7)
    while a == 5:
        a = random.randrange(-1, 7)
    if a == -1:
        wicket+=1
        # player.append([])
        if strike == -1:
            # print("Player {0} got out".format(p1))
            p1 += gapcount
            p1pointer *= -1
            p2pointer *= -1
            gapcount = 2
        else:
            # print("Player {0} got out".format(p2))
            p2 += 1
            gapcount += 1
        # p1, p2 = p2, p1
        # strike *= -1
    if wicket == 10:
        break
    if a != -1:
        l.append(a)
    if a == -1:
        d.append('w')
        print('w', end = " ")
    else:
        if strike == p1pointer:
            player[p1-1].append(a)  # showing error for some cases
        else:
            player[p2-1].append(a)
        # d.append(a)
        print(a, end = " ")
    if (a%2 == 1) and (a != -1):
        strike *= -1
    if i%6 == 0 :
        e.append(sum(l))
        print("Runs scored this over: ", sum(l))
        # if a%2 == 0:
        strike *= -1
        if strike == -1:
            print("{0} is on strike".format(player_names[p1-1]))
        else:
            print("{0} is on strike".format(player_names[p2-1]))
        print("{0} and {1} are playing".format(player_names[p1-1], player_names[p2-1]))
        l = []
    # if a%2 == 1:
    #     strike *= -1
# print(player)
# print(d)
# print(e)
count = 1
print()
print("_______________________________")
for f in player:
    print("{0} scored {1} runs".format(player_names[count-1], sum(f)))
    count += 1
print("Total score: ", sum(e))
print("Wickets: ", wicket)

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
