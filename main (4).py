from random import random
N = 5
a = []
k = []
for i in range(N):
    z = []
    for j in range(N):
        n = int(random()*100)
        print('%4d' % n, end='')
        z.append(n)
    print()
    a.append(z)
print()

for i in range(N):
    z = []
    for j in range(N):
        n = int(random()*100)
        print('%4d' % n, end='')
        z.append(n)
    print()
    k.append(z)
print()

for i in range(N):
    for j in range(N):
        if k[i][j]>a[i][j]:
            n = k[i][j]
        else:
            n = a[i][j]
        print('%4d' % n, end='')
    print()
    