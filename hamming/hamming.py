
def distance(strand_a, strand_b):
    if len(strand_a) == len(strand_b):
        a = list(strand_a)
        b = list(strand_b)
        count = 0
        for i,j in zip(a,b):
            if i != j:
                count+=1
        return count
    else:
        raise ValueError(".+")

