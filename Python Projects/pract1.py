print("Python Starts")
print ('**********************************************************')
# Modules is a file containing code written by somebody else which can be imported and used in our programs. ex os, tensorflow etc
# Pip is used to download modules
# To import any mpodules we use the so called 'import' function
import os # example of import
# Now about comments Comments in Python are the lines in the code that are ignored by the compiler during the execution of the program.
# Now going on to comments single line comments are commented using single #
'''
Whereas multiple lines comments are commented using
triple quotes(''',''')
'''
# variable is a reserved memory location to store values.
'''
A variable name must start with a letter or the underscore character.
A variable name cannot start with a number.
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ).
Variable names are case-sensitive (name, Name and NAME are three different variables).
The reserved words(keywords) cannot be used naming the variable.
'''
x = 'Variable String'
y = 69 
z = 55.55
''' 
Here we assigned different values to x, y, z
i.e. differnet values to different reserved locations
i.e. x is assigned a string value
y an integer and z a float
'''
# Integer, float and string are data types
# Data types are the classification or categorization of data items.
# lets print the variables
print (x)
print (y)
print (z)
print ('>>>We printed the values of the variables that we assigned')
# Python is a fantastic language that automatically identifies the type of data for us
# Now to know the data type of the variables we use 'typeof' function for example.
print(type(x))
print(type(y))
print(type(z))
print ('>>>Here we printed the types of the values that we assigned to the variables')
# ARITHMETIC OPERATORS (+, -, *, /) 
print ('Using addition operator: 3 + 5 =  ', 3+5)
print ('Using subtraction operator: 8 - 5 =  ', 8-5)
print ('Using multiplication operator: 3 * 5 =  ', 3*5)
print ('Using division operator: 12 / 2 =  ', 12/2)
print ('>>This are the Arithmetic Operators')
# COMPARISON OPERATORS ( >, <, >=, <=, ==, !=)
a = 3 > 5
print ('Using Comparison operator > greater than: a =  ', a)
b = 3 < 5
print ('Using Comparison operator < less than: b =  ', b)
c = 3 >= 5
print ('Using Comparison operator greater than or equal to >= : c =  ', c)
d = 3 <= 5
print ('Using Comparison operator less than or equal to <= : d = ', d)
f = 5 == 5
print ('Using Comparison operator equal to == : f = ', f)
g = 6 != 8
print ('Using Comparison operator not equal to != : g = ', g)
print ('>>This are the Comparison Operators')