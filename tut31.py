with open("test.txt") as f:
    a = f.readlines()
    print(a)

f = open("test.txt")
print(f.read())
f.close()