# for loop

list1 = [["Harry", 1], ["Larry", 2],
           ["Carry", 6], ["Marie", 250]]
# dict1 = dict(list1)

for item in list1:
    print(item)

for item, value in list1:
    print(item, "and lolly is ", value)

items = [int, float, "Sumit", 5, 3, 3, 22, 21, 64, 23, 233, 23, 6 ]

for item in items:
    if str(item).isnumeric() and item >= 6:
        print(item)