#First Task
import sys

#Round Keys
P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
LS1 = [2, 3, 4, 5, 1]
LS2 = [3, 4, 5, 1, 2]
P8  = [6, 3, 7, 4, 8, 5, 10, 9]

#Enc/Dec Perm Tables
IP  = [2, 6, 3, 1, 4, 8, 5, 7]
IP1 = [4, 1, 3, 5, 7, 2, 8, 6]
EP  = [4, 1, 2, 3, 2, 3, 4, 1]
P4  = [2, 4, 3, 1]

#S Tables
sZero = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
sOne  = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]


def createRoundKeys(key):
    k1 = None
    k2 = None
    Permutate(key,P10)


    return [k1,k2]

def Permutate(input, table):

    return permutatedArray

def Encode():
    print("Encode", key, input)

def Decode():
    print("Decode", key, input)













if(__name__ == "__main__"):
    encOrDec = str(sys.argv[1])
    key = list(str(sys.argv[2]))
    input = list(str(sys.argv[3]))
    if(encOrDec == "enc"):
        Encode()
    else:
        Decode()
    