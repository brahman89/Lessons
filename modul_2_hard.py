import random
def rock():
    r = 20
    R1 = list(range(3, r+1))
    r = random.choice(R1)
    return r
rock()

from operator import truediv

n = rock()
L1 = list(range(1, n + 1))
L2 = []
VS = []
VS2 = []
LS = []
J = []
D = {}
for i in L1:
    for j in range(1, n + 1):
        n1 = L1[i - 1]
        n2 = j
        n3 = n1 + n2
        J.append(j)
        L2.append(n3)
        VS.append([L1[i - 1],j])
#print(VS)
#print(range(len(VS)))

from collections import defaultdict
D = defaultdict(list)
for k, v in zip(L2, VS):
    D[k].append(v)

#print(J)
#print(VS)
#print(L2)
print(D)
for s in D:




