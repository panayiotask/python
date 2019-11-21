# 1
a=set([0,1,2,3,4,5])
b=set([2,4,6,8])
print(a.union(b))
print(a.intersection(b))

# 2
band=['mel','geri','victoria','mel','emma']
counts={}
for member in band:
    if member not in counts:
        counts[member]=1
    else:
        counts[member] += 1
    print(counts)

for name in counts:
    print(name, counts[name])

# 3
if {}:
    print ('hi') # nothing happens

d={'maggie': 'uk', 'ronnie': 'usa'}

