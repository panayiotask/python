# 1
x=[1,2,3,4,5]
print(x)
print(x[1]) #print second item
print (x[-2]) #print second to last
print (x[0:]) #select the whole list
print (x[1:5]) #select 2nd to 4th items inclusive

# 2
y=list(range(10))
print(y)
y[0]=10 #replace 1st item with 10
print(y)
y.append(11) #append no. 11 at the end
print(y)
y2=[12,13,14]
y.extend(y2) #extend list with another list
print(y)

# 3
forward=[]
backward=[]

values=['a','b','c']

for value in values:
    forward.append(value)
    backward.insert(0,value)
print(forward)
print(backward)

forward.reverse() #reverse order
print(forward == backward)

# 4
countries=['uk','usa','uk','uae']
dir(countries)
#help(countries.count)
countries.count('uk') #printed when in python shell, otherwise...
print(countries.count('uk'))
