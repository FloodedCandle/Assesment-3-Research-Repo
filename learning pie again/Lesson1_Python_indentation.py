# Indentation refers to the spaces at the beginning of a code line,

# Where in other programming languages the indentation in code is for readbility only, the indentation in Python is very important.

# Python uses indentation to indicate a blocke of code.
# Example
if 5 > 2:
    print("five is grater than two!")

# Python will give you an error if you skip the indentation:
# Example
if 5 > 2:
print("five is grater than two!")

# The number of spaces is up to you as a programmer, the most common use is four, but it has to be at least one.
# Example
if 5 > 2:
    print("five is grater than two!")
if 5 > 2:
               print("five is grater than two!")

# You have to use the same number of spaces in the same block of code, otherwise Python will give you an error:
# Example
if 5 > 2:
    print("Five is greater than two!")
        print("Five is greater than two!")


