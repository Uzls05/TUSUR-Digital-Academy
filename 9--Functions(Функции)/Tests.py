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


say_hi("Man")
print_max(6,6)