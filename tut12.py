s = set()
print(type(s))
l = [1, 2, 3, 4, 5]
s_from_list = set(l)
print(s_from_list)
print(type(s_from_list))
s.add(1)
s.add(2)
s.remove(2)
print(s_from_list)
s1 = {7, 8}
print(s.isdisjoint(s1))