# -*- coding: utf-8 -*-
"""Assignment_5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QNXPZcxc6XNgpXDGUDpZwjVjn5yvXGXy
"""

#Task 1

a_tuple = ("The Institute", ("Best Mystery & Thriller", "The Silent Patient", 68821), 75717,
[1, 2, 3, 400, 5, 6, 7], ("Best Fiction", "The Testaments", 98291))
print(a_tuple[3][3])

#Task 2
the_tuple = (-10, 20, 25, 30, 40)
new_tuple=the_tuple[2:-2]
print(new_tuple)

#Task 3
book_info = (
("Best Mystery & Thriller","The Silent Patient",68,821),("Best Horror","The Institute",75,717),
("Best History & Biography","The five",31,783 ),("Best Fiction","The Testaments",98,291)
)
length=len(book_info)
print("Size of the tuple is:",length)
for i in range(length):
  print(book_info[i])

#Task 4

book_info = (("Best Mystery & Thriller","The Silent Patient",68821),
("Best Horror","The Institute",75717),
("Best History & Biography","The five",31783 ),
("Best Fiction","The Testaments",98291)
)
print('{} won the {} category', format (book_info[0][1],book_info[0][0]))

#Task 5
g_tuple = (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
user_input= int(input())
length = len(g_tuple)
count=0
for i in range(length):
  if g_tuple[i] == user_input:
    count=count+1
  else:
    count=count
print(user_input, "appears", count, "times in the tuple")

#Task 6

g_tuple = (10, 20, 30, 40, 50, 60)
list_1 = list(g_tuple)
list_2 = []
length = len(list_1)
for i in range(-1,-length-1,-1):
  list_2.append(list_1[i])
print(tuple(list_2))

g_tuple = ('a','b','c','d','e','f','g','h')
list_1 = []
length = len(g_tuple)
for i in range(-1,-length-1,-1):
  list_1.append(g_tuple[i])
print(tuple(list_1))

#Task 7

given_1 = {'A':90, 'B': 0}
given_2 = {'C':50}
new_dict = {}
new_dict.update(given_1)
new_dict.update(given_2)
print(new_dict)

#Task 8

input_1 = int(input())
dictionary_1 = {}
sum=0
count=0
for i in range(1,input_1+1):
  keys = input()
  values = int(input())
  dictionary_1[keys]=values
print(dictionary_1)
for values in dictionary_1.values():
   sum = sum + values
   count = count + 1
avg = sum// count
print(avg)

input_1 = int(input())
dictionary_1 = {}
sum=0
count=0
for i in range(0,input_1):
  keys = input()
  values = int(input())
  dictionary_1[keys]=values
print(dictionary_1)
for values in dictionary_1.values():
   sum = sum + values
   count = count + 1
print(sum)
print(count)
print("Average is",sum//count)

#Task 9

exam_marks = {'Cierra Vega': 175, 'Alden Cantrell': 200, 'Kierra Gentry': 165, 'Pierre Cox': 190}
new_dictionary = {}
i_user = int(input())
for key,value in exam_marks.items():
  if value >= i_user:
    n_value = value
    n_key = key
    new_dictionary[n_key] = n_value
  else:
    pass
print(new_dictionary)

#Task 10

g_dictionary = {'sci fi': 5, 'mystery': 3, 'horror': 14, 'young_adult': 2, 'adventure':9}
max = g_dictionary["sci fi"]
print(max)
for key,value in g_dictionary.items():
   if g_dictionary[key] >= max:
     max = g_dictionary[key]
     n_key = key
   else:
     max = max
print("The highest selling book genre is '" + n_key +"' and the number of books sold are "+ str(max) + ".")



#Task 11

a_string = "Python programming is fun"
a_string = a_string.lower()
print(a_string)
b_string = ""
new_dict = {}
c_1 = 0
for i in range(0, len(a_string)):
  if a_string[i] !=" ":
    b_string=b_string+a_string[i]
  else:
    pass
print(b_string)
for i in range(0,len(b_string)):
  if b_string[i] not in new_dict:
    key = b_string[i]
    new_dict[b_string[i]]=1
    #new_dict[b_string[i]] = new_dict[b_string[i]] + 1

  else:
    new_dict[b_string[i]] = new_dict[b_string[i]] + 1

    #key = b_string[i]
    #new_dict[b_string[i]]=1
print(new_dict)

a_string = input("Please write:")
a_string = a_string.lower()
b_string = ""
new_dict = {}
for i in range(0, len(a_string)):
  if a_string[i] !=" ":
    b_string=b_string+a_string[i]
  else:
    pass
for i in range(0,len(b_string)):
  if b_string[i] not in new_dict:
    key = b_string[i]
    new_dict[b_string[i]]=1
  else:
    new_dict[b_string[i]] = new_dict[b_string[i]] + 1
print(new_dict)

#Task 12

dict_1 = {'A': [1, 2, 3], 'b': ['1', '2'], "c": [4, 5, 6, 7]}
count=0
for key,value in dict_1.items():
  for i in value:
    count = count + 1
print(count)

dict_1 = {'A': [1, 2, 3, 4, 5], 'b': ['1', '2', '4'], "c": [4, 5, 6, 7]}
counting=0
for key,value in dict_1.items():
  for i in value:
    counting = counting + 1
print(counting)

#Task 13

list_1 = [("a", 1), ("b", 2), ("a", 3), ("b", 1), ("a", 2), ("c", 1)]
new_dict = {}
list_a=[]
list_b=[]
list_c=[]
for i in list_1:
  if i[0] == "a":
    for j in range(1,len(i)):
      l_1.append(i[j])
    new_dict.update({i[0]:l_1})
  elif i[0] == "b":
    for j in range(1,len(i)):
      l_2.append(i[j])
    new_dict.update({i[0]:l_2})
  else:
    for j in range(1,len(i)):
      l_3.append(i[j])
    new_dict.update({i[0]:l_3})
print(new_dict)

list_1 = [("a", 1), ("b", 2), ("a", 3), ("b", 1), ("a", 2), ("c", 1)]
new_dict = {}
list_a=[]
list_b=[]
list_c=[]
for i in range(len(list_1)):
  if list_1[i][0] == "a":
    for j in range(1,len(list_1[i])):
      list_a.append(list_1[i][j])
      new_dict["a"]=list_a
  elif list_1[i][0] == "b":
    for j in range(1,len(list_1[i])):
      list_b.append(list_1[i][j])
      new_dict["b"]=list_b
  else:
    for j in range(1,len(list_1[i])):
      list_c.append(list_1[i][j])
      new_dict["c"]=list_c
print(new_dict)

list_1 = [("a", 1), ("b", 2), ("a", 3), ("b", 1), ("a", 2), ("c", 1)]
new_dict = {}
new_list = []
for i in list_1:
  if i[0] not in new_list:
     new_list.append(i[0])
for i in new_list:
  l_1 = []
  for j in list_1:
    if j[0] == i:
       l_1.append(j[1])
    new_l=l_1
#print(new_list)
print(new_l)

#7
dic_1={'Harry':15, 'Draco':8, 'Nevil':19}
dic_2={'Ginie':18, 'Luna': 14}
dic_3={}
for key,value in dic_1.items():
  dic_3[key]=value
for key,value in dic_2.items():
  dic_3[key]=value
print(dic_3)

#19

myList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
b = []
index1 = 0
index2 = 0
index1 = 1
b = myList
while (index1 < 10):
  myList[index1] = index1 + 1
  index2 = 1
  while (index2 < index1):
     myList[index1] = b[index2-1] + myList[index2] - index1
     index2 = index2 + 1
  print(myList[index1])
  index1 = index1 + 1

#18

myList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
b = []
index1 = 0
index2 = 0
index1 = 1
b = myList
while(index1<10):
  myList[index1] = index1+2;
  index2 = 1;
  while(index2<index1):
     myList[index1] = b[index1]+myList[index2]-index1
     index2 = index2+1
  print(myList[index1])
  index1 = index1+1

(True and False) and (False and False) or True

#16

myList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
index1 = 0
index2 = 0
index1 = 1
while(index1<10):
   myList[index1] = index1+4
   index2 = 1
   while(index2<index1):
      myList[index1] = myList[index1] +myList[index2]-index1
      index2 = index2+1
   print(myList[index1])
   index1 = index1+1

#17

myList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
index1 = 0
index2 = 0
index1 = 1
while (index1 < 10):
  myList[index1] = index1 + 4
  index2 = 1
  while (index2 < index1):
    myList[index1] = myList[index1] + myList[index2] - index1
    index2 = index2 + 1
  print(myList[index1])
  index1 = index1 + 1