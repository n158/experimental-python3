# -*- coding: UTF-8 -*-

def add_method2(cls):
    def method2(self):
        print('method 2')
        print(self.var)
    cls.method2 = method2
    return cls

@add_method2
class Best(object):
    def __init__(self):
        self.var = 'instance var'

    @staticmethod
    def method1():
        print('method 1')

obj = Best()
obj.method1()
obj.method2()
