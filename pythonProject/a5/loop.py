# even numbers from 1 - 10
# start = 1
# end = 10
# while start <= end:
#     if start % 2 == 0:
#         print(start)
#     start += 1
#
# odd numbers from 1-10
# start = 1
# end = 10
# while start <= end:
#     if start % 2 == 1:
#         print(start)
#     start += 1











##################################




# wap to print numbers from -10 to -1
# s = -10
# end = -1
#
# while s <= end:
#     print(s, end=" ")
#     s += 1




#wap to check if the number is prime or not
# num = 9
# i = 2
# while i < num:
#     if num % i == 0:
#         print("not prime")
#         break
#     i += 1
# else:
#     print("prime")

#  10 prime numbers -- range of numbers
#
# num = 1
# count = 0
# while num > 0:
#     if num > 1:
#         i = 2
#         while i <= num//2: # i < num
#             if num % i == 0:
#                 break
#             i += 1
#         else:
#             count += 1
#             if count <= 10:
#                 print(num,end=" ")
#     num += 1

# Fibonacci numbers upto 10

# a = 0
# b = 1
# while a <= 10:
#     print(a,end=" ")
#     c = a + b
#     a , b = b, c


# fibonacci series upto 10 numbers


# a = 0
# b = 1
# count = 0
# while count <= 10:
#     print(a,end=" ")
#     c = a + b
#     a , b = b, c
#     count += 1

# wap to traverse through a string printing each charcter

# s = "suhasini"
# i = 0
# while i < len(s):
#     print(s[i],end=" ")
#     i += 1


# range(start,end,step)
# print(list(range(1,11,1)))
# print(tuple(range(1,11)))
# print(str(range(11)))

# write a program to print even numbers from 1-50

# for num in range(1, 50):
#     if num % 2 == 0:
#         print(num)

# prime numbers

# num = 12
# for i in range(2,num):
#     if num % i == 0:
#         print("not prime")
#         break
# else:
#     print(num)

### for prime number series from 1 - 10

# for num in range (1,11):
#     if num >1:
#         for i in range(2,num):
#             if num % i == 0:
#                 break
#         else:
#             print(num,end=" ")

# write a program to traverse through iteralable

# s = "hello"
# for char in s:
#     print(char)
# for i in range(len(s)-1):
#     print(i,s[i],end=" ")

# set

# s = {"hello", "hai", "world"}
# for element in s:
#     print(element,end=" ")

#Dictionary
# d = {"a":1, "b":2, "c":3}
# print(d["a"])
# print(d.get("a"))
# for key in d:
#     print(key,d[key],end=" ")





############################Program to count the number of digits and alphabets in the string

s = "hai 1234 python23"
count_a = 0
count_d = 0

# for i in s:
#     if i.isalpha():
#         count_a += 1
#     elif i.isdigit():
#         count_d += 1
# print(count_a,count_d)

# for i in s:
#     if ord("a")<= ord(i)<= ord("z") or ord("A")<= ord(i)<= ord("Z"):
#         count_a += 1
#     elif "0"<= i <= "9":
#         count_d += 1
# print(count_a,count_d)

####################################

# sentence = "hai how are you"
# count = 0
# l = sentence.split()
# print(l)
#
# for word in l:
#     count += 1
# print(count)


############ print all repeated characters
# s = "hello world"
# for char in set(s):
#     if s.count(char) > 1:
#         print(char,end=" ")




########### to remove the duplicate/repeated characters in the given string

# s = "hello world"
# res = ""

# for ch in s:
#     if s.count(ch) == 1:
#         res += ch
# print(res) # he wrd

# for ch in s:
#     if ch not in res:
#         res += ch
# print(res) #helo wrd
# print(set(s)) # {'h','e','l','o',' ','w','r','d'}


######## print duplicate characters without using inbuilt methods
# s = "hello world"
# non_duplicates = ""
# duplicates = ""
#
# for ch in s:
#     if ch not in non_duplicates:
#         non_duplicates += ch
#     else:
#         duplicates += ch
# print(non_duplicates)
# print(set(duplicates))
# print("".join(set(duplicates)))



# to print all the indices of the given substring


# s = "hello world"
# ch = "o"
#
# for i in range(len(s)):
#     if s[i] == ch:
#         print(i,end=" ")

### first occurence of the index of the substring

# s = "hello world"
# ch = "o"
# print(s.index(ch))# inbuilt function
#
# for i in range(len(s)):   # without using inbuilt function
#     if s[i] == ch:
#         print(i)
#         break

### first occurence of the index of the substring
#
#
# s = "hello world"
# ch = "o"
# print(s.index(ch))# inbuilt function
#
# for i in range(len(s)):   # without using inbuilt function
#     if s[i] == ch:
#         print(i)
#         break



##############





