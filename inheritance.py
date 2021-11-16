class C:
    def __init__(self):
        print("c")
class B(C):
    def __init__(self):
        super().__init__()
        print("b")
b=B()