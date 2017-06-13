'''
this script creates a text file of 20 lines with random numbers in the range of 1 <--> 100
each line contains 10 numbers
then opens the file and prints us the required element if line index and element index is 
given.
'''



# import numpy module for random number generation or random module is also fine
import numpy as np

# initialize a list to hold the lines.
random_num_list = []

for i in range(20):
    # creting a list of 10 random numbers using numpy random.random_integers function
    x = np.random.random_integers(1,100,10)
    x = str(x).replace('[','').replace(']','')+'\n'
    random_num_list.append(x)
# creating a text file in write mode
with open('rand_num.txt','w+') as foo:
    foo.writelines(random_num_list)
# opening the text file in read mode
with open('rand_num.txt','r+') as foo:
    y = foo.readlines()

# printing the required element
print('the {0}th line {1}th element is {2}'.format(line_no+1,element_no+1,y[line_no].split()[element_no]))
