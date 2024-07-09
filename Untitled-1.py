
class a():
    def __init__(self):
        print("A")

    def display(self):
        print("your in class a") 

class b(a):
    def __init__(self):
        super().__init__()
        print("B")

    def display(self):
        print("your in class  b")


obj1=b()
b.display(b)



 