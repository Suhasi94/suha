#List of even numbers between range 1-50
#l1 = [i for i in range(1,50) if i%2==0]
#print(l1)

#"Returns a list names starting with vowels in the given string"
# names = ['laura', 'steve', 'bill', 'james', 'bob', 'greg', 'scott', 'alex', 'ive']
#l2 = [i for i in names if i[0] in 'aeiouAEIOU']
#print(l2)
'''
#"Filtering all the languages which starts with 'p'"
languages = ['Python', 'Java', 'Perl', 'PHP', 'Python', 'JS', 'C++', 'JS', 'Python', 'Ruby']
l3 = [i for i in languages if i[0] in 'pP']
print(l3)
'''
#Names starting with consonants
names = ['laura', 'steve', 'bill', 'james', 'bob', 'greg', 'scott', 'alex', 'ive']
l4 = [i for i in names if i[0] not in 'aeiouAEIOU']
#print(l4)


#"Filtering out those names which are less than 6 characters
names = ['apple', 'google', 'yahoo', 'gmail', 'flipkart', 'instagram', 'microsoft']
l5 = [i for i in names if len(i)<6]
#print(l5)

#Raise to the power of list index
a = [1, 2, 3, 4, 5]
l6=[a[i]**i for i in range(0,len(a))]
#print(l6)

#"Build a list of tuples with string and its length pair"
names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']
l7 = [(i,len(i)) for i in names]
#print(l7)

#"Build a list with only even length string"
names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']
l8 = [i for i in names if len(i)%2==0]
#print(l8)

#l9Generating List of PI values with increasing decimal point numbers

#List comprehension to sum the factorial of numbers from 1-5
from math import factorial
l10 = [factorial(i) for i in range(1,6)]
#print(sum(l10))

#"Reverse the item of a list if the item is of odd length string"
names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']
l11 = [i[::-1] for i in names if len(i)%2!=0 ]
#print(l11)

#Reverse the item of a list if the item is of odd length string otherwise keep the item as is!.
names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']
l12 = [i if len(i)%2==0 else i[::-1] for i in names]
#print(l12)

s = 'abracadabraca'
l = set(s)
var = {}
for i in l:
    if i in s:
        var[i]=s.count(i)
#print(var)

d = {var[i]:s.count(i) for i in l if i in s}
#print(d)

#Counting occurrences of word in the string
sentence = "hello world welcome to python hello hi hello hello"
l = sentence.split()
var = {}
for i in l:
    if i in l:
        var[i]=l.count(i)
#print(var)
#print({i:l.count(i) for i in l if i in l})

'''
files = ['youtube.txt', 'amazon.pdf', 'facebook.pdf', 'google.pdf', 'apple.doc']
res = []
for i in files:
    for j in range(len(i)):
        if i[j]=='.':
            res.append(i[j+1:])

#print(res)
res = []
for i in files:
    for j in range(len(i)):
        if i[j]=='.':
            res.append(i[:j])
            break

print(res)
'''

