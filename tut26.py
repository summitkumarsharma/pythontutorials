# file handling - read operation
f = open("test.txt")
content = f.read()
print(content)

# content = f.read(3445)
# print("1", content)
# content = f.read(3445)
# print("2", content)

# for line in content:
#     print(line)
# for line in f:
#     print(line)
# for line in f:
#     print(line, end="")

# content = f.readline()
# print(content)
# content = f.readline()
# print(content)
# content = f.readline()
# print(content)

# content = f.readlines()
# print(content)
f.close()