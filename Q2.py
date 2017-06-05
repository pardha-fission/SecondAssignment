
'''
2)Question print numbers in descending if count is greater than one
'''
list1 = input('Enter your list:').split()

list1 = [int(x) for x in list1]


set1 = set(list1)
print(set1)
l2 = []
for i in set1:
    if list1.count(i) > 1:
        l2.append(i)

l2.sort(reverse=True)

for i in l2:print(i,end=" ")



