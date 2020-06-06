# F Strings

import math
me = "Sumit"
a1 = 1
# a = "This is %s %s "%(me, a1)
a = "This is {1} {0}"
b = a.format(me, a1)
b = f"This is {me} {a1} {4*65} {math.cos(60)}"
print(b)