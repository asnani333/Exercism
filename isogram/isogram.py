def is_isogram(string):
    if string.isalpha():
        string = string.upper()
        if len(set(string))!= len(string):
            return False
        return True
    else:
        l = []
        for i in string:
            if i.isalpha():
                l.append(i)
                print(l)
        if len(l)!= len(set(l)):
            return False
        else:
            return True

        
