class calculator():
    def __init__(self,sq,qb,rt):

        sq=sq*sq
        qb=qb*qb*qb
        rt=rt**0.5
        
        self.sq=sq
        self.qb=qb
        self.rt=rt

c= calculator(12,23,9)
print(c.sq,c.qb,c.rt)