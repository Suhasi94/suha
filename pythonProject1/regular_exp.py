import re
"""
#program to print upper case and lower case characters
sentence = "Hello World Welcome To Python"

pattern = r"[A-Z]"
pattern1 = r"[a-z]"

upper_ = re.findall(pattern, sentence)
print(len(upper_))

lower_ = re.findall(pattern1, sentence)
print(lower_)
print(len(lower_))

print(len(sentence))
"""

greeting = "hello world welcome to regular expressions in python"
#pattern = "python"
#print(re.findall(pattern, greeting))
#print(re.findall('welcome', greeting))
#print(re.findall('universee',greeting))

#print(re.findall('hello', 'hello world hello there how are you'))

#re is an case sensitive
#print(re.findall('Hello', 'hello world hello there how are you'))

#ignoring case using IDNORECASE flag in re
#print(re.findall('Hello', 'hello world hello there how are you',re.IGNORECASE))

#word = "@hello12world34welcome!123"

#res = re.findall(r"\D", word)
#print(''.join(res))

############### matching all the characters using '.'  #################
#"." - matches anything and everything (a-z, A-Z, 0-9, all the special characters)
#one dot = one character

data = 'hello world'
#print(re.findall(r'.',data))

#matching pattern('a' followed by exactly one character and followed by 'b')
#print(re.findall(r"a.b",'abc'))
#print(re.findall(r'a.b','acb'))
#print(re.findall(r'a.b','abb'))
#print(re.findall(r'a.b','a b'))
#print(re.findall(r'a.b','aabb'))
#print(re.findall(r'a.b','a@b'))


#####################startswith(^) ###############
#print(re.findall("^hello","hello how are you"))
#print(re.findall('^are','hello how are you'))

#################### endswith($) ################
#print(re.findall("hello$","hello how are you"))
#print(re.findall("you$","hello how are you"))
'''
########### matching multiple characters using "."
print(re.findall('a.a','ana'))
print(re.findall('a.a','ama'))
print(re.findall('a.a','amma'))
print(re.findall('a.a','aaaa'))

#matching characters using ".."
print(re.findall('a..a','ana'))
print(re.findall('a..a','ama'))
print(re.findall('a..a','amma'))
print(re.findall('a..a','aaaa'))
print(re.findall('a..a','a a'))
print(re.findall('a..a','a  a'))
print(re.findall('a..a','asha'))
'''
#matching any number of characters
#print(re.findall("a.*a","amma"))
#print(re.findall("a.*a",'aa'))

#print(re.findall('an.*a','amma'))
#print(re.findall('an.*a','anna'))

#### combining * and ^/$ #####################

#print(re.findall('^a.a$',"hello anna"))
#print(re.findall('an.a$',"hello anna"))
#print(re.findall('an.a$',"anna hello"))
#print(re.findall('^an.a',"anna hello"))

#to check anna is begining as well as at the end
#print(re.findall('^an.a$',"anna"))
#print(re.findall('^an.a$',"anna hello"))#[]
#print(re.findall('^an.a$',"anna hello anna"))#[] as it satisfies only one condition

############ matching one or any number of characters#############

#print(re.findall(r"an+a",'ana'))
#print(re.findall(r'an+a','anna'))
#print(re.findall(r'an+a','aa'))
#print(re.findall(r'an*a','aa'))

########### matching 0 or 1 occurance ###########################

#print(re.findall(r'an?a','aa'))
#print(re.findall(r'an?a','ana'))
#print(re.findall(r'an?a','anna'))
#print(re.findall(r'colou?r','this is a beautiful color and that is an ugly colour'))


########## matching urls with http and https ###############################
'''
url = "http://www.google.com"
url1 = "https://www.google.com"

print(re.findall(r"http",url))
print(re.findall(r'http',url1))
print(re.findall(r'http?',url1))
print(re.findall(r'http?',url))
'''

############# matching only vowel character ##################
# by using normal for loop
words = "hello anna how are you doing"
'''
for letter in words:
    if letter in "aeiouAEIOU":
        print(letter)

#by using reg ex
print(re.findall(r"[aeiou]", words))

#to find the number of vowels
print(len(re.findall(r"[aeiou]", words)))

print(re.findall(r"[aeiou]", words).__len__())


############ matching the range by using - #####################

print(re.findall(r'[0123456789]','the cost of the book is 100'))
print(re.findall(r'[abcdefghij]','hello world'))
print(re.findall(r'[0-9]','the cost of the book is 100'))
print(re.findall(r'[a-j]','hello world'))


############# matching only numeric characters #################

print(re.findall(r'[0-9]','The cost of the i11 is 50000 and i13 is 73000'))
print(re.findall(r'[0123456789]','The cost of the i11 is 50000 and i13 is 73000'))
print(re.findall(r'\d','The cost of the i11 is 50000 and i13 is 73000'))

#matching complete number
# + -->greedy character
print(re.findall(r'[0-9]+','The cost of the i11 is 50000 and i13 is 73000'))
print(re.findall(r'\d+','The cost of the i11 is 50000 and i13 is 73000'))
print(re.findall(r'\d+','The cost of the i11 is 50000 and i13 is 73000 at 12345@98756'))
print(re.findall(r'[abcd]+','abcdefghiabiuycd'))



### ^ --> outside the character set represents start of the string
### ^ --> inside the character set represents negation i.e., matches everything excepts
# the characters in the set

print(re.findall(r'[^0-9]','the cost of the book is at rs.100'))
print(re.findall(r'[^0-9]+','the cost of the book is at rs.100'))
print(re.findall(r'[^abcd]','axbycde'))
print(re.findall(r'[^abcd]+','axbycde'))

'''

############ matching different patterns ###############

#only upper case
#print(re.findall(r'[A-Z]','Here We Are Discussing Regular Expression'))
#print(re.findall(r'[A-Z]+','Here WE Are Discussing REGUlar Expression'))
#only lower case
#print(re.findall(r'[a-z]','Here We Are Discussing Regular Expression'))
#print(re.findall(r'[a-z]+','Here We Are Discussing Regular Expression'))

#both upper and lower case
#print(re.findall(r'[A-Za-z]','Here We Are Discussing Regular Expression'))
#print(re.findall(r'[A-Za-z]+','Here We Are Discussing Regular Expression'))

#match to upper,lower and numeric
#print(re.findall(r'[A-Za-z0-9]','The cost of iphone of Rs.75000'))
#print(re.findall(r'[A-Za-z0-9]+','The cost of iphone of Rs.75000'))

#match all except alphabets and numbers
#print(re.findall(r'[^A-Za-z0-9]','The cost of iphone of Rs.75000'))
#print(re.findall(r'[^A-Za-z0-9]+','The cost of iphone of Rs.75000'))

############ counting the number of specific characters ################

#counting  number of numeric characters
#print(len(re.findall(r'[0-9]','The cost of iphone of Rs.75000')))

#counting number of spaces characters
#print(len(re.findall(r' ','The cost of iphone of Rs.75000')))

#counting number of spaces using \s
#print(len(re.findall(r'\s','The cost of iphone of Rs.75000')))

#counting the special characters excluding white space characters
#print(re.findall(r'[^A-Za-z0-9\s]','i am @flying %from blr to Goa tmrw and flight cost is rs.21000'))
#print(len(re.findall(r'[^A-Za-z0-9\s]','i am @flying %from blr to Goa tmrw and flight cost is rs.21000')))

################# splitting words ##########################

#print(re.findall(r'\w','My scooty number is Ka64s5734'))
#print(re.findall(r'\w+','My scooty number is Ka64s5734'))

########## limiting the number of characters in a pattern using {} #############

#matches each and every numeric character
#print(re.findall(r'\d+','the pin code of bangalore is 560001 and tel code is 080'))

#matching only using \d
#print(re.findall(r'\d\d\d\d\d\d','the pin code of bangalore is 560001 and tel code is 080'))

#matching only pin code using {}
#print(re.findall(r'\d{6}','the pin code of bangalore is 560001 and tel code is 0809988776655'))

#matching only pincode using word boundry(\b)
#print(re.findall(r'\b\d{6}\b','the pin code of bangalore is 560001 and tel code is 0809988776655'))

############## matching words starting with 'h' ################
'''
sentence = "hello tonny hi how are you happy birthday"
print(re.findall(r'h[a-z]', sentence))
print(re.findall(r'h[a-z]+', sentence))
print(re.findall(r'\bh[a-z]', sentence))
print(re.findall(r'\bh[a-z]+', sentence))
'''

########## matching words starting with p and j

#sentence = "Python is a programming language. Python is easier than Java"
#print(re.findall(r'\b[PJ][a-zA-Z]+\b',sentence))

########## matching words ending with 'y' ###################
#sentence = 'hi how are you, happy birthday flying'
#print(re.findall(r'[a-zA-Z]+y\b',sentence))
'''
### to count the number of occurances non-special characters in the given string####
sentence = "hello@world! welcome!!! to python$"

letters = re.findall(r'[a-zA-z]',sentence)
print(len(letters))

d = {letter:letters.count(letter) for letter in letters}
print(d)
'''

'''
############## filtering only those characters except digits ################
word = "@hello12world34welcome!123"

print(re.findall(r'\D',word))
print(re.findall(r'\D+',word))
'''

'''
########## count the characters in each word (Ignore special characters)
sentence = "hi there! hoe are you:) How are you doing today!"
words = re.findall(r'[a-zA-Z]+',sentence)

d = {word:len(word) for word in words}
print(d)
'''

'''
######## number of uppercase and  lowercase letters

sentence = "Hello World Welcome To Python"
upper_ = re.findall(r'[A-Z]', sentence)
print(len(upper_))

lower_ = re.findall(r'[a-z]',sentence)
print(len(lower_))
'''

'''
##### print only those words starts with the vowels #######
sentence = 'hello hi american engineers and indian writers officers united states'
print(re.findall(r'\b[aeiou][a-z]+',sentence))
'''
'''
######################### matching only 3 letters words #######################

sentence = "hi there how are you how are you doing today"
print(re.findall(r'\b[a-zA-Z]{3}\b',sentence))
'''
'''
##### matching either "python" or 'java'
sentence = "programming in python is fun and programming in java is mess"
print(re.findall(r'(python|java)',sentence))
'''
'''
########## matching words starting with "he" ##################
sentence = "he helps the community and he is the hero"
print(re.findall(r'\bhe[a-zA-Z]+',sentence))# + --> is one or more occurance
print(re.findall(r'\bhe[a-zA-Z]*',sentence))
'''
'''
######### matching words starting with 'he' or 'se' ###########
sentence = 'he helps the community and he is the hero she sells sea shells on the sea shore'
print(re.findall(r'\b(?:he|se)[a-zA-Z]*', sentence))
'''
'''
########## matching the files and file extensions ##############

download_messages = """ Downloading file archive.zip to downloads folder...
Downloading file image.jpeg to downloads folder...
Downloading file index.html to downloads folder...
Downloading file python.py to downloads folder...
"""

#to use "." in the pattern we cant use it directly as it has some other meaning,
#instead it has to be escaped
print(re.findall(r'\.[a-zA-Z]+',download_messages))
print(re.findall(r'\b[a-zA-Z]+\.[a-zA-Z]+',download_messages))
'''
'''
################# creating acronyms of the file formats #################
# acronyms means the first letter of each words in the string
#for eg:Image Processing : IP
file_formats = ['Graphics Interchange Format', 'Advanced Audio Coding', 'Cascading Style Sheets',
                'HyperText Markup Language', 'Joint Photographic Experts Group',
                'Content Management System', 'Tagged Imaged File Format',
                'Windows Media Audio', 'Comma Separated Values',
                'JavaScript Object Notation']
match = []
for file in file_formats:
    data = re.findall(r'[A-Z]',file)
    match.append(''.join(data))

print(match)
#o/p --> ['GIF', 'AAC', 'CSS', 'HTML', 'JPEG', 'CMS', 'TIFF', 'WMA', 'CSV', 'JSON']
'''
'''
############ matching phone numbers ##################
Phone_Numbers = ['123-345-0987', '456-9832-098', '800-987-4756', '080-1234567823',
                 '123-456-789','123-345-34','900-938-0987']

res = []
for num in Phone_Numbers:
    match = re.findall(r'\d{3}-\d{3}-\d{4}',num)
    if match:
        res.append(match)

print(res)

#getting the only the numbers starts with 6789
res = []
for num in Phone_Numbers:
    match = re.findall(r'[6789]\d{2}-\d{3}-\d{4}',num)#here we have to change d{3}-d{2}
    if match:
        res.append(match)

print(res)
'''
'''
####################### matching valid dates ##########################

dates = ['2019-01-02', '2019-13-02', '2019-12-26', '26-08-2019', '20-19-20',
         '2019-12-31', '2019-12-32']

#year = '\d{4}'
# month = (0[0-9]|1[0-2])
# day= (0[0-9]|1[0-9]|2[0-9]|3[01])

pattern = r'\d{4}-(?:0[0-9]|1[0-2])-(?:0[0-9]|1[0-9]|2[0-9]|3[01])'
res = []
for date in dates:
    match = re.findall(pattern, date)
    if match:
        res.append(match)
print(res)
'''
'''
################### matching 24 hour time format ####################

formats = ['00:00:00', '23:59:59', '24:00:00', '1:59:20', '12:9:10', '10:20:8']

#hours
#00,01.........09 --> 0[0-9]
#10,11,........19 --> 1[0-9]
#20,21,22,23 --> 2[0-3]
#pattern = ([01][0-9]2[0-3])

#mintutes
#00,01......09
#10,11......19
#20,21......29
#30,31......39
#40,41......49
#50,51......59
#pattern=[0-5][0-9]

#seconds
#00,01......09
#10,11......19
#20,21......29
#30,31......39
#40,41......49
#50,51......59
#pattern=[0-5][0-9]

pattern = r'(?:[01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]'
res = []
for data in formats:
    match = re.findall(pattern, data)
    if match:
        res.append(match)
print(res)

'''
'''
##################### matching mail id ############################
emails = ['test.user@company.com', 'test.user2@company.com', 'test_user@company.com',
          'testing@company.com', '123test-T.user@company.com', 'testing@company',
          'testingcompany.com']
pattern = r'\b[^0-9][a-zA-Z]+[\.-]?[a-zA-Z0-9]+@[a-zA-z]+\.(?:com|edu|in|au|gov)'
'''
'''
################ matching pan number ##############################

sentence = "my pan number id ABCDE1234S and my friends pancard number is XYZTR3104J"
pattern = r'[A-Z]{5}\d{4}[A-Z]'
print(re.findall(pattern, sentence))
'''
'''
############### matching ip address #############################
ips = ['10.1.2.3','127.0.0.0','199.99.9.9','199.9.9999.9','127-0-0-0']
pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
for i in ips:
    print(re.findall(pattern,i))
'''

############ replacing characters in a string ##################
#sub()- to replace old string with an new string

#Replace whitespaces with newline character in the string
sentence = "hello world welcome to python"
words = re.sub(r'\s','\n',sentence)
#print(words)

#replace all the vowels with *
words = re.sub(r'[aeiou]','*',sentence)
#print(words)

#replace all the numerics by *
sentence = "hello123world welcome456to python012 "
words = re.sub(r'\d','*',sentence)
print(words)