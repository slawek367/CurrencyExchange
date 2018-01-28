def singleton(cls):
    def __new__(cls, *args, **kwargs):
        try:
            return cls.__instance
        except AttributeError:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        
    cls.__new__ = staticmethod(__new__)
    return cls

@singleton
class Config():
    depositTax = 0.01
    startUsdMoney = 2000;

'''
singleton test:

conf = Config()
conf.depositTax = 2

conf2 = Config()
conf2.depositTax = 3

print(conf.depositTax)
print(conf2.depositTax)
'''