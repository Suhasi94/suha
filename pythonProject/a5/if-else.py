# palindrome or not
# string = input("enter a string: ")
# if string[::-1] == string:
#     print("palindrome")
# else:
#     print("not a palindrome")


##########starting with vowel or not
# string = input("enter a string: ")
# if string[0] in "aeiouAEIOU":
#     print("starts with vowel")
# else:
#     print("does not starts with vowel")

########check if the integer is palindrome or not

# num = int(input("enter the number: "))
# if str(num)[::-1] == str(num):
#     print(f"{num} is palindrome")
# else:
#     print(f"{num} is not a palindrome")



########given character is a special character or not

# a = input("eneter a character: ")
# if a.alnum() != True: #if not a.alum()
#     print("it is a special character")

############to check if the iterable is empty or not
# l = [1, 2, 3]
# if l: #bool(l) #if len(l) == 0
#     print("not empty")
# else:
#     print("empty")
#
# ###########inline if-else
#
# iterable = "hello"
#
# # {true block} if condition else {false block}
# print("not empty" if iterable else "empty")
#
# num = 1221
# a = str(num)
# print("palindrome" if a[::-1]==a else "not palindrome")


###########to check if the key is present in the dictionary or not

# d = {"a": 1, "b": 2}
# key = "b"
# if key in d:
#     print("present")
# else:
#     print("not present")
#
# ###inline
# print("key is present" if key in d else "not present")


###############check if the given value is string or not

# a = "holiday"
# if isinstance(a,str):
#     print("its true")
# else:
#     print("its false")

###########check if the given string ends with the vowel or not

# a = "swatI"
# if a[-1] in "aeiouAEIOU":
#     print("it ends with vowel")
# else:
#     print("it ends with cons")

###CHECK IF THE LIST HAS EVEN NUMBER OF ELEMENTS OR NOT


# l = [1, 2, 3, 4]
# if len(l) % 2 == 0:
#     print("it has even number of elements")
# else:
#     print("it has odd number of elements")

### in a number check if the 1st number is even or odd

# n = 2345
# if isinstance(n, (int,str)) and int(str(n)[-2]) % 2 ==0:
#     print("its even")
# else:
#     print("its odd")



#### Greatest of three numbers

# a, b, c = 10, 20, 30
# if a > b and a > c:
#     print("a is greater")
# elif b > c:
#     print("b is greater")
# else:
#     print("c is greater")


#####converting upper to lower and vice versa

# s = input("enter the string: ")
# if s.isupper(): # s == s.upper()
#     print(s.lower())
# else:
#     print(s.upper())
# if "a"<= s <= "z":
#     print(chr(ord(s)-32))
# elif "A"<= s <="Z":
#     print(chr(ord(s)+32))

### CHECK WHETHER THE GIVEN YEAR IS A LEAP YEAR OR NOT

# y = int(input("enter the year: "))
# if ((y % 400 == 0) or (y % 100 != 0 and y % 4 == 0)):
#     print("its a leap year")
# else:
#     print("its not a leap year")

## check the number of keys in the dictionary, if the number is even print the dictionary as it is else add a new key to make it even and print it

# d = {"a": 1, "b":2, "c":3}
# if len(d) % 2 == 0:
#     print(" it is even")
# else:
#     d.update({"d": 4})
#     print(d)



# d = {"a": 1, "b": 2, "c": 3}
# if len(d) % 2 == 0:
#     print(d)
# else:
#     d["d"] = 4 # d.update(d=4) # d.update({"d":4}) # d.setdefault(e)
#     print(d)

# # check if entered character is vowel or not , if it is vowel than create a dictionary  with char and its ascii value pair

# ch = "a"
# d = {}
# if ch in "aeiouAEIOU":
#      d.update({ch: ord(ch)}) #d = dict.fromkeys(ch,ord(ch)) #d[ch] = ord(ch)
#      print(d)
# else:
#     print("its not a vowel")









