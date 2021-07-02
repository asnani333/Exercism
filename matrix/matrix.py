class Matrix:
    def __init__(self, matrix_string):
        l = matrix_string.split('\n')
        self.l = list(l)
        self.a = []
        for i in self.l:
            self.a.append(list(map(int,i.split(" "))))

    def row(self, index):
        return self.a[index-1]
    
    def column(self, index):
        m =[]
        for i in self.a:
            m.append(i[index-1])
        return m