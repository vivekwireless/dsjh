# 1)wap to print length of the string without using inbuilt function.
# st='hi there how are you'
# count=0
# for i in st:
#     count+=1
# print(count)

# 2)wap to reverse a string without using any inbuilt function.
# st='hi there how are you'
# out=''
# for i in st:
#     out=i+out
# print(out)
# print(st[::-1])


# 3)wap to replace one string with another string ex.'hello world' replaces world with 'universe'
# from re import findall, sub, finditer
# st ='hello world'
# new_st=sub('world','universe',st)
# print(new_st)

# 4)how to convert a string to a list and viceversa
# st='hello vivek how are you'
# lst=st.split()
# print(lst)
# var=" ".join(lst)
# print(var)

# 5)convert a string 'hello welcome to python' to a comma separated string.
# from re import sub
# st='hello welcome to python'
# var=sub('\s',",",st)
# print(var)
# or
# print(",".join(st.split()))


# 6)wap to print alternate characters in a string.
# st='hello vivek how are you'
# for i in range(0,len(st),2):
#     print(st[i])
# or
# print(st[::2])
# or
# for i in st[::2]:
#     print(i,end="")


# 7)wap to print ascii values of the characters present in the string
# st='hello vivek how are you'
# for item in st:
#     if item==" ":
#         continue
#     else:
#         print(item, ord(item))

# 8)wa function to convert upper case to lowercase and viceversa without using inbuilt methods.

# def upptolower(any_str):
#     out= ""
#     for i in any_str:
#         if 'A'<=i<='Z':
#             out+=chr(ord(i)+32)
#         elif 'a'<=i<='z':
#             out+=chr(ord(i)-32)
#         elif i==" ":
#             out+=" "
#     return out
# print(upptolower('Hello ViVek HoW are YoU'))

# 9)wap to swap two numbers without using 3rd variable.
# a=10
# b=20
# a,b=b,a
# print(a)
# print(b)
# a=a+b
# b=a-b
# a=a-b
# print(a,b)

# 10)wap to merge two different lists
# a=[1,2,3,4]
# b=[6,4,5,8]
# c='skso'
# d='jshs'
# print(a+b)
# print(c+d)
# print([a,b])
# print(c,d)
# print(*a,*b)

# 11)wap to read a random line in file (ex. 50, 65, 78th line)
# with open(r"E:\vs code\sample.log",'r') as file:
#     for index,item in enumerate(file, start=1):
#         if index==50:
#             print(item)

# or

# from random import *
# with open(r"E:\vs code\sample.log",'r') as file:
#     print(choice(file.readlines())) #file.readlines() takes all lines of the file into a list

# from itertools import islice
# def rand_line(n):
#     with open(r"E:\vs code\sample.log",'r')as f:
#         lines=islice(f,n)
        # print(list(lines))
#         for line in lines:
#             print(line)


# 12)write a program to read random lines in a file

# from random import *
# with open(r"E:\vs code\sample.log",'r') as file:
#     var=file.readlines()
#     for _ in range(4):
#         print(choice(var))

# or
# from random import *
# with open(r"E:\vs code\sample.log", 'r') as r_obj:
#     var=r_obj.readlines()

# random_line = choices(var, k=3)
# print(random_line)


# 13)wap to print last N lines of a file.
# with open(r"E:\vs code\sample.log",'r') as file:
#     var=file.readlines()
#     print(var[-10::])



# 14) wap to check if the given string is palindrom or not without using reversed method.
a=input('enter the string')
# b=""
# for i in a:
#     b=i+b
# if a==b:
#     print('palindrome')
# else:
#     print("not a palindrome")

if a==a[::-1]:
    print("string is palindrome")

# reverse of a string
# seq_string = 'Python'
# # print(seq_string[::-1])
# var=list(reversed(seq_string))
# print(var)
# print("".join(var))

# 15)wap to search for a character in a given string and return the corresponding index.
# def searchchar(anychar,givenstring):
#     for index,item in enumerate(givenstring):
#         if item==anychar:
#             return index,item
# print(searchchar('a','hello vishal'))

# 16) wap to get the below output**********
# sentence='hello world welcome to python programming hi there'
# from collections import defaultdict
# d=defaultdict(list)
# for item in sentence.split():
#     d[item[0]]+=[item]
# print(d)

# 17) wap to replace all the characters with - if the character occurs more than once in a string
# my_string= 'hellohai'
# for i in my_string:
#     if my_string.count(i)>1:
#         my_string=my_string.replace(i,"-")
# print(my_string)


# 18)write a decorator that returns only positive value of substraction.
# def positive(func):
#     def wrapper(*args,**kwargs):
#         result=func(*args,**kwargs)
#         return abs(result)
#     return wrapper

# @positive
# def sub(a,b):
#     return a-b
# print(sub(-3,6))



# 19)how to count the number of instances of a class that is being created.
# class point:
#     counter=0
#     def __init__(self,name):
#         self.name=name
#         point.counter+=1

# a=point('vivek')
# b=point('sunil')
# c=point('sandeep')
# d=point('ashish')
# print(point.counter)


# 20)wa fuction which takes a list of strings and integers. if the item is a string it should print as it is
#  and if the item is intger or float , it should reverse it.
# def revint(lst):
#     out=[]
#     for item in lst:
#         if type(item)==str:
#             out.append(item)
#         elif type(item)==int:
#             out.append(int(str(item)[::-1]))
#         else:
#             out.append(float(str(item)[::-1]))
#     return out


# def revint(lst):
#     out=[]
#     for item in lst:
#         if isinstance(item, str):
#             out.append(item)
#         elif isinstance(item,(int)):
#             out.append(int(str(item)[::-1]))
#         elif isinstance(item,(float)):
#             out.append(float(str(item)[::-1]))
#     return out

# print(revint(['vivek', 34, 23, 987, 'sandeep', 89.95, 84.3, 'nihal']))


# 21)make a class iterable
# class Cafe:
#     def __init__(self,menu):
#         self.__menu=menu
#         self.i=-1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.i+=1
#         if self.i<len(self.__menu):
#             return self.__menu[self.i]
#         raise StopIteration

# d=Cafe([1,2,3,4])
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))
# for item in d:
#     print(itme)

# or
# lst=['edureka','python','java']  here lst may be anything str/lst/tuple/set
# var=iter(lst)
# print(next(var))
# print(next(var))

# class UniversityClassIter:
#     def __init__(self,name, university_class):
#         self.name=name
#         self.university_class=university_class

#     def __iter__(self):
#         return self.name.__iter__()
# a=UniversityClassIter('saleem',[10,20,30])

# 22 Write a Custom class which can access the values of dictionaries using d['a'] and d.a

# class Mydict:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __getattribute__(self, index):
#         if index=='name':
#             return super().__getattribute__('name')
#         elif index=='age':
#             return super().__getattribute__('age')

#     def __getitem__(self, index):
#         if index == "name":
#             return self.name
#         elif index=='age':
#             return self.age

# d = Mydict("mamata", 10)

# print(d.name)
# print(d["name"])


# 23)wap to get the output
# st='hi how are you'
# # # out='ih woh era uoy'
# out=[i[::-1] for i in st.split()]
# var=" ".join(out)
# print(var)

# 24)wap to get the output
# st='hi how are you'
# # print(st[-1:-(len(st)+1):-1])
# print(st[::-1])

# 25)write a lambda function to add two numbers (a,b)
# var=lambda a,b:a+b
# print(var(2,3))

# 26)What is the output of the followinges
# a=[1,2,3]
# b=[4,5,6]
# print([a,b])
# print((a,b))

# 27)how to remove duplicates from the list without using inbuilt functions
# items=[1,2,3,4,1,2,3,4,5]
# st='hello how are you i am fine'
#print(list(set(items)))
# out=""
# for i in st:
#     if i not in out:
#         out+=i
# st=out
# print(st)


# 28)find the longest word in the sentence

# sentence='hello world welcome to python'
# d={item:len(item) for item in sentence.split()}
# var=sorted(d.items(), key=lambda i:i[-1])
# print(var[-1][0])

# or
# var=sorted(sentence.split(),key=lambda item:len(item))
# print(var[-1])


# 29)wap to reverse the values in the dictionary if the value is of type string
# d={'a':'hello','b':100, 'c':10.1, 'd':'world'}
# for i,j in d.items():
#     if isinstance(j,str):
#         d[i]=j[::-1]
# print(d)


# 30)wap to get 1234 from the below tuple
# a=('1','2','3','4')
# var="".join(a)
# print(var)

# 31)how to get the elements that are in the list b but not in the list a
# a=[1,2,3]
# b=[1,2,3,4]

# for i in b:
#     if i not in a:
#         print(i)

# 32) a function takes variable no of positional arguments as input. how to check if the arguments
#  that are passed are more than 5.
# def func(*args):
#     if len(args)>5:
#         return True
#     else:
#         return False
# print(func(10,20,30,40,50))

# 33) Count the no of occurances of 'critical', 'info' and 'error' messages.
# from collections import defaultdict
# with open(r"E:\vs code\sample.log",'r') as file:
#     d=defaultdict(int)
#     for line in file:
#         if line.strip():
#             var=line.split()
#             d[var[2]]+=1
#     print(d)

# 34) wa function to reverse any iterable without using reverse function
# def rev(any_iterable):
#     return any_iterable[::-1]
# print(rev(([1,2,3,4])))
# or
# nums = [1,2,3,4,5]

# res = []
# for num in nums:
#     res.insert(0,num)
# print(res)

# 35)write a function to print the below output
# func('TRACXN', 0)  should print 'RCN'
# func('TRACXN', 1) SHOULD PRINT 'TAX'

# def escape(any_str, index):
#     if index==0:
#         return any_str[1::2]
#     else:
#         return any_str[::2]
# print(escape('TRACXN',0))

# 36)sum all the numbers in the below string
# s="Sony12India567Pvt2Ltd"
# sum=0
# for i in s:
#     if '0'<=i<='9':
#         sum+=int(i)
# print(sum)

# or
# from re import findall
# matches=findall(r"\d",s)
# var=[int(item) for item in matches]
# print(sum(var))

# 37) wap to sum all the numbers in the below string
# st='Sony12India567Pvt2ltd'
# from re import findall
# var=findall(r"\d+", st)
# sum=0
# for i in var:
#     sum+=int(i)
# print(sum)

# 38)print all the numbers in the below list
# lst=['abc', '123','hello', '23']
# from re import findall
# for i in lst:
#     var=findall(r"\d+",i)
#     if var:
#         print(i)

# 39)wap to print no of occurances of characters in a string without using inbuilt function
# st='helloworld'
# d={item:st.count(item) for item in st}
# print(d)
# d={}
# for i in st:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)

# 40) wap to print only the repeated characters and count of the same
# s='helloworld'
# d={item:s.count(item) for item in s if s.count(item)>1}
# print(d)

# 41) wap to get alternate characters of a string in list format.
# s='helloworld'
# lst=[s[i] for i in range(0,len(s),2)]
# print(lst)

# or
# lst=[]
# for i in s[::2]:
#     lst.append(i)
# print(lst)

# 42) wap to get square of list of numbers using lambda function
# lst=[1,2,3,4,5]
# for item in lst:
#     var=lambda item:item**2
#     print(var(item))

# or
# var=map(lambda item:item**2,lst)
# print(list(var))


# By using map function
# def vaer(item):
#     return item**2
# var=map(vaer,lst)
# print(list(var))

# 43)write a function that accepts two strings and returns true if the two strings are anagrams of each other
# def check_anagram(data1,data2):
#     if set(data1) == set(data2):
#         return True
#     else:
#         return False
# print(check_anagram("eat","tea"))

# 44) wap to iterate through the list and build a new list, only if the items of the list has even no of characters.
# lst=['apple','yahoo','google','gmail','walmart','flipkart','facebook','amazon']
# out=[item for item in lst if len(item)%2==0]
# print(out)

# 45)wap to iterate through the list and build a new dictionary, only if the items of the list has even no of characters.
# lst=['apple','yahoo','google','gmail','walmart','flipkart','facebook','amazon']
# d={item:len(item) for item in lst if len(item)%2==0}
# print(d)

# 46)wap which squares the numbers in a list using map object
# def sqr(item):
#     return item**2
# var=map(sqr,[1,2,3,4,5])
# print(list(var))

# or
# res = list(map(lambda item: item**2,a))
# print(res)


# 47)count no of lines of a file without loading the file to the memory.
# with open(r"E:\vs code\sample.log",'r') as file:
#     c=0
#     for line in file:
#         if line.strip():
#             c+=1
#     print(c)


# 48)printing line and line no in a file
# with open(r"E:\vs code\sample.log", 'r') as file:
#     for line_no,line in enumerate(file, start=1):
#         if line.strip():
#             print(line_no,line)

# 49) wap to print sum of entire list and sum of only internal lists.
# l=[[1,2,3],[4,5,6],[7,8,9]]
# c=0
# for i in l:
#     print(sum(i))
#     c+=sum(i)
# print(c)

# 50) wap to reverse the list as belows
# lst=['hi','hello','python']
# res=['python','hello','hi']
# print(lst[::-1])

# or
# out=[]
# for item in lst:
#     out=[item]+out
# print(out)

# 51)wap to get the output
# a1=(1,2,3,4)
# b1=(100,200,300)
# out=(1,2,3,4,100,200,300)
# print(a1+b1)

# 52)wap to replace the value present in the nested dictionary
# d={'a':100, 'b':{'m':'man','n':'nose','o':'ox','c':'cat'}}
# d['b']['n']='eye'
# print(d)

# 53)wap to find the no of white spaces in a file
# from re import findall, finditer, sub
# with open(r"E:\vs code\sample.log", 'r') as file:
#     c=0
#     for line in file:
#         var=findall(r"\s",line)
#         c+=len(var)
#     print(c)

# 54)grouping anagrams
# lst=['listen','hello','eat','desserts','silent','peek','ate','keep','tea','stressed']
# def check_anagram(data1,data2):
#     if set(data1) == set(data2):
#         return True
#     else:
#         return False
# dk=[(lst[i],lst[j]) for i in range(len(lst)) for j in range(i+1,len(lst)) if i!=j]
# out=[]
# for item in dk:
#     if check_anagram(item[0],item[1]):
#         if item not in out:
#             out.append(item)
# print(out)

# # 55)difference between defaultdict and normal dict
# Defaultdict is a container like dictionaries present in the module collections. The functionality of both dictionaries and defaultdict
# are almost same except for the fact that defaultdict never raises a KeyError. It provides a default value for the key that does not exists.
# If you didn't use a defaultdict you'd have to check to see if that key exists, and if it doesn't, set it to what you want.

# 56)explain property decorator in python
# The property decorator is a built-in decorator for the property() function in Python.
# It is used to give "special" functionality to certain methods to make them act as getters, setters, or
# deleters when we define properties in a class.
# class Student:
#     def __init__(self, name):
#         self.__name = name

#     @property
#     def name(self):
#         return self.__name

#     @name.setter
#     def name(self, value):
#         self.__name=value

#     @name.deleter   #property-name.deleter decorator
#     def name(self, value):
#         print('Deleting..')
#         del self.__name
# s = Student('Steve')
# s.name -->'Steve'
# s.name='bill' #setter
# del s.name --->Deleting..

# 57)what is mutable and immutable data types
# The major difference between mutable and immutable objects in Python is that mutable
# objects can be modified or changed after their creation but the immutable objects can not be modified after their creation.

# 58)explain get methods in the dictionaries.
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = car.get("model")
# print(x)
# The get() method returns the value of the item with the specified key.

# 59)write a list comprehension to get a list of even numbers from 1 to 50
# lst=[item for item in range(1,51) if item%2==0]
# print(lst)

# 60)find the longest non repeated substring in the below string.
# s='This is a programming language and programming is fun'
# lst=[item for item in s.split() if s.split().count(item)==1]
# var2=sorted(lst,key=lambda item:len(item))
# print(var2[-1])

# 61)wap to find the duplicate element in the list without using inbuilt function
# names=['apple','google','apple','yahoo','google']
# lst=[]
# for i in range(len(names)):
#     for j in range(len(names)):
#         if i!=j:
#             if names[i]==names[j]:
#                 if names[i] not in lst:
#                     lst.append(names[i])
# print(lst)

# or
# for i in range(len(names)):
#     for j in range(i+1,len(names)):
#         if names[i]==names[j]:
#             print(names[i])

# 62)wap to count the no of occurances of each item in the list without using inbuilt function
# names=['apple','google','apple','yahoo','google','facebook','gmail','yahoo','apple']
# d={name:names.count(name) for name in names}
# print(d)
# or

# d={}
# for i in names:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# print(d)

# 63)write a function to check if the no if prime
# def prime(any_num):
#     for i in range(2, any_num):
#         if any_num%i==0:
#             return False
#     return True
# print(prime(57))

# 64)how to create a tuple of numbers from 0 to 10 by using range function
# t=[i for i in range(1,11)]
# print(tuple(t))

# or

# b=tuple()
# for i in range(1,11):
#     b=b+(i,)
# print(b)

# 65)get max output
# lst=[10,20,40,30,50]
# print(max(n))

# var=sorted(n)
# print(var[-1])

# large = 0
# for num in lst:
#     if num>large:
#         large = num
# print("largest number ", large)

# if asked smallest no
# small=lst[0]
# for i in lst:
#     if i<small:
#         small=i
# print(small)


# 66)write a method that returns last digit of an integer
# def ret_last(any_num):
#     return int(str(any_num)[-1])
# print(ret_last(19846743))

# 67)wap to find most common words in a given list
# words=['look','into','my','eyes','look','into','my','eyes','the','eyes','the','eyes','the','eyes','not','around','the','eyes','dont','look','around','the','eyes']
# 'look','into','my','eyes','you','are','under']
# d={item for item in words if words.count(item)>1} #it is a set comprehension
# print(list(d))

# or

# d={word:words.count(word) for word in words if words.count(word)>1}
# var=sorted(d.items(),key=lambda item: item[-1])
# print(var[-1][0])

# 68)make a function named tail that takes a sequence(like a list,string,tuple) and a number n and returns the last n elements from the
# given sequence, as a list.
# from logging import raiseExceptions

# def tail(any_collection, n):
#     if type(any_collection) in (list,str,tuple):
#         var=any_collection[-n:]
#         return list(var)
#     else:
#         raiseExceptions("only list ,string and tuple datatypes are allowed")
# print(tail([10,20,40,30,50],3))

# 69)check if the no if perfect square or not
# from math import sqrt,factorial
# def perfectsq(any_no):
#     x=int(sqrt(any_no))
#     if x**2==any_no:
#         return True
#     else:
#         return False
# print(perfectsq(82))

# 70)wap to get all the duplicate items and the no of times the item is repeated in the list.
# names=['apple','google','apple','yahoo','google','facebook','gmail','yahoo','apple']
# d={item: names.count(item) for item in names if names.count(item)>1}
# print(d.keys())

# 71)wap to count the no of occurances of each word in a file
# from collections import defaultdict
# with open(r"E:\vs code\sample.log",'r') as file:
#     c=0
#     d=defaultdict(int)
#     for line in file:
#         if line.strip():
#             var=line.split()
#             for item in var:
#                 d[item]+=1
#     print(d)


# extra
# this program counts the total no of words in a file
# with open(r"E:\vs code\sample.log",'r') as file:
#     c=0
#     for line in file:
#         if line.strip():
#             var=line.split()
#             c+=len(var)
#     print(c)


# 72)wap to count the no of occurances of vowels in a file
# from re import findall
# with open(r"E:\vs code\sample.log",'r') as file:
#     c=0
#     for line in file:
#         if line.strip():
#             var=findall(r"[aeiouAEIOU]", line)
#             c+=len(var)
#     print(c)

# # 73)wap to print all numeric values in a list
# lst=['apple',1.2,'google','12.6','26','100']
# from re import findall
# for i in lst:
#     if isinstance(i,str):
#         var=findall(r"\d",i)
#         if var:
#             print(i)
#     elif isinstance(i,(int,float)):
#         print(i)


# 74) rectangle patterns
# n=5
# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")
#     print()

#  right angle triangle pattern
# n=5
# for i in range(n+1):
#     for j in range(n):
#         if i+j>n-1:
#             print("*",end=" ")
#     print()

# left angle triagle
# n=5
# for i in range(n+1):
#     for j in range(n):
#         if i+j>n-1:
#             print("*",end=" ")
#         else:
#             print(' ',end=" ")
#     print()

# full triangle
# n=5
# for i in range(n+1):
#     for j in range(n):
#         if i+j>n-1:
#             print("*",end=" ")
#         else:
#             print(' ',end="")
#     print()


# diamond pattern
# n=5
# for i in range(n):
#     for j in range(n):
#         if i+j==n//2 or j-i==n//2 or i-j==n//2 or i+j==n+n//2-1:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()


# 75) wap to count the no of occurances of a particular word in a file
# def count_occurance(any_word):
#     with open(r"E:\vs code\sample.log",'r') as file:
#         c=0
#         for line in file:
#             if line.strip():
#                 var=line.split()
#                 if any_word in var:
#                     c+=var.count(any_word)
#         print(f"Count of {any_word} is {c}")

# count_occurance('INFO')


# 76)wap to map a product to a company and build a dictionary with company and list the products pair
# all_products=['iphone','mac','gmail','maps','iwatch','windows','ios','google drive','one drive']
# apple={'iphone','mac','iwatch','ios'}
# google={'gmail','maps','google drive'}
# microsoft={'windows','one drive'}
# from collections import defaultdict
# d=defaultdict(list)
# for item in all_products:
#     if item in apple:
#         d['apple_products'].append(item)
#     elif item in google:
#         d['google_products'].append(item)
#     else:
#         d['microsoft_products'].append(item)
# print(d)

# 77)wap to rotate the contents of the list
# lst = [1, 4, 6, 7, 2]
# lst= lst[2:] + lst[:2] #rotate clockwise,left rotate
# lst = lst[-3:] + lst[:-3] #rotate anticlockwise, right rotate
# print(lst)

# 78)wap to rotate the characters of the string
# st = 'helloworld'
# st= st[1:] + st[:1] #rotate clockwise,left rotate
# st= st[-1:] + st[:-1] #rotate anticlockwise, right rotate
# print(st)

# 79)wap to count the no of empty spaces in a given string
# st="hello vivek how are you"
# from re import findall
# var=findall(r"\s",st)
# print(len(var))

# 80)wap to print only non repeated characters in a string
# st="hello vivek how are you i am fine"
# for i in st:
#     if st.count(i)==1:
#         print(i)

# 81)wap to print all the consonants in the given string
# st='hello vivek how are you'
# from re import findall
# var=findall(r"[^aeiouAEIOU.\s\d]", st)
# print(var)

# 83)wap to count the no of commented lines in a file
# from re import findall
# with open(r"E:\vs code\access-log.txt",'r') as file:
#     c=0
#     for line in file:
#         if line.strip():
#             if line.startswith("#"):
#                 c+=1
#     print(c)

# 84)wap to find whether a year is leap year or not
# year=1004
# if (year%4 == 0 and year%100 != 0) or (year%400 == 0) :
#     print(year, "is a leap year.")
# else :
#     print(year, "is not a leap year.")

# 85)linear search
# A simple approach is to do a linear search, Start from the leftmost element of arr[] and one by one compare x with each element of arr[]
# If x matches with an element, return the index.
# If x doesn’t match with any of the elements, return -1.
# def linear(arr,x):
#     for i in range(len(arr)):
#         if arr[i]==x:
#             return i
#     return -1

# or
# def linear(arr,n):
#     for index,item in enumerate(arr):
#         if item==n:
#             print(index)

# print(linear([1,2,3,3,4],3))

# 86)diff bet range and xrange
# range()	                                                                xrange()
# Returns a list of integers.	                                            Returns a generator object.
# Execution speed is slower	                                            Execution speed is faster.
# Takes more memory as it keeps the entire list of elements in memory.	Takes less memory as it keeps only one element at a time in memory.
# All arithmetic operations can be performed as it returns a list.	    Such operations cannot be performed on xrange().
# In python 3, xrange() is not supported.	                                In python 2, xrange() is used to iterate in for loops.


# 87)wap to count no of capital letters in a string
# st='Hi How are You WelCome to Python'
# from re import findall
# matches=findall(r"[A-Z]",st)
# print(matches)
# print(len(matches))


# 88)right angle triangle pattern
# n=4
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()


# 89)wap to get the following output
# a=[1,2,3,4,5,6,7,8,9]
# i=0
# while i<len(a):
#     print(a[i:i+2])
#     i=i+2

# 90) wap to check if the elements in the second list is series continuation of items in the first list
# a=[10,12,14,16,18]
# b=[20,22,24,26,28]

# temp = list1[0] - list2[0]
# if len(list1) == len(list2):
#     for l1_item, l2_item in zip(list1, list2):
#         if l1_item  - l2_item == temp:
#             continue
#         else:
#             print("series has some missmatch nums ")

# else:
#     print("some missmatch")


# 91) diff bet append and extend
# append() adds a single element to the end of the list while .
# extend() can add multiple individual elements to the end of the list.
# append :-
# my_list = ['geeks', 'for', 'geeks']
# another_list = [6, 0, 4, 1]
# my_list.append(another_list)
# print(my_list)

# # extend:-
# my_list = ['geeks', 'for']
# another_list = [6, 0, 4, 1]
# my_list.extend(another_list)
# print(my_list)

# 92)wap to find first repeating character in a string
# st='helol vik how are you'
# d=[]
# for i in st:
#     if i not in d:
#         if i!=" ":
#             d.append(i)
#     else:
#         print(i)
#         break

# 93)
# from re import finditer
# sentence = "hello world welcome hello there hello there hello universe"

# def index_nth_occurance(any_string,any_substring, nth_occurance):
#     matches = finditer(any_substring,any_string)
#     for index,item in enumerate(matches):
#         if index==(nth_occurance-1):
#             print(item.start(), item.end())

# index_nth_occurance(sentence,'hello',2)

# 94)wap to print prime no from 1 to 50
# def prime(n):
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True
# lst=[i for i in range(1,51) if prime(i) and i>1]
# print(lst)


# 95) wap to sort a list which has mix of both odd and even no the sorted list should have odd no first and
# then even no
# a=[3,4,1,7,2,12,8,6,9,11]
# var=sorted(a)
# odd=[item for item in var if item%2==1]
# even=[item for item in var if item%2==0]
# print(odd+even)

# 96)wap to sort a list which has mix of both odd and even no, the sorted list should have odd no first and then even no, but odd no should
# be in ascending order and even no should be in descending order.
# a=[3,4,1,7,2,12,8,6,9,11]
# var=sorted(a)
# odd=[item for item in var if item%2==1]
# even=[item for item in var if item%2==0]
# print(odd+even[::-1])

# 97)wap to count no of occurances of non special characters in a given string
# from re import findall
# s='hello@world! welcome!!! Python$ hi how are you & where are you?'
# var=findall(r"[a-zA-Z]",s)
# print(var)
# print(f"no of non special characters in the string {len(var)}")

# 98) grouping flowers and animals in the given list
# items=['lotus-flower','lily-flower','cat-animal','sunflower-flower','dog-animal']
# from collections import defaultdict
# d=defaultdict(list)
# for item in items:
#     var=item.split("-")
#     name,category=var
#     d[category].append(name)
# print(d)

# or

# f=[]
# a=[]
# for item in items:
#     var=item.split("-")
#     if var[-1]=='flower':
#         f.append(var[0])
#     else:
#         a.append(var[0])
# grouping=[(i,j) for i in f for j in a]
# print(grouping)

# 99)grouping files with same extensions
# files=['apple.txt','yahoo.pdf','gmail.pdf','google.txt','amazon.pdf','facebook.txt','flipkart.pdf']
# from collections import defaultdict
# d=defaultdict(list)
# for item in files:
#     name,category=item.split(".")
#     d[category]+=[name]
# print(d)


# 100)filter only those characters except digits
# s='@hello12world34welcome!123'
# from re import findall
# var=findall(r"[^0-9]",s)
# print("".join(var))


# 101)count no of words in a sentence,ignore special characters
# sentence='hi there! how are you:) how are you doing today!'
# from re import findall
# var=findall(r"\b[a-zA-Z]+\b",sentence)
# print(len(var))


# 102)grouping even and odd numbers
# numbers=[1,2,3,4,5,6,7,8,9,10]
# from collections import defaultdict
# d=defaultdict(list)
# for i in numbers:
#     if i%2==0:
#         d[0]+=[i]
#     else:
#         d[1].append(i)
# print(d)

# 103) find all max numbers from the below list
# numbers=[1,2,3,0,4,3,2,4,2,1,0,4]
# var=sorted(numbers)
# for i in numbers:
#     if i==var[-1]:
#         print(i)

# or

# max_no=0
# for item in numbers:
#     if item>max_no:
#         max_no=item
# print(max_no)
# lst=[i for i in numbers if i==max_no]
# print(lst)


# 104)find all max length words from the below sentence
# sentence='hello world hi apple you yahoo to you'
# var=sentence.split()
# maximum=sorted(var,key=len)
# for i in var:
#     if len(i)==len(maximum[-1]):
#         print(i)

# 105)
# s='0-0,4-8,20-20,43-45'
# out=[]
# var=s.split(",")
# for i in var:
#     a,b=i.split("-")
#     for j in range(int(a),int(b)+1):
#          out.append(j)
# print(out)

# 106)can we override a static method in python
# yes, Static method definitions are unchanged even after any inheritance,
# which means that it can be overridden, similar to other class methods.
# class Test:
#     def method_one(self):
#         print("Called method_one")
#     @staticmethod
#     def method_two():
#         print("Called method_two")
#     @staticmethod
#     def method_three():
#         Test.method_two()
# class T2(Test):
#     @staticmethod
#     def method_two():
#         print("T2")
# a_test = Test()
# a_test.method_one()
# a_test.method_two()
# a_test.method_three()
# b_test = T2()
# b_test.method_two()


# 107)write a function which returns the sum of lengths of all the iterables
# def sum_len(any_iterable):
#     sum=0
#     for i in any_iterable:
#         sum+=len(i)
#     return sum

# print(sum_len(([1,2,3],(4,5),['apple','google','yahoo','gmail','flipkart'],{1,2,3},{'a':1,'b':2})))


# 108) Replace whitespaces with newline character in the below string
# sentence = "Hello world welcome to python"

# words = sentence.split()
# result = "\\n".join(words)
# print(result)

# 109)replace all vowels with astrix("*")
# s='hello world welcome to python'
# from re import sub
# var=sub(r"[aeiouAEIOU]", "*", s)
# print(var)


# 110)replace all occurances of 'java' with python in a file.

# with open(r"E:\vs code\hgt.txt", "r+") as file1:
#     with open(r"E:\vs code\hgt9.txt", "w+") as file2:
#         for line in file1:
#             if line.strip():
#                 var=line.replace('java','pythen')
#                 file2.write(var)


# 111)max sum of 3 no and min sum of 3 no
# n=[10,15,20,25,30,35,40,15,15]
# var=sorted(n)
# print(f"sum of max 3 no {sum(var[-3::])}")
# print(f"sum of min 3 no {sum(var[:3:])}")

# 112)get this output- ['PYTHON', 'POOL']
# input='python@#$%pool'
# out=[]
# from re import findall
# var=findall(r"[a-z]+",input)
# for item in var:
#     out.append(item.upper())
# print(out)

# 113) wap to print all the numbers which are ending with 5
# numbers=['1','12','123','12345','125','905','55','5','95655','5555']
# for i in numbers:
#     if i.endswith("5"):
#         print(i)

# 114)wap to get the indexes of each item in the below list
# names=['apple','google','apple','yahoo','yahoo','google','gmail','gmail','gmail']
# from collections import defaultdict
# d=defaultdict(list)
# for index,item in enumerate(names):
#     d[item].append(index)
# print(d)

# 115)wap to print 'Banglore' 10 times without for loop
# i=0
# while i<10:
#     print('Banglore')
#     i+=1

# 116)wap to print all the words which starts with letter 'h' in the given string
# st='hello world hi hello universe how are you happy birthday'
# for i in st.split():
#     if i.startwuth('h'):
#         print(i)

# or

# from re import findall
# var=findall(r"\bh\w+",st)
# print(var)

# 117)wap to print sum of all the even no in the given string
# st='hello 123 world 567 welcome to 9724 python'
# var=[int(i) for i in st if '0'<i<'9' and int(i)%2==0]
# print(sum(var))

# or

# from re import findall
# var=findall(r"[0-9]",st)
# lst=[int(i) for i in var if int(i)%2==0]
# print(sum(lst))

# # 118)wap to add each number in word1 and word2
# word1='hello 1 2 3 4 5'
# word2='world 5 6 7 8 9'
# for i in range(len(word1)):
#     for j in range(len(word2)):
#         if i==j and '0'<=word1[i]<='9' and '0'<=word2[i]<='9':
#             print(int(word1[i])+int(word2[j]))

# or

# for i,j in zip(word1,word2):
    # if "0"<=i<='9' and "0"<=j<='9':
#         print(int(i)+int(j))

# # 119)wap to filter out even and odd no in the given string
# from re import findall
# sentence = 'hello 123 world 456 welcome to python498675634'
# nums = findall(r"\d", sentence)
# odd_nums = [int(num) for num in nums if int(num)%2==1]
# even_nums = [int(num) for num in nums if int(num)%2==0]
# print(odd_nums)
# print(even_nums)


# 120)wap to print all the no which are starting with 8
# n=['857','987','8','120','888','547','7674','89']
# for i in n:
#     if i.startswith('8'):
#         print(i)


# 121)wap to remove duplicates from the list without using set or empty list
# l=[1,2,3,4,1,2,3,4,3,4,4]
# print(list(set(l)))

# or

# l=list(dict.fromkeys(l))
# print(l)

# or
# d={i:l.count(i) for i in l }
# print(list(d.keys()))

# 122)print all the missing numbers from 1 to 10 in the below list
# lst=[1,5,3,6, 7,9]
# for i in range(1,11):
#     if i not in lst:
#         print(i)

# 123)
# l1=[1,2,3]
# l2=['a','b','c']
# out=[]
# for i in l1:
#     for j in l2:
#         out.append(str(i)+j)
# print(out)


# 125)find output
# class Demo:
#     def greet(self):
#         print('hello world')
#     def greet(self):
#         print('hello universe')
# d=Demo()
# d.greet()

# 126)in the below list, find all the no pairs which result in 10 either when added or substracted
# a=[3,5,-4,8,11,1,-1,6]
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]+a[j]==10 or a[i]-a[j]==10 or a[j]-a[i]==10:
#             print((a[i],a[j]))

# # 127)write a decorator to prefix +91 to the original phone no
# def add_countrycode(func):
#     def wrapper(*args,**kwargs):
#         res=func(*args,**kwargs)
#         result='+91'+str(res)
#         return result
#     return wrapper

# @add_countrycode
# def phone(any_phone):
#     if len(str(any_phone))==10:
#         return any_phone

# print(phone(7057521047))

# 128)wap to get the below output
# d={'a':1,'b':2,'c':3,'d':4,'e':5}
# lst=[]
# for i in d.items():
#     if i[-1]%2==0:
#         lst.append(i[0])
# print(lst)

# 129)can we have multiple __init__ methods in a class
# yes

# class example:
#     def __init__(self):
#         print("One")
#     def __init__(self):
#         print("Two")
#     def __init__(self):
#         print("Three")
# e = example()

# 130) why python is object oriented programming language
# There are 4 major principles that make an language Object Oriented. These are Encapsulation, Data Abstraction,
# Polymorphism and Inheritance. These are also called as four pillars of Object Oriented Programming

# 131)what are .pyc files
# .pyc files are created by the Python interpreter when a .py file is imported. They contain the "compiled bytecode" of
# the imported module/program so that the "translation" from source code to bytecode (which only needs to be done once)
# can be skipped on subsequent imports if the .pyc is newer than the corresponding .py file, thus speeding startup a
# little. But it's still interpreted. Once the *.pyc file is generated, there is no need of *.py file, unless you edit it.

# 132)reverse the string without using inbuilt and slicing
# st='hello vivek how are you'
# out=''
# for i in st:
#     out=i+out
# print(out)

# 133)wap to get the below output
# input="10.20.30.40"
# # # output="40.30.20.10"
# out=""
# var=input.split(".")
# print(".".join(var[::-1]))


# 134)difference between while loop and for loop

# # 135)what are magic methods in python
# Magic methods in Python are the special methods that start and end with the double underscores. They are also called dunder methods.
# Magic methods are not meant to be invoked directly by you, but the invocation happens internally from the class on a certain action.

# 136)what is pylint
# Pylint is a static code analysis tool for the Python programming language. It is named following a
# common convention in Python of a "py" prefix.but includes the following features:

# Checking the length of each line
# Checking that variable names are well-formed according to the project's coding standard
# Checking that declared interfaces are truly implemented
# It enforces a coding standard
# Pylint analyses your code without actually running it.
# It checks for errors
# It can make suggestions about how the code could be refactored.

# 137)find output
# a=[1,2,3,4]*2
# out=[1, 2, 3, 4, 1, 2, 3, 4]

# 138)difference between is and == operator in python
# The == operator compares the value or equality of two objects,
# whereas the Python is operator checks whether two variables point to the same object in memory.

# 139)what is 'self' in class
# self represents the instance of the class.
# By using the “self” we can access the attributes and methods of the class in python.
# It binds the attributes with the given arguments.

# 140)diff bet assert and ifelse statement
# An if statement is a part of the logic of the code. The assert statement is used to validate input when debugging code.
# If the if statement's condition is False, the code continues from where we want it to.

# 141)difference between a module,package and a library
# The module is a simple Python file that contains collections of functions and global variables and with having a .py extension file.
# It is an executable file and to organize all the modules we have the concept called Package in Python.
# The package is a simple directory having collections of modules. This directory contains Python modules and also having __init__.py file by which the interpreter interprets it as a Package.
# The package is simply a namespace. The package also contains sub-packages inside it.
# The library is having a collection of related functionality of codes that allows you to perform many tasks without writing your code.
# It is a reusable chunk of code that we can use by importing it into our program, we can just use it by importing that library
# and calling the method of that library with a period(.).
# However, it is often assumed that while a package is a collection of modules, a library is a collection of packages.

# 142)using while loop,print this logic
# 1
# 12
# 123
# 1234

# i = 1
# while i<=4:
#     j=1
#     while j<=i:
#         print(j, end="")
#         j = j+1
#     print()
#     i = i+1

# By for loop
# n=5
# for i in range(n):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()



# 143)
# items=['$123.45','$434.23','$567.89']
# out=[]
# from re import findall
# for i in items:
#     var=findall(r"\d+\.\d+",i)
#     for item in var:
#         out+=[float(item)]
# print(out)


# # 144)generator function for febonacci series
# def fibonacci():
#     a = 0
#     b = 1
#     while True:
#         yield a
#         next_number = a + b
#         a = b
#         b = next_number
# d=fibonacci()
# print(next(d))
# for i in d:
#     print(i)


# 145)wap to print common character present in all the items in a list
# items = [ "glory", "grlass", "srighlt", "flirght"]
# for ch in items[0]:
#     if ch in items[1] and ch in items[2] and ch in items[3]:
#         print(ch)


# 146)function should accept a list and if any no divisible by 3 then modify to 33 or else keep it as it is
# def modify_list(any_list):
#     if type(any_list)==list:
#         for i in range(len(any_list)):
#             if any_list[i]%3==0:
#                 any_list[i]=33
#         return any_list
# print(modify_list([10,20,9,18,25,36,15]))


# 147)
# 123*
# 12*4
# 1*34
# *234

# n=4
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i+j==n+1:
#             print('*',end=' ')
#         else:
#             print(j,end=' ')
#     print()

# # 148)wap to map digits to its corresponding word
# d={'0':'zero','1':'one', '2':'two', '3':'Three','4':'four','5':'five', '6':'six','7':'seven'}
# def map_digit(any_digit):
#     if isinstance(any_digit,str) and '0'<=any_digit<='9':
#         if any_digit in d.keys():
#             return d[any_digit]
#     else:
#         raise Exception("only numbers inside a string are allowed")
# print(map_digit('5'))




# 149)read the file in reversed manner
# with open(r'E:\vs code\hgt.txt','r') as file:
#     var=file.readlines()
#     for line in var[::-1]:
#         print(line)

