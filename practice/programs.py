#convert the string "hello welcome to python" to a comma separated string
'''
var = "hello welcome to python"
res = var.split()
print(','.join(res))
'''
'''
#wap to search for a character and return the corresponding index
var = "hello world"
chr_ = 'l'
def find_index(var,chr_):
    list_ = []
    for i in range(0,len(var)):
        if var[i]==chr_:
            list_.append('character {} is at index {}'.format(chr_,i))

    return list_
print(find_index(var,chr_))

#i/p
sentence = "hello world welcome to python programming hi there"
words = sentence.split()
from collections import defaultdict
d = defaultdict(list)
print(d)
for word in words:
    d[word[0]].append(word)
    print(d)

def positive(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return abs(result)
    return wrapper

@positive
def sub(a,b):
    return a-b

print(sub(1,2))

class Login:
    l_c = 0

    def __init__(self):
        Login.l_c+=1

l1=Login()
print(Login.l_c)
l2=Login()
print(Login.l_c)

s = "hello world"
d = {i:s.count(i) for i in s if s.count(i)>1}
print(d)


s1='listen'
s2='silent'
if sorted(s1)==sorted(s2):
    print('anagram')
'''
var = "aaaabbbyyy"
d = set(var)
#print([''.join((letter,str(var.count(letter)))) for letter in d])

l=[[1,2,3],[4,5,6],[7,8,9]]
l1 = [sum(l[i]) for i in range(len(l))]
#print(l1)

import re
s = 'hello world hello helloworld'
data = re.findall(r'\bhello',s)

print(data)
