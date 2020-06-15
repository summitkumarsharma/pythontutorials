# Multilevel Inheritance


class Dad:
    basketball = 1


class Son(Dad):
    dance = 1
    # basketball = 4

    def is_dance(self):
        return f"yes i can dance {self.dance} no of times"


class Grandson(Son):
    dance = 6

    def is_dance(self):
        return f" Jackson yeah ! yes i can dance awesomely {self.dance} no of times"


d1 = Dad()
s1 = Son()
gd = Grandson()
print(gd.is_dance())
print(gd.basketball)

# quiz
