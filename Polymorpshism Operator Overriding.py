class box:
    def __init__(self,weight):
        self.weight=weight
    def __add__(self,other):
        return self.weight+other.weight
c1=box(695)
c2=box(690)

print("weight is=",c1+c2)