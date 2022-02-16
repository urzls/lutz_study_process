from setwrapper import Set

'''
Наследует все атрибуты класса Set, но расширяет методы intersect
    и union, добавляя возможность обработки нескольких операндов; 
    обратите внимание, что “self” – по-прежнему первый аргумент
    (теперь сохраняется в списке аргументов *args); кроме того,
    обратите внимание, что теперь унаследованные операторы & и | 
    вызывают новые методы с двумя аргументами, но для одновременной 
    обработки более чем 2 операндов требуется вызов метода, 
    а не выражения:
'''

class MultiSet(Set):
    def intersect(self, *others):
        res = []
        for x in self:
            for other in others:
                if x not in other: break
            else:
                res.append(x)
        return Set(res)

    def union(*args):
        res = []
        for seq in args:
            for x in seq:
                if not x in res:
                    res.append(x)
        return Set(res)

