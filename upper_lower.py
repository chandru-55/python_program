s = input("enter the string")
d = {'upper case':0,'lower case':0}

for c in s:
	if c.isupper():
		d["upper case"] += 1
	elif c.islower():
		d["lower case"] += 1
	else:
		pass
print("upper values:",d["upper case"])
print("lower values:",d["lower case"])
