#test
import random
import matplotlib.pyplot as plt 
overs = int(input("Enter number of overs: "))
balls = 6*overs
wicket = 0
l = list()
e=list()
d=list()
strike = -1

player = [[], []]
overlist = list()
p1 = 1
p2 = 2

for i in range(1,balls+1):
    a = random.randrange(-1, 7)
    while a == 5:
        a = random.randrange(-1, 7)
    if a == -1:
        wicket+=1
        player.append([])
        if strike == -1:
        	p1 += 2
        else:
        	p2 += 1
    if wicket == 10:
        break
    if a != -1:
        l.append(a)
    if a == -1:
        d.append('w')
        print('w', end = " ")
    else:
    	if strike == -1:
    		player[p1-1].append(a)
    	else:
    		player[p2-1].append(a)
        # d.append(a)
    	print(a, end = " ")
    if i%6 == 0 :
        e.append(sum(l))
        print("Runs scored this over: ", sum(l))
        strike -= -1
        # if strike = 
        if strike == -1:
        	print("Player {0} is on strike".format(p1))
        else:
        	print("Player {0} is on strike".format(p2))
        print("Player {0} and Player {1} are playing".format(p1, p2))
        l = []
    if a%2 == 1:
    	strike -= -1
# print(player)
# print(d)
# print(e)
count = 1
print()
print("_______________________________")
for f in player:
	print("PLayer {0} made {1} runs".format(count, sum(f)))
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
=======
import random
import matplotlib.pyplot as plt 
overs = int(input("Enter number of overs: "))
balls = 6*overs
wicket = 0
l = list()
e=list()
d=list()
strike = -1

player = [[], []]
overlist = list()
p1 = 1
p2 = 2

for i in range(1,balls+1):
    a = random.randrange(-1, 7)
    while a == 5:
        a = random.randrange(-1, 7)
    if a == -1:
        wicket+=1
        player.append([])
        if strike == -1:
        	p1 += 2
        else:
        	p2 += 1
    if wicket == 10:
        break
    if a != -1:
        l.append(a)
    if a == -1:
        d.append('w')
        print('w', end = " ")
    else:
    	if strike == -1:
    		player[p1-1].append(a)
    	else:
    		player[p2-1].append(a)
        # d.append(a)
    	print(a, end = " ")
    if i%6 == 0 :
        e.append(sum(l))
        print("Runs scored this over: ", sum(l))
        strike -= -1
        # if strike = 
        if strike == -1:
        	print("Player {0} is on strike".format(p1))
        else:
        	print("Player {0} is on strike".format(p2))
        print("Player {0} and Player {1} are playing".format(p1, p2))
        l = []
    if a%2 == 1:
    	strike -= -1
# print(player)
# print(d)
# print(e)
count = 1
print()
print("_______________________________")
for f in player:
	print("PLayer {0} made {1} runs".format(count, sum(f)))
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
>>>>>>> a63d23b92b37c56476396863dd06197e539c4357
