'''
1) Question check if number is a prime and it's first bit is set
'''

def is_prime(integer):
    for number in range(2,integer//2+1):
        if integer % number ==0:
            return False
    return True

def is_bit_position_set(integer,position):
    bin_val = str(bin(integer))
    if bin_val[-(position+1)] == '1':
        return True
    return False


list1 = [1,7,13,17]
for element in list1:
    if is_prime(element) and is_bit_position_set(element,1):
        print('yes')
    else:
        print('no')





