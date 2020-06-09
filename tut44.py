# Enumerate function
l1 = ["Bhindi", "Aloo", "chopsticks", "chowmin"]

i = 1
for item in l1:
    if i % 2 != 0:
        print(f"Jarvis please buy {item}")
    i += 1

# we can do the above using enumerate function

for index, item in enumerate(l1):
    if index % 2 == 0:
        print(f"Jarvis please buy {item}")
