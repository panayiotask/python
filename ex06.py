# 1
s=('I love to write python')
for l in s:
    print(l)
print(s[4])
print(s[-1])
print(len(s))
print(s[0])
print(s[0][0])
print(s[0][0][0])

# 2
s=('I love to write python')
split_s=s.split(' ')
print(split_s)
for word in split_s:
    if word.lower().find('i') !=-1:
        print('I found "i" in:', word)

# 3
something=('Completely Different')
dir(something)
t=something.count('t')
print(t)
plete=something.find('plete')
print(plete)
split=something.split('e')
print(split)
thing2=something.replace('Different', 'Silly')
print(thing2)
# something[0]='B'
