# 1
x=3
# while x>=1: # infinite loop
#     print(x)

while x<1: # never gets called
    print(x)

# 2
gases=['He', 'Ne', 'Ar', 'Kr']
count=0
while count < 4:
    item=gases[count]
    print(item, count)
    count += 1

# 3
name='Mary'
if name == 'Lisa':
    print(name, 'plays saxophone')
elif name == 'Bart':
    print(name, 'rides skateboard')
else:
    print(name, 'lives in Springfield')

# 4
x=1
if x:
    print(x, ' is True')
else:
    print('False')

if 22.1:
    print('True')
else:
    print('False')

if 'hello':
    print('True')
else:
    print('False')

if [1,2]:
    print('True')
else:
    print('False')

if 0:
    print('True')
else:
    print('False')

if 0.0:
    print('True')
else:
    print('False')

if None:
    print('True')
else:
    print('False')

if False:
    print('True')
else:
    print('False')

if '':
    print('True')
else:
    print('False')

if []:
    print('True')
else:
    print('False')

if {}:
    print('True')
else:
    print('False')

if ():
    print('True')
else:
    print('False')
