class Person:
    def __init__(self,n,g,a):
        self.name=n
        self.gender=g
        self.age=a
    def talk(self):
        print("hi this is ",self.name)
    def vote(self):
        if self.age<18:
            print("not eligible")
        else:
            print("eligible to vote")
ob1=Person("siri","female",23)
ob2=Person("giri","male",16)
ob1.talk()
ob1.vote()
ob2.talk()
ob2.vote()
