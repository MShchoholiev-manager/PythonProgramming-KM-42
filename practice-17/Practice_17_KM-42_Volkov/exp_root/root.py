def root2(num):
    return round(num ** (0.5), 2)

def root3(num):
    if num < 0:
        return round(-(-num) ** (1 / 3), 2)

    return round(num ** (1 / 3), 2)
