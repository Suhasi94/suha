# n = int(input("enter the number: "))
# s = "suhasini"
# for i in range(n):
#     a = s[0]
#     b = s[1:len(s)]
#     s = b + a
# print(s)
# ###############################################
s = 0
l = [[1,2,3],[4,5,6],[7,8,9]]
for i in l:
    if not isinstance(i,int):
        for j in i:
            s += j
    else:
        s += i
print(s)
