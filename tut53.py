# Creating Our First Class In Python


class Student:
    pass


st1 = Student()
st2 = Student()
print(st1, st2)

# creating instance variables of  object student1
st1.name = "John"
st1.std = 12
st1.section = 1

# creating instance variables of  object student2
st2.name = "James"
st2.std = 11
st2.section = 2
st2.subjects = ["Hindi", "Physics", "English"]
print(st1.name, st2.subjects)
