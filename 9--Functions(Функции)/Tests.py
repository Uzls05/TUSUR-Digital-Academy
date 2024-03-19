def say_hi(name):
    name = name.capitalize()
    print(f"HI,{name}")


def print_max(a,b):
    if a > b:
        print(f"{a},is max")
    elif a == b:
        print(f"{a}, equals to {b}")
    else:
        print(f"{b},is max")


def get_max_value(a, b):
    if a > b:
        return a
    elif a == b:
        return None
    return b


say_hi("Man")
print_max(6,6)
a = 1
b = 1
max_value = get_max_value(a, b)
if max_value is None:
    print(f"{a},equals to {b}")
else:
    print(f"{max_value} is max")