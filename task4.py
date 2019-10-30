import numpy as np 
from collections import OrderedDict
keyf = []

cipher = []
plantext = "yesssai"
def message_to_digraphs(message_original):
    message = []
    message_original=message_original.upper()
    message_original = message_original.replace(" ", "")
    i=0
    for a in message_original:
        message.append(a)
    j=len(message)
    j=j//2
    
    for a in range(j):
        if message[i] == message[i+1]:
            message.insert(i+1,'X')
        i=i+2
    if len(message)%2 == 1:
        message.append('X')
    i = 0
    new = []
    j = len(message)//2+1
    for x in range(1,j):
        new.append(message[i:i+2])
        i=i+2
    print("BIGRAMS: ",new)
    return new

   

# remove duplicate characters
def remove_duplicate(key):
    return "".join(OrderedDict.fromkeys(key))


# remove spaces convert text in upper case , replace j with i and append key with ABCD
def key_merge(key):
    key = key.replace(" ","")
    key = key.upper()
    key = key + "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = key.replace("j","i")
    key1=remove_duplicate(key)
    
    for a in key1:
        keyf.append(a)
#    print(keyf)
    return keyf
    


# making 5 by 5 matrix and insert values in it    
def matrix(key):
    key = key_merge(key)
    matrix1 = np.array(key).reshape(5,5) 
    print("MATRIX: \n",matrix1)
    return matrix1


def postion(matrix,a):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == a:
                x=i
                y=j
    return x,y

def encrypt(key ,message):
    print("KEY: ", key)
    print("PLAIN TEXT: ",message)
    matrix1 = matrix(key)
    message = message_to_digraphs(message)
    

    for a in message:
        x1,y1 = postion(matrix1,a[0])
        x2,y2 = postion(matrix1,a[1])
        if x1 == x2:
            if y1 == 4:
                y1 = -1
            if y2 == 4:
                y2 = -1
            cipher.append(matrix1[x1][y1+1])
            cipher.append(matrix1[x1][y2+1])
        elif y1 == y2:
            if x1 == 4:
                x1 = -1
            if x2 == 4:
                x2 = -1
            cipher.append(matrix1[x1+1][y1])
            cipher.append(matrix1[x2+1][y2])
        else:
            cipher.append(matrix1[x1][y2])
            cipher.append(matrix1[x2][y1])
    ot = ""        
    for e in cipher:
        ot =ot+e
    print(cipher) 
    return ot.lower()
    

def decrypt(key, message):
    print("KEY: ", key)
    print("CIPHER: ",message)
    matrix1 = matrix(key)
    message = message_to_digraphs(message)
    

    for a in message:
        x1,y1 = postion(matrix1,a[0])
        x2,y2 = postion(matrix1,a[1])
        if x1 == x2:
            if y1 == 4:
                y1 = -1
            if y2 == 4:
                y2 = -1
            cipher.append(matrix1[x1][y1-1])
            cipher.append(matrix1[x1][y2-1])
        elif y1 == y2:
            if x1 == 4:
                x1 = -1
            if x2 == 4:
                x2 = -1
            cipher.append(matrix1[x1-1][y1])
            cipher.append(matrix1[x2-1][y2])
        else:
            cipher.append(matrix1[x1][y2])
            cipher.append(matrix1[x2][y1])
    for a in cipher:
        if a == 'X':
            cipher.remove('X')
    ot = ""
    for e in cipher:
        ot =ot+e
    return ot.lower()

            




#print(message_to_digraphs(plantext))
#merge("python exercises practice solution")
s = input("For encryption press1 and for decryption press 2: ")
key = input("Enter key: ")
msg=input("Enter msg: ")
if s == '1':
    print("CIPHER TEXT: ",encrypt(key,msg))
if s == '2':
    print("plain TEXT: ",decrypt(key,msg))