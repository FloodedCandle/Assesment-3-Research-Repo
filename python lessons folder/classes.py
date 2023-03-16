# class declaration
class cat():
    name:None
    age:None
    isHappy:None

    # contractor
    def __init__(self, name, age, isHappy):
        self.name = name
        self.age = age
        self.isHappy = isHappy

    def display(self):
        print("CAT")
        print("name", self.name)
        print("age", self.age)
        print("is happy", self.isHappy)

    def sound(self):
        print("MEOWWWWW IM IN PAIN")

# cat1 = cat()
# cat.name = "jack"
# cat.age = 6
# cat.isHappy = True
cat1 = cat("jack",7 ,True)

cat1.display()
cat1.sound()
cat2 = cat("miky",420 , False)
# cat2 = cat()
# cat2.name = "get rekt"
# cat2.age = 69
# cat2.isHappy = False

cat2.display()
cat2.sound()