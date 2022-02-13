'''
hsh = {1: 'a', 2: 'b', 3: 'c'}
k = hsh.keys() [2]
print(k)

from random import randint
arr = [elem for elem in range(randint(2,10))]
res = ''
for elem in arr:
    res += str(elem)

print(res)

arr2 = ['dog', 'cat', 'fisher', 'eggplant']
string = 'abracadabra'
#print(string[1])
#print(string.replace('b', '___', 1))

slicer = string[0:6]
slicer = slicer[::-1].replace('a', '___', 1)[::-1]
#print(slicer + string[6::])
print(list(string))


word = 'I love potato'
print(word.split(' '))
'''
arr = list(range(1,101))
for elem in arr:
    if elem % 3 == 0:
        print('foo')
    elif elem % 5 == 0:
        print('bar')
    
