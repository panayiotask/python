# 1
t=(1,)
print(t[-1]) #print last element
t2=tuple(range(100,201))
print('First item: ', t2[0]) # Print first item
print('Last item: ', t2[-1]) # Print last item

# 2
mylist=[23, 'hi', 2.4e-10];
for (count, item) in enumerate(mylist):
    print (count, item)

# 3
(first, middle, last)=mylist
print(first, middle, last)
(first,middle,last)=(middle,last,first)
print(first, middle, last)
