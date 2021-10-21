import sys
import random as r

def createM1(N):
    m1 = []
    for i in range(1,N+1):
        m1.append(i)
    r.shuffle(m1)
    return m1
    
def createM2(N):
    m2 = []
    for i in range(0,N):
        m2.append(createM1(N))
    return m2

def createM3(m1,m2,N):
    m3 = [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    #Create empty
    # for i in range(0,N):
    #     for j in range(0,N):
    #         m
    for i in range(0,N):
        for j in range(0,N):
            afterM1 = m1[j]
            afterM2 = m2[afterM1-1][i]
            m3[j][afterM2-1] = i+1
    return m3

N = 5
K = 1
P = 1

#m1 = createM1(N)
m1 = [4, 1, 3, 5, 2]
#m2 = createM2(N)
m2 = [[5, 1, 4, 2, 3],[2, 4, 5, 1, 3],[3, 5, 2, 4, 1],[4, 1, 2, 3, 5],[1, 5, 3, 4, 2]]
m3 = createM3(m1,m2,N)

print(m1)
print(m2)
print(m3)

print(m3[m2[m1[1]][1]][1])