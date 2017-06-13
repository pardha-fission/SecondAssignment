
'''
2)Question print numbers in descending if count is greater than one
'''

# converting the input string into a list
list1 = input('Enter your list:').split()

# converting the list elements i.e strings into integers
list1 = [int(x) for x in list1]

# counting the frequnecy of the elements by a ref "set"
set1 = set(list1)

l2 = []
for i in set1:
    if list1.count(i) > 1:
        l2.append(i)
# sorting the elements in descending order
l2.sort(reverse=True)

# printing the elements
for i in l2:print(i,end=" ")



