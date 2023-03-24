#Python has commenting capability for the purpose of in-code documentaion
# comments start with a #, and Python will render the rest of the line as a comment.

# Commments can be used to explain Python code.
# Comments can be used to make the code more readable.
# Comments can be used to prevent execution when testing code.

# Python will ignore codes that start with #.

# Comments can be placed at the end of a line, and Python will ignore the rest of the line.
# Example
print("Hello, World!")#This is a comment

# Comment does not have to be text that explains the code, it can also be used to prevent Python from executing code:
# Example
# print("Hello, World!")
print("thanks, Bud!")

"MULTILINE COMMENTS"
# Python does not realy have a syntax for multiline comments.
# To add a multiline comment you could insert # for each line.

# Or, not quite as intended, you can use multiline strings.
# Since Python will ignore strings literals that are not assigend to a variable,you can add a multiline string(Triple quotes)in your code, and place your comment inside it:
"""
This is a comment
using more then
one line
"""
print("Hello, World!")

# As long as the string is not assigned to a variable, Python will read the code, but then ignore it, and you have made a multiline comment.
