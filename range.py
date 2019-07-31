l = []

for s in range (2000,3200):
    if (s%7 == 0) and (s%5 !=0):
        l.append(str(s))
  
    else:
        pass
print(','.join(l))
        
