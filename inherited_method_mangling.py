import inspect

class AA:
    def a(self):
        print("A")

class A(AA):
    def b(self):
        print("B")
    
    def c(self):
        self._c("C")
    
    def _c(self, c):
        """
        _c: this convention is used for declaring private variables, functions,
        methods and classes in a module. Anything with this convention are
        ignored in from module import *. But we can not force somethings
        private ones and also can call it directly from other modules. So
        sometimes we say it “weak internal use indicator”.
        :param c:
        :type c:
        :return:
        :rtype:
        """
        print(c)
    
    def _single_method(self):
        pass
    
    def __double_method(self):  # for mangling
        print("AA")
        pass

class B(A):
    
    def __double_method(self):  # for mangling
        print("BA")
        pass

print([x for x in inspect.getmembers(A) if x[0][0] != '_'])

print([x for x in inspect.getmembers(B) if x[0][:2] != '__'])

a = A()
aa = B()
b = a.a
c = a._c("FFF")
b()
a.c()

aa._A__double_method()  # mangling call example
aa._B__double_method()


"""
[('a', <function AA.a at 0x02C134F8>), ('b', <function A.b at 0x02C13D20>), ('c', <function A.c at 0x02CAAE40>)]
[('_A__double_method', <function A.__double_method at 0x02CAAF18>), ('_B__double_method', <function B.__double_method at 0x02CAAF60>), ('_c', <function A._c at 0x02CAAE88>), ('_single_method', <function A._single_method at 0x02CAAED0>), ('a', <function AA.a at 0x02C134F8>), ('b', <function A.b at 0x02C13D20>), ('c', <function A.c at 0x02CAAE40>)]
FFF
A
C
AA
BA
"""
