i = input("Enter string: ")
str = ""
for a in i:
    a = ord(a)
    if a < 88:
        a = a  + 3
        a = chr(a)
        str =str + a
    else:
        a = a + 3
        a = a - 26
        a = chr(a)
        str =str + a
print(str)