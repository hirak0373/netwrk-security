import numpy as np
pl = []
kl = []
def encrypt():
    for a in plaintxt:
        pl.append(a)
    while(True):
        if len(pl)%depth == 0:
            break
        else:
            pl.append('X')
    for a in range(depth):
        k = a
        for b in range(len(pl)//depth):
            kl.append(pl[k])
            k=k+depth


    matrix1 = np.array(kl).reshape(depth,len(pl)//depth)
    print(matrix1)
def decrypt():
    for a in plaintxt:
        pl.append(a)
    
    print(pl)
    for a in range(len(pl)//depth):
        k = a
        j=len(pl)//depth
        for b in range(depth):
            kl.append(pl[k])
            k=k+j
    for a in kl:
        if a == 'X':
            kl.remove('X')
    kl.remove('X')
    print(kl)
ch=input("Press 1 for encryption and 2 for decryption: ")
depth = int(input("Enter depth: "))
plaintxt = input("Enter string: ")

if ch == '1':
    encrypt()
elif ch == '2':
    decrypt()





'''
for a in range(depth):
    k = "l",a
    k = []
for a in range(0,depth):
    k = a
    for b in range(len(pl)//depth):
        
        "l",a.append()
        k = k + depth

for i in range(depth):
    k="l",i
    print(k)
'''