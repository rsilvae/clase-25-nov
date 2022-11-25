class Country:
    def __init__(self,Country,Currency,code="No tiene codigo"):
        self.Country=Country
        self.Currency=Currency
        self.code=code
    def change_curreny(self,a,b):
        self.Currency=a
        self.code=b
    def print(self):
        print(self.Country, " usa el/la ",self.Currency,"(",self.code,")")
