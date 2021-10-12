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
    key = Permutate(key,P10)    #Permutated with P10
    keyL = key[0:5]             #Left side of the key
    keyR = key[5:]              #Right side of the key
    #k1 Working
    keyL1 = Permutate(keyL,LS1) #Left side of key permutated with LS1
    keyR1 = Permutate(keyR,LS1) #Right side of key permutated with LS1
    k1 = keyL1 + keyR1          #Merge keys
    k1 = Permutate(k1, P8)      #Merged key permutated with P8
    k1                          #k1 Calculated
    #k2 Working
    keyL2 = Permutate(keyL1,LS2)#Left side of keyL1 permutated with LS2
    keyR2 = Permutate(keyR1,LS2)#Right side of keyR1 permutated with LS2
    k2 = keyL2 + keyR2          #Merge Keys
    k2 = Permutate(k2,P8)       #Merged key permutated with p8
    k2                          #k2 Calculated
    return [k1,k2]

def Permutate(input, table):
    permutatedString = ""        #Initial empty string
    for i in range(len(table)): #loops through the permutation table
        newIndex = table[i]-1   #gets the new index for the input
        permutatedString = permutatedString + input[newIndex] #adds the letter at the new index to the empty string
    return permutatedString      #final result is permutated string

def sTable(input, table):
    row = input[0] + input[3] #takes first and last digit for the row
    col = input[1] + input[2] #takes second and third digit for the column
    row = int(row,2)          #gets integer value from binary
    col = int(col,2)
    return table[row][col]    #returns value in position

def fFunction(input,key):
    inputEP = Permutate(input,EP)
    XOR = int(inputEP,2) ^ int(key,2)
    XOR = '{0:0{1}b}'.format(XOR,len(key))
    XORleft = XOR[0:4]
    XORright = XOR[4:]
    s0 = '{0:0{1}b}'.format(sTable(XORleft,sZero),2)
    s1 = '{0:0{1}b}'.format(sTable(XORright,sOne),2)
    merged = s0 + s1
    output = Permutate(merged,P4)
    return output

def Encode(key, input):
    roundKeys = createRoundKeys(key)        #[k1, k2]
    input = Permutate(input,IP)             #Applies IP permutation to the input
    inputL = input[0:4]                     #Left side of input
    inputR = input[4:]                      #Right side of input
    input3 = fFunction(inputR,roundKeys[0]) #Right side of input after the function
    inputLXOR3 = '{0:0{1}b}'.format(int(inputL,2) ^ int(input3,2),4) #XOR of inputL and output of function(input3)

    inputL = inputR
    inputR = inputLXOR3
    input3 = fFunction(inputR,roundKeys[1])
    inputLXOR3 = '{0:0{1}b}'.format(int(inputL,2) ^ int(input3,2),4)

    merged = str(inputLXOR3) + str(inputR)
    output = Permutate(merged,IP1)
    return output


def Decode(key, input):
    roundKeys = createRoundKeys(key)
    input = Permutate(input,IP)             #Applies IP permutation to the input
    inputL = input[0:4]                     #Left side of input
    inputR = input[4:]                      #Right side of input
    input3 = fFunction(inputR,roundKeys[1]) #Right side of input after the function
    inputLXOR3 = '{0:0{1}b}'.format(int(inputL,2) ^ int(input3,2),4) #XOR of inputL and output of function(input3)

    inputL = inputR
    inputR = inputLXOR3
    input3 = fFunction(inputR,roundKeys[0])
    inputLXOR3 = '{0:0{1}b}'.format(int(inputL,2) ^ int(input3,2),4)

    merged = str(inputLXOR3) + str(inputR)
    output = Permutate(merged,IP1)
    return output

if(__name__ == "__main__"):
    encOrDec = str(sys.argv[1])
    keyIn = str(sys.argv[2])     #0110100111
    inputIn = str(sys.argv[3])   #01000101
    if(encOrDec == "enc"):
        print(Encode(keyIn, inputIn))
    else:
        print(Decode(keyIn, inputIn))
    

#python myDes.py enc 0110100111 01000101
#>> 01001100
#
#python myDes.py dec 0110100111 01001100
#>> 01000101