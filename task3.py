alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
M1 =    ["A","S","D","F","G","H","J","K","L","P","O","I","U","Y","T","R","E","W","Q","Z","X","C","V","B","N","M"]
M2 =    ["Q","A","Z","W","S","X","E","D","C","R","F","V","T","G","B","Y","H","N","U","P","J","M","I","K","O","L"]
M3 =    ["Z","X","C","V","B","N","M","K","I","O","P","L","U","J","H","Y","T","G","F","R","E","D","S","W","Q","A"]
str = ""
dstr = ""
j= input("press 1 for encryption 2 for decryption: ")
inp = input("Enter a string: ")
chk1 = False
chk2 = False
chk3 = False
if j == '1':
    for a in inp:
        chk = alpha.index(a)
        if chk1 == False:
            s = M1[chk]
            str =str + s
            chk1 = True
    #        chk2 = False
        elif chk2 == False:
            s = M2[chk]
            str =str + s
            chk2 = True
    #        chk3 = False
        elif chk3 == False:
            s = M3[chk]
            str =str + s
            chk1 = False
            chk2 = False
    print(str)
if j == '2':
    for a in inp:
        if chk1 == False:
            chk = M1.index(a)
            s = alpha[chk]
            dstr =dstr + s
            chk1 = True
        elif chk2 == False:
            chk = M2.index(a)
            s = alpha[chk]
            dstr =dstr + s
            chk2 = True
        elif chk3 == False:
            chk = M3.index(a)
            s = alpha[chk]
            dstr =dstr + s
            chk1 = False
            chk2 = False
    print(dstr)

