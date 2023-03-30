"Python Variables - Assign Multiple Values"

"Many Values to Multiple Variables"
# Python allows you to assign values to multiple variables in one line:
x , y, z = "yellow" , 'green', 'blue'
print(x)
print(y)
print(z)

"One Value to Multiple Variables"
# And you can assign the same value to multiple variables in one line:
x , y, z = "yellow"
print(x)
print(y)
print(z)

"Unpack a Collection"
# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", 'cherry']
x, y, z = fruits
print(x)
print(y)
print(z)

"OUTPUT VARIABLES"
#The python print() funcion is often used to output variables.
x = 'help me'
print(x)
#in the print() function, you output multiple variables, separated by a comma:
x = 'pls '
y = 'help '
z = 'me'
print(x,y,z)
#u can also use + operator to output multiple variables.
print(x+y+z)
#Notice the space character after 'pls ' and 'help ', without them the result would be "plshelpme".

#for numbers, the + character works as a mathematical operator:
x= 5
y= 10
print(x+y)

#The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:

x = 5
y = "John"
print(x, y)