from collections import *

'''
#if the specified key is not present then it will show error
var = {'a':1,'b':2, 'c':3}
print(var['d'])
'''
'''
#In order to overcome this problem we have to make use of defaultdict
#lets create a function
def def_value():
    return "Not Present"

d = defaultdict(def_value)
d['a']=1
d['b']=2

print(d['a'])
print(d['b'])
print(d['c'])
'''
'''
#by using lambda function
d = defaultdict(lambda :"not present")
d['a']=1
d['b']=2
print(d['a'])
print(d['b'])
print(d['c'])
'''
'''
#__missing__ is used to give the default value 
d = defaultdict(lambda: "Not Present")
d["a"] = 1
d["b"] = 2

# Provides the default value
# for the key
print(d.__missing__('a'))
print(d.__missing__('d'))
'''
'''
#default value as an list
#When the list class is passed as the default_factory argument,
#then a defaultdict is created with the values that are list.
d = defaultdict(list)

for i in range(0,5):
    d[i].append(i)

print(d['a'])
'''
'''
#default value as int
#when we pass int class as the default_factory argument
#then the defaultdict is created with default value as 0
d = defaultdict(int)
l = [1,2,3,1,2,3,1,4]
for i in l:
    d[i] +=1

print(d)
'''
####counter
#print(Counter(['b','b','a','b','c','a','b','a','c','a','b','c']))

#print(Counter({'a':5,'b':2,'c':3}))

#print(Counter(A=5,B=3,C=7))

#deque

queue = deque(['name','age','dob'])
#print(queue)
'''
#inserting the elements
de = deque([1,2,3])
de.append(4)
print(de)

de.appendleft(6)
print(de)
'''

#removing elements

de = deque([6,7,1,2,3,4,9])
print(de.pop())
print(de.popleft())