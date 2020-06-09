# time module concept
import time

initial = time.time()
print(initial)

k = 0
while k < 15:
    print("This is me")
    time.sleep(2)
    k += 1
print("while loop ran in time =", time.time()-initial, "seconds")

initial2 = time.time()
print(initial2)
for i in range(15):
    print("This is me")
print("for loop ran in time =", time.time()-initial2, "seconds")

localtime1 = time.asctime(time.localtime(time.time()))
print(localtime1)
