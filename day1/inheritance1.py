class siva:
    def hello(self):
        print("hello")
class baby1(siva):
    def hi(self):
        print("hi")
class baby2(siva):
    def bye(self):
        print("bye")
class gbaby(baby1):
    def goodbye(self):
        print("good bye")
b2=baby2()
b2.hello()
b2.bye()

gb=gbaby()
gb.hello()
gb.hi()
gb.goodbye()
