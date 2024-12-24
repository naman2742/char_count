#taking string as inout from the user:

str = input("Enter your string : ")

#storing each char of string in a list as a separate element:

list = []              
l = len(str)           

for x in range(0,l):
    list.append(str[x])          

#creting a list that includes all elements in the string but only once

for x in list:
    while list.count(x)>1:
        list.remove(x)
    else:
        continue
    
list.sort()
list.remove(" ")   #avoiding counting blank spaces

#counting all elements in the list(with every element at once) in the string 

for x in list:
    n = str.count(x)
    print(x, " : ", n)  #printing the number of occurrences of every element in the string
    n = 0