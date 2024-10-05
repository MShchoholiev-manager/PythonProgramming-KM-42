i = (int(input("amount:")))
list1 = [ ]
for n in range(i):
    k = input("element:")
    list1.append(k)
    if (n == i-1):
        if n == 0:
            print(k)
        if n>=1:
            for l in range (i):
                l = list1.remove(k)
                if (n == i-1):
                    for k in list1:
                        print(k, end=", " f"and {l}")