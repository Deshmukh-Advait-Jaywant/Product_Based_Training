class siva:
    def gold(self):
        print("price 5L")
    def car(self):
        print("price 3L")
class baby1(siva):
    def bank(self):
        print("deposited 2L")
class baby2(siva):
    def jwels(self):
        print("price 10L")

b1=baby1()
b1.bank()
b1.gold()
b1.car()

b2=baby2()
b2.jwels()
b2.gold()
b2.car()
