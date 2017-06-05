
'''
3)Given a string,swap all the lower case letters to upper case and vice versa,split the string with delimiter “ “ and join the string with “-”.Output the string.

I/O: input a string
O/P: output the modified string

Example:
	i/p: i am the GREATEST.
	o/p:I-AM-THE-greatest.

'''

text = input('Enter your input text: ')

text = text.swapcase()
text = text.replace(" ","-")
print(text)


