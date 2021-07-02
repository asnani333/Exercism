def score(word):
    w = list(word.lower())
    print(w)
    value = 0
    for i in w:
        if i in ('a','e','i','o','u','l','n','r','s','t'):
            value+= 1
        elif i in ('d','g'):
            value+= 2
        elif i in ('b','c','m','p'):
             value+= 3
        elif i in ('f','h','v','w','y'):
            value+= 4
        elif i in ('k'):
            value+= 5
        elif i in ('j', 'x'):
            value+= 8
        elif i in ('q', 'z'):
            value+= 10
    return value
