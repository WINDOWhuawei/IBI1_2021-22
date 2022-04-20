import re
class Sale(object):
    def __init__(self,total_money,price): #use class to take	two	parameters in the fuction
        self.total_money=total_money
        self.price=price
    def choclate(self): #define the fuction
        i=0
        y=self.total_money
        x=self.price
        i=y//x #calculate the number of bars
        y=y%x #calculate the change that will be left over
        return (i,y) #i is the number of bars, while y is the change that will be left over
c=Sale(100,7) #example as total_money=100, price=7
print (Sale.choclate(c))
