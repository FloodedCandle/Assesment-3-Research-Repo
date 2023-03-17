# class declaration
class cat():
    name: None
    age: None
    isHappy: None

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


class DomesticCat(cat):
    owner: None

    def display(self):
        print("domestic CAT")
        super().display()
        print("Owner", self.owner)

    
    def __init__(self, owner, name, age, isHappy):
        super().__init__(name, age, isHappy)
        self.owner = owner


class WildCat(cat):
    def hunt(self):
        print("im hunting....PLS")

    def sound(self):
        print("")


cat1 = WildCat("jack", 7, True)

cat1.display()
cat1.sound()

cat2 = DomesticCat("timm","jack" ,6,True)


cat2.display()
cat2.sound() 
