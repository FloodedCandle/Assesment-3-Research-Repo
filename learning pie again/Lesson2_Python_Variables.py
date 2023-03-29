# In Python, variables are created when you assign a value to it:
# Example
x = 5
y = "Hello, World!"

# Python has no command for declaring a variable.

"VARIABLES"
# Variables are containers for storing data values.
# Example
x = 5
y = "Ya boi" 
print(x)
print(y)

# Variables do not need to be declared with any particual type, and can even change type  after they have been set.
x = 4 # x is the type int
x = "mema" # x is now the type str
print(x)

"CASTING"
# if you want to specify the data type of a variable, this can be done with casting.
# Example
x = str(3) # will be "3"
y = int(3) # will be 3
z = float(3) # will be 3.0

"GET THe TYPe"
# You can get the data typ of a variable with the:
type() #function.
#Example
x = 5
y = "me"
print(type(x))
print(type(y))

"SINGLE OR DOUBLE QUOTES?"
#String variables can be declared either by using single or double quotes:
x = "me"
#the same as 
x = 'me'

"CASE=SENSITIVE"
#variable names are case-sensitive
#Example
a = 4
A = "papi"
#A will not overwrite a

"VARIABLE NAMES"
#a variable can have short name(like x and y) or a more descriptive name(age, name, total_colume). 
# Rules for python variable:
# a variable name must start with a letter or the underscore character
# a variable name cannot start with a number.
# a variable name can only contain alpha-numeric characters and underscores(A-z, 0-9, and _)
# variable names are case-sensitive(age, Age and AGE are three different variables)
# a ariable name cannot be any of the python keywords.

"LEGAL VARIABLE NAME EXAMPLE"
myvar = 'jay'
my_var = 'jay'
my_var_ = 'jay'
myVar = 'jay'
MYVAR = 'jay'
myvar2 = 'jay'

"ILLEGAL VARIABLE NAMES EXAMPLE"
2myvar = 'joe'
my-var = 'joe'
my var = 'joe'

"MULTI WORD VARIABLE NAMES"
#Variable names with more than one word can be iffivuil to read.
#There are sveral techniques you can use to make them more readable:
"CAMEL CASE"
#Each word,  except the first,  starts with capital letter:
myVariableName = 'tommy'
"PASCAL CASE"
#Each word starts with a capital letter:
MyVariableName = 'tommy'
"SNAKE CASE"
#Easg ord is separated by an underscore character:
my_variable_name = 'tommy'
