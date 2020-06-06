# file handling - write operation

# f = open("test-write.txt", "w")
# content = "To write to an existing file, you must add a parameter to the open()function" \
#           "\n1.a - Append - will append to the end of the file \n2.w - Write - will overwrite any existing content"
# no_of_chars = f.write(content)
# print("File content is written ")
# print("Number of Characters written - ", no_of_chars)
# f.close()
#
#
# f = open("test-write.txt", "a")
# content = "\n3.r - open the file in read mode - default mode \n" \
#           "4.w - open the file in write mode\n5.x - create file if not exits"
# f.write(content)
# print("content is appended")
# f.close()

f = open("test-write.txt", "r+")
print(f.read())
f.write("\nEnd of file")
f.close()

