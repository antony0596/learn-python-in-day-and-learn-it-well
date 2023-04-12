# Prints the words "Hello World"
print('Hello World')

brand = 'Apple'
exchangeRate = 1.235235245
# %s is a placeholder for a string
# %d is a placeholder for an integer. Confusing, I know
# if we want to add spaces before an integer, can can add a number between % and d to indicate the desired length of the string. For instance '%5d' %(123) will print "  123" with 2 spaces in front of it so that the total length is 5.
# %f is a placeholder for a float
# in the below example (%4.2f) 4 means total length, including the decimal point, and 2 means the number of digits after the decimal point. If we did 5 instead of 4, we would get 5 digits total, including a space in front of the number
message = 'The price of this %s laptop is %d USD and the exchange rate is %4.2f USD to 1 EUR' %(brand, 1299, exchangeRate)
print(message)

# we can also use the format() method to format strings
# 'string to be formatted'.format(arguments to be inserted into the string)
# we use curly braces {} as placeholders for the arguments

message = 'The price of this {0:s} laptop is {1:d} USD and the exchange rate is {2:4.2f} USD to 1 EUR'.format(brand, 1299, exchangeRate)
print(message)

# We don't have to provide the order. It will be inferred from the order of the arguments
message = 'The price of this {} laptop is {} USD and the exchange rate is {} USD to 1 ER'.format(brand, 1299, exchangeRate)
print(message)

message1 = '{0} is easier than {1}'.format('Python', 'Java')
# 'Python is easier than Java'
print(message1)

message2 = '{1} is easier than {0}'.format('Python', 'Java')
# 'Java is easier than Python'
print(message2)

message3 = '{:10.2f} and {:d}'.format(1.234234234, 12)
# '      1.23 and 12'
print(message3)

message4 = {}.format(1.234234234)
# '1.234234234' no formatting is applied
print(message4)