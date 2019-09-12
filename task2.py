A = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,"K":10,"L":11,"M":12,"N":13,"O":14,"P":15,"Q":16,"R":17,"S":18,"T":19,"U":20,"V":21,"W":22,"X":23,"Y":24,"Z":25}
alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lemon = [alpha.index("L"),alpha.index("E"),alpha.index("M"),alpha.index("O"),alpha.index("N")]
i = 0 
str = ""
inp = input("Enter a string: ")
for a in inp:
    chk = alpha.index(a)
    if i < len(lemon):
        chk = chk + lemon[i]
        if chk > 25:
            chk = chk - 26
        str =str + alpha[chk]
        i =i+1
    else: 
        i = 0
        chk = chk + lemon[i]
        if chk > 25:
            chk = chk - 26
        str =str + alpha[chk]
        i = i+1
print(str)
