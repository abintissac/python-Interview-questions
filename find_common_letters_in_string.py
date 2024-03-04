def common():
    a = input("Enter the first string: ")
    b = input("Enter the second string: ")
    a1 = set(a)
    b1 = set(b)
    print(a1)
    print(b1)
    lst = a1 & b1
    print("common letters are:",lst)

common()
