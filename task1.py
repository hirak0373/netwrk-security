j= input("press 1 for encryption 2 for decryption: ")
i = input("Enter string: ")
k = int(input("Enter key: "))
str = ""
dstr = ""
if j == '1':
    for a in i:
        a = ord(a)
        if a < 88:
            a = a  + k
            a = chr(a)
            str =str + a
        else:
            a = a + k
            a = a - 26
            a = chr(a)
            str =str + a
    print(str)
if j == '2':
    for a in i:
        
        a = ord(a)
        a = a - k
        if (a < 65):
            a = a + 26
        a = chr(a)
        dstr = dstr + a 
        
    print(dstr)
