# if __name__==__main__ usage & necessity


def show_1(string1):
    return f"Give this string to {string1}"


def show_2(num1, num2):
    return num1 + num2 + 5


print("the module name is -", __name__)


if __name__ == '__main__':
    print(show_1("me"))
    a = show_2(3, 4)
    print(a)