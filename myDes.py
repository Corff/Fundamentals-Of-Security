#First Task
import sys

def Encode():
    print("Encode", key, input)

def Decode():
    print("Decode", key, input)

if(__name__ == "__main__"):
    encOrDec = str(sys.argv[1])
    key = str(sys.argv[2])
    input = str(sys.argv[3])
    if(encOrDec == "enc"):
        Encode()
    else:
        Decode()
    