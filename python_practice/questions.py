'''#Write a program to find the length of the string without using inbuilt function (len)**
def len_(iterable):
    count_ = 0
    for i in iterable:
        count_ += 1
    return count_

#print(len_('hai'))
#print(len_([1,2,3,4,5]))

#Write a program to reverse a string without using any inbuilt functions.**
def reverse_str(var):
    res=''
    for i in var:
        res=i+res
    return res

#print(reverse_str('hello world'))

#Write a program to replace one string with another. e.g. "Hello World" replace "World" with "Universe"
s = 'hello world'
#print(s.replace('world','universe'))

#How to convert a string to a list and vice-versa
def convert_to_string(any_list):
    return ''.join(any_list)

def convert_to_list(any_str):
    return any_str.split()

#print(convert_to_string(['hello','world']))
#print(convert_to_list('hello'))

#Covert the string "Hello welcome to Python" to a comma separated string.**
s = "Hello welcome to Python"
var = s.split()
#print(','.join(var))

#Write a program to print alternate characters in a string
s = 'hello world'
#print(s[0::2])

#Write a Program to print ascii values of the characters present in a string
'''
'''
s='hello'
for i in s:
    print(ord(i))


#Write program to convert upper case to lower case and vice-versa without using inbuilt method.

def convert(any_str):
    res = ''
    for i in any_str:
        if 'A'<=i<='Z':
            res+=chr(ord(i)+32)
        elif 'a'<=i<='z':
            res+=chr(ord(i)-32)

        else:
            res+=i

    return res

#print(convert('HeLlo WOrld'))

#Write program to swap two numbers without using 3rd variable.
a = 10
b = 20
a,b = b,a
#print(a,b)

#Write program to merge two different lists
a = [1,2,3]
b = [4,5,6]
#print(a+b)
#print([*a, *b])

#Write program to read a random line in a file. (ex. 50, 65, 78th line)

#Write a program to check if the given string is Palindrome or not without using reversed method
def is_palindrome(str1):
    if str1 == str1[::-1]:
        return True
    else:
        return False
#print(is_palindrome('racecar'))
#print(is_palindrome('hello'))

#Write a program to search for a character in a given string and return the corresponding index.

def search(str1,key):
    for index,value in enumerate(str1):
        if value == key:
            print(f'character {value} at index {index}')

#search('hello world','l')

#Write a program to get the below output**
sentence = "hello world welcome to python programming hi there"
#d = {'h': ['hello', 'hi'], 'w': ['world', 'welcome'], 't': ['to', 'there'], 'p': ['python', 'programming'] }
from collections import defaultdict
l = sentence.split()
d = defaultdict(list)
for i in l:
    d[i[0]].append(i)

#print(d)

#Write a to replace all the characters with - if the character occurs more than once in a string
s = 'hello world'
#print(''.join(['-' if s.count(i)>1 else i for i in s]))


#write a decorator that returns only positive values of subtraction
def positive(func):
    def inner(*args, **kwargs):
        res = func(*args, **kwargs)
        return abs(res)
    return inner

@positive
def sub(a,b):
    return a-b

#print(sub(-9,5))

#How to get the count of number of instances of a class that is being created.
class Sample:
    login_count = 0
    def __init__(self):
        Sample.login_count +=1

s1=Sample()
#print(Sample.login_count)
s2=Sample()
#print(Sample.login_count)

#Write a function which takes a list of strings and integers.If the item is a string it
#should print as is and if the item is integer of float it should reverse it.
['apple', 'yahoo', '1234', 100, 123.76, '26.23']

def sample(l1):
    res = []
    for i in l1:
        if type(i) in [int,float]:
            res.append(str(i)[::-1])

        else:
            res.append(i)

    return res

#print(sample(['apple', 'yahoo', '1234', 100, 123.76, '26.23']))

#Write a class named Simple and it should have iteration capability.**`
class Simple:
    def __init__(self, items):
        self._items = items

    def __iter__(self):
        return iter(self._items)

s = Simple([1, 2, 3, 4, 5])

for i in s:
    print(i)

#Write a Custom class which can access the values of dictionaries using d['a'] and d.a"

class Mydict:

    def __init__(self,d):
        self.dict_ = d

    def __getitem__(self, item):
        return self.dict_[item]

    def __getattr__(self, name):
        return self.dict_[name]

d = Mydict({'a':1,'b':2})

# Write a python program to get the below output*
sentence = "Hi How are you"
#o/p should be "iH woH era uoy"
l = sentence.split()
res = []
for i in l:
    res.append(i[::-1])

#print(" ".join(res))

# Write a python program to get the below output
sentence = "Hi How are you"
#o/p should be "ouy era woH iH"

res=''
for i in sentence:
    res=i+res
#print(res)

#Write a lambda function to add two numbers (a, b)

add = lambda x,y:x+y
#print(add(10,20))

#How to remove duplicates from the list without using inbuilt functions
items = [1, 2, 3, 4, 1, 2, 3, 4, 5]
res = []
for item in items:
    if item not in res:
        res.append(item)

#Find the longest word in the sentence*
sentence = "Hello world Welcome to Python"
words = sentence.split()
count = 0
c_word =''
for i in words:
    if len(i)>count:
        c_word = i
        count = len(i)
#print(count, c_word)


#write a program to reverse the values in the dictionary if the value is of type String
d = {'a': 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}
res = {key:value[::-1] if type(value)==str else value for key,value in d.items()}
#print(res)

# write a program to get 1234
t = ('1', '2', '3', '4')
#print(''.join(t))

#How to get the elements that are in list b but not in list a
a = [1, 2, 3]
b = [1, 2, 3, 4]
#print(set(b)-set(a))

#A function takes variable number of positional arguments as
# input. How to check if the arguments that are passed are more than 5
def func(*args):
    if len(args)>5:
        print("length of arguments passed is greater than 5")

    else:
        print("length of arguments is less than 5")

#func(1,2,3,4,5,6)
#count the number of occur rences of "CRITICAL", "INFO" and "ERROR" lines in a log file.

lines = """CRITICAL:Hello world
INFO: This is an info
ERROR: This is an error 
CRITICAL: This is critical
CRITICAL:Hello world
INFO: This is an info
ERROR: This is an error 
CRITICAL: This is critical
CRITICAL:Hello world
INFO: This is an info
ERROR: This is an error 
CRITICAL: This is critical
CRITICAL:Hello world
INFO: This is an info
ERROR: This is an error 
CRITICAL: This is critical"""

l1 = lines.split("\n")
d = defaultdict(int)

for i in l1:
    error_type , other = i.strip().split(":")
    d[error_type]+=1

#print(d)

#Write a function to reverse any iterable without using reverse function.**
a = [1, 2, 3, 4, 5]
def reverse_(l1):
    res=[]
    for i in l1:
        res = [i] + res
    return res

#print(reverse_(a))
#print(res)

#Write a function to print the below output
# func("TRACXN", 0)  # Should print RCN
# func("TRACXN", 1)  # Should print TAX

def func(str1, flag):
    if flag == 0:
        return str1[1::2]
    else:
        return str1[::2]

#print(func("TRACXN", 0))
#print(func("TRACXN", 1))

#Write a program to sum all the numbers in below string
var = "Sony12India567Pvt2ltd"
import re
list_ = re.findall(r'\d+' , var)
res = 0
for i in list_:
    res+=int(i)
#print(res)


#Print all the numbers in the below list
a = ['abc', '123', 'hello', '23']
for i in a:
    if i.isdigit():
        print(i)


#Program to print the number of occurrences of characters in a String without using inbuilt functions
s = 'helloworld'
d = defaultdict(int)
l = s.split()
for i in s:
    d[i]+=1
#print(d)

#Program to print only the repeated characters and count of the same
s = 'hello world'
d = defaultdict(int)
for i in s:
    d[i]+=1
#print(d)

for key,value in d.items():
    if value>1:
        print(key, value)

dict_ = {i:s.count(i) for i in s if s.count(i)>1}
#print(dict_)

#Write a program to get square of list of number's using lambda function
a = [1, 2, 3, 4, 5]
square = lambda a:a*a
b = [square(i) for i in a]
#print(b)

#Write a function that accepts two strings and returns True if the two
# strings are anagrams of each other
def is_anagram(str1,str2):
    var1 = set(str1.upper())
    var2 = set(str2.upper())

    if var1 == var2:
        return True

    else:
        return False

#print(is_anagram('eat','ate'))
#print(is_anagram('racecar','racecar'))
#print(is_anagram('life','wife'))

#Write a program to iterate through list and build a new list, only if the
# items of the list has even number of characters.**

names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
#print([i for i in names if len(i)%2==0])

#Write a program to iterate through list and build a new dictionary,
# only if the items of the list has even number of characters.**
names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
#print({i:len(i) for i in names if len(i)%2==0})

#46 Write a program which squares the numbers in a list using map object
a = [1, 2, 3, 4, 5]
def square(num):
    return num**2

l1 = map(square ,a)
#print(list(l1))
'''
#47 Count number of lines in a file without loading the file to the memory
#with open(r'C:\Users\User\Desktop\filehandling\files\sample1.txt') as f:
    #count = 0
    #for i in f:
        #count +=1
    #print(count)

#48 Printing line and line no's*
#with open(r'C:\Users\User\Desktop\filehandling\files\sample1.txt') as f:
    #for line_num,line in enumerate(f, start=1):
        #print(line_num,line)
'''
#49 Write a Program to print the sum of entire list and sum of only internal list
var = [[1,2,3], [4,5,6], [7,8,9]]
l1 = [sum(i) for i in var]
#print(l1)

l2 = sum([item for list_in in var for item in list_in])
#print(l2)

#50 Write a program to reverse the list as below**
words = ["hi", "hello", "python"]
# o/p ['nohtyp', 'olleh', 'ih']
res = []
for word in words:
    res = [word[::-1]] + res
#print(res)

#51Write a program to update the tuple**
t1 = (1, 2, 3, 4)
t2 = (100, 200, 300)
t = t1 + t2
#print(t)

#52Write a program to replace value present in nested dictionary
d = {'a': 100, 'b': {'m': 'man', 'n': 'nose', 'o': 'ox', 'c': 'cat'}}
# Replace "nose" with "net"
for key, value in d.items():
    if isinstance(value,dict):
        d[key]['n']='net'
#print(d)
'''

#53Write a program to count the number of white spaces in a file
import  re
spaces = 0
with open(r'C:\Users\User\Desktop\filehandling\files\sample1.txt') as f:
    for file in f:
        match = re.findall(r"\s", file)
        if match:
            spaces+=len(match)

#print(spaces)

'''
#54Grouping anagrams.
words = ['eat', 'ate', 'tea', 'hello', 'silent', 'listen']
d=defaultdict(list)
for word in words:
    s = ''.join(sorted(word))
    #print(s)
    d[s].append(word)

#print(d)
#print(d.values())

#55Find the longest non-repeated substring in the below string**
s = "This is a Programming language and Programming is fun"
l1 = s.split()
d = {word:len(word) for word in l1 if s.count(word) == 1}
#print(sorted(d.items()))
#print(sorted(d.items(), key=lambda item: item[-1])[-1])


#56Write a program to find the duplicate elements in the list without
# using inbuilt functions**
names = ['apple', 'google', 'apple', 'yahoo', 'google']
s = set(names)

for i in s:
    count = 0
    for name in names:
        if i == name:
            count += 1

    if count>1:
        print(i)


#62Write a program to count the number occurrences of each item in the list
# without using any inbuilt functions**
names = ['apple', 'google', 'apple', 'yahoo', 'google', 'facebook', 'gmail', 'yahoo']
s = set(names)
res = {}
for item in s:
    count=0
    for word in names:
        if item == word:
            count+=1
    res[item]=count
print(res)
'''
'''
#program to check weather it is an prime number or not
def is_prime(num):
    for i in range(2,num):
        if num%i == 0:
            #print(num,"not an prime")
            return False
    else:
        #print(num," is an prime")
        return True

for i in range(1,50):
    if is_prime(i) == True:
        print(i)


#65Write a program to find the largest number in the list without using any inbuilt functions**
numbers = [10, 200, 30, 4000, 50]
largest = 0
for i in numbers:
    if i > largest:
        largest = i
print(largest)


#Write a method that returns the last digit of an integer. For example,
# the call of get_last_digit(3572) should return 2.

def func(num):
    str1 = str(num)
    return int(str1[-1])

print(func(3572))

#67 Write a program to find most common words in a given list
from collections import  Counter
words = [
'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the',
'eyes', 'look', 'into','my', 'eyes', "you're", 'under'
]

var = Counter(words)
#Counter.most_common(var)
var.most_common()
print(var)

#68 Make a function named tail that takes a sequence (like a list, string, or tuple) and a number n 
#and returns the last n elements from the given sequence, as a list.

def tail(var,n):
    if not isinstance(n, int):
        raise TypeError("value of n should be an integer")
    if n<=0:
        return []
    return list(var[-n:])

print(tail([1,2,3,4,5,6],3))

#Write function named is_perfect_square that accepts a number and
#returns True if it's a perfect square and False if it's not.*
from math import sqrt
def is_perfect_square(num):
    n = int(sqrt(num))
    return num == n*n

print(is_perfect_square(30))


import re
sentence = "Hi How are You WelCome to PytHon"
pattern = r'[A-Z]'
match = re.findall(pattern,sentence)
print({i:match.count(i) for i in match})

sentence = "Hi there! How are you:) How are you doing today!"
import re
from collections import Counter
words = re.findall(r'\b\w+', sentence)
print(words)
print(Counter(words))
'''
from collections import defaultdict
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d = defaultdict(list)
for num in numbers:
    if num%2==0:
        d[0].append(num)

    else:
        d[1].append(num)

#print(d)

#Find all max numbers from the below list**
numbers = [1, 2, 3, 0, 4, 3, 2, 4, 2, 1, 0, 4]
max_num = max(numbers)
#print(max_num)

all_max_num = [i for i in numbers if i == max_num]
#print(all_max_num)

'''
#Find all max length words from the below sentence**
sentence = "hello world hi apple you yahoo to you"
l1 = sentence.split()
max_len_word = max(sentence.split(), key=len)
max_len_words = [ word for word in sentence.split() if len(word) == len(max_len_word)]
print(max_len_words)


numbers = ['857', '987', '8', '120', '888888', '547', '7674', '89', '589', '388888', '2889']
import re
for num in numbers:
    match = re.findall(r'\b8',num)
    if match:
        print(num)

l1 = [1, 2, 3, 4, 1, 2, 3, 4, 3, 4, 4]
l2=l1.copy()
'''

word = 'AAAaaccYYY'
ele = set(word)
res=[]
for i in ele:
    if i in word:
        res.append(i+str(word.count(i)))

print(res)