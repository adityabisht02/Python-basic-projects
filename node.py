class treenode:
    def __init__(self, data):
        self.data=data;


class data:
    def __init__(self, sepallength, sepalwidth,petallength,petalwidth,speciesname):

        self.sepallength = sepallength;
        self.sepalwidth = sepalwidth;
        self.petallength = petallength;
        self.petalwidth = petalwidth;
        self.speciesname = speciesname;

class operationnode:
    def __init__(self,operation):
        self.operation=operation;

def operationfunc(opernode,p1,p2):
    if(opernode=="*"):
        return p1.data.sepallength*p2.data.sepallength;

p1 = treenode(10,5,4,3,"flower");
p2=treenode(22,21,3,4,"garbage");

multiply=operationnode("*");



print(p1.sepallength*p2.sepallength);
        
