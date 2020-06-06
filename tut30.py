# file  seek and tell function
f = open("test.txt")
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
print(f.seek(0))
print(f.readline())
f.close()

