class demo:
 a=10
 b=20
def__init__(self,c,d):
 self.c=c
 self.d=d
def display(self):
    print(self.c,self.d)
def ch_c(Self,new):
    self.c=new
@classmethod
def dis(cls):
    print(cls.a,cls.b)
    @staticmethod
    def msg():
     print("public acess specifiers")
    user=demo(10,20)
    user.display()
    user.ch_c(40)
    user.display()