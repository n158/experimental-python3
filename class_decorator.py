def add_method2(s1):
    
    def method2(s2):
        print('method 2')
        print(s2.var)
    s1.method2 = method2
    return s1

@add_method2
class Best(object):
    def __init__(self):
        self.var = 'instance variable'
        
    @staticmethod
    def method1():  # static method don't require self parameter
        print('method 1')

obj = Best()
obj.method1()
obj.method2()


"""
method 1
method 2
instance variable
"""
