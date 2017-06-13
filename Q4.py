'''
4)Given two values a and b.print a/b ,in the case of exception print the error code.(Use Exceptions)

I/O: input a and b
O/P: a/b or the error code

Example:
i/p: 2 0
o/p: integer division or module by zero
i/p: 2 $
o/p: invalid literal for int() with base 10
'''


try:
    a = int(input('enter the numerator: '))
    b = int(input('enter the denominator: '))
    print('{0}/{1} = {2}'.format(a,b,(a/b)))


except ValueError as e:
    print('{0} is not an integer'.format(e))

except ZeroDivisionError as e:
    print('Division by Zero is Infinite')


