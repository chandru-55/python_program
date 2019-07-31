'''
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
'''
s = input("enter the string")
d = {"upper case"=0,"lower case"=0}

for c in s:
	if c.isupper():
		d["upper case"] += 1
	elif c.islower():
		d["lower case"] += 1
	else:
		pass
print("upper values:",d["upper case"])
print("lower values:",d["lower case"])

'''
'Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
​
Hints: 
Consider use range(#begin, #end) method
'''

'''
'Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
'''
v=input()
l=v.split(',')
t=tuple(l)
print(l)
print(t)

'''

Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
​
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''
item=[x for x in input().split(',')]
item.sort()
print(','.join(item))