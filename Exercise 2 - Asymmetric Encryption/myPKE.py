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
    #Create empty
    m3 = []
    for i in range(0,N):
        temp = []
        for j in range(0,N):
            temp.append(0)
        m3.append(temp)

    for i in range(0,N):
        for j in range(0,N):
            afterM1 = m1[j]-1
            afterM2 = m2[afterM1][i]-1
            m3[afterM2][j] = i+1
    return m3

#if(__name__ == '__main__'):
    N = int(sys.argv[1])

m1 = [4, 1, 3, 5, 2]
m2 = [[5, 1, 4, 2, 3],[2, 4, 5, 1, 3],[3, 5, 2, 4, 1],[4, 1, 2, 3, 5],[1, 5, 3, 4, 2]]
N = 5

#m1 = createM1(N)
#m2 = createM2(N)
m3 = createM3(m1,m2,N)

#print(m1)
#print(m2)
#print(m3)

k = 1
p = 2

A = m1[k-1]
print(A)
B = m2[A-1][p-1]
print(B)
C = m3[B-1][k-1]
print(C)
