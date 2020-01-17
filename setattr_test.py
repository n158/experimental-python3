# -*- coding: UTF-8 -*-


class Object:
    attr1: None
    attr2: None
    attr3: None


if __name__ == '__main__':
    params = {'attr1': '1', 'attr2': '2', 'attr3': '3'}
    obj = Object()
    for p in params:
        setattr(obj, p, params[p])
    
    print(obj.attr1)
    print(obj.attr2)
    print(obj.attr3)

    # Output:
    # 1
    # 2
    # 3
