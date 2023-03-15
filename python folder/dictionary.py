# dictionary/arrys?

course={
    "name":"software development fundamentals",
    "duration":"8 weeks"
}

print(course)

print(course["name"])

# to add more keys in the arry
course["fee"]= 1000.00
course["copyright"]="Whitecliffe"

print(course)

# to remove keys in the arry
course.pop("fee")
print(course)

for x in course:
    print(x,course[x])