def frequency_words():
    str = input("enter a string ")
    print(str)
    a = str.split()
    print(a)
    d={}
    for i in a:
        if i not in d.keys():
            d[i]=0
        d[i] = d[i]+1
    print(d)
frequency_words()