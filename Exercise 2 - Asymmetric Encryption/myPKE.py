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
            afterM1 = m1[j]
            afterM2 = m2[afterM1-1][i]
            m3[j][afterM2-1] = i+1
    return m3

if(__name__ == '__main__'):
    N = int(sys.argv[1])

m1 = createM1(N)
m2 = createM2(N)
m3 = createM3(m1,m2,N)

print(m1)
print(m2)
print(m3)