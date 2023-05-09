# 1. abs(number)
number = -32.3
complex_number = 3 + 4j

print(abs(number))  # 32.3
print(abs(complex_number))  # 5.0
# Возвращает абсолютное значение числа. Может быть применена к int, float, complex(x) (вернется величина), или к обьекту, реализующему функцию __abs__()
# Результат всегда положителен

# 2. aiter()

# 3. iter(object, [sentinel] = индикатор)
# Вызов функции  и интерпретация первого аргумента сильно зависят от наличия значения sentinel: в случае если он не подается на вход, то object должен быть
# итерируемым Обьектом-Коллекцией(Последовательность(Sequence): Изменяемая - (Список -List), Неизменяемые - (Строка - Str, Кортеж - Tuple), - ИТЕРИРУЕМЫЕ
# Множества(Sets): Изменяемое - Множество(Set), Неизменяемое - Неизменное множество(Frozenset), Отображение (Mapping): Словарь(Dictionary)) - НЕ ИТЕРИРУЕМЫЕ
# Или он должен поддерживать протокол последовательности метод __getitem__() с целыми аргументами, начиная с 0.

# Если передается аргумент sentinel, то ожидается, что первый аргумент object, поддерживает вызов __call__(). В этом случае созданный итератор будет вызывать указанный объект с каждым обращением
# к своему __next__() и проверять полученное значение на равенство со значением, переданным в аргумент sentinel. Если полученное значение равно sentinel, то бросается исключение StopIteration,
# иначе возвращается полученное значение.


class MyIterable(object):
    def __init__(self):
        self.index = 0
        self.items = [1, 2, 3, 4]

    def __call__(self):
        value = self.items[self.index]
        self.index += 1
        return value


x = iter(MyIterable(), 3)

print(next(x))  # 1
print(next(x))  # 2
# print(next(x)) # StopIteration

x = iter(['Apple', 'Banana', 'Orange'])
print(next(x))  # Apple
print(next(x))  # Banana
print(next(x))  # Orange

# 4. next(iterator, [default])
# Возвращает следующий элемент итерируемого обьекта методом __next__(). При подаче default, при проходе последнего элемента обьекта, возвращает default, иначе, StopIteration

x = iter((1, 2, 3, 4.5))
print(next(x))  # 1
print(next(x))  # 2
print(next(x))  # 3
print(next(x))  # 4.5

x = iter([56, 32, 12])

new_item = next(x)
print(new_item)  # 56

new_item = next(x)
print(new_item)  # 32

new_item = next(x)
print(new_item)  # 12

# 5. all(iterable) и any(iterable)
#                     def all(iterable):                                            def any(iterable):
#                         for element in iterable:                                      for element in iterable:
# all(iterable)  <==>         if not element:               any(iterable)  <==>             if element:
#                                 return False                                                  return True
#                         return True                                                   return False
# Возвращает True, если все элементы итерируемого обьекта = True <==> Они все ненулевые или обьект пуст - all()
#
# Возвращает True, если хотя бы один элемент итерируемого обьекта = True <==> Есть хотя бы один ненулевой элемент - any()
#
item_list = [True, True, True, True]
print(all(item_list))  # True
print(any(item_list))  # True

item_list = []
print(all(item_list))  # True
print(any(item_list))  # False

item_list = [5, 3.7, 0, 10]
print(all(item_list))  # False
print(any(item_list))  # True

# 6. bin(int)
# Переводит int в десятичной форме счисления в строку - содержащую это число в двоичной, добавляя в начале строки '0b'
# Если же подается не int, то обьект должен поддерживать метод __index__(), который вернет int

print(bin(3))  # '0b11'
print(int(bin(3)[2:]))  # 11
print(f'{14:#b}', f'{14:b}')  # '0b1110', '1110'

# 7. class bool(x)
# Проводит стандартную проверку истинности выражения, возвращая True или False:
# По умолчанию любой обьект считается True, если только он не поддерживет метод __bool__(), который возвращает False, или поддерживает метод __len__(), который возвращает 0
# Список наиболее частых обьектов, значение которых при проверке истинности равно False:
# • Обьект - константа, определяемая как False: None/False
# • Обьект нулевой - 0, 0.0, Oj, Decimal (0), Fraction (0, 1)
# • Обьект - пустая последовательность или коллекция - '', (), [], {}, set (), range (0)
# Операции и функции, возвращающие Булевы значения, возвращают 0 или False в случае False и 1 или True в случае True

print(int(bool(item_list)))  # 1

for i in item_list:
    print(bool(i), end=' ')  # True, True, False, True
print()

# 8.chr(int),  int < 1114111
# Преобразует целое число в символ Юникода, обратная функция - ord()
# Функция вернет строку, соответствующую переданному на вход целому числу из таблицы символов Unicode

print(chr(ord('§')))  # '§'

print(chr(3486))  # 'ඞ' - АМОГУС!

# 9.ord(str)
# Возвращает порядковый номер переданного символа по системе Unicode

print(ord('ඞ'))  # 3486

# 10. callable(x)
# Принимает обьект с одним аргументом. Возвращает True, если обьект КАЖЕТСЯ вызываемым, и False, если обьект точно не вызывается
# Важно, что даже если callable() вернул True, вызов обьекта может сопровождаться ошибкой
# Однако, если callable() возвращает False, вызов обьекта обязательно завершится ошибкой

x = 5
print(callable(x))  # False


def testfunction():
    print('test')


y = testfunction()  # 'test'
print(callable(y))  # True


class Foo:
    def __call__(self):
        print('testcall')


print(callable(Foo))  # True


class Foo2:
    @staticmethod
    def printsmth():
        print('something')


print(callable(Foo2))  # True

# 11. CLASS bytes, bytesarray
# Байты отличаются от массива байтов лишь тем, что последний - изменяемый обьект, а по сути bytes представляет собой строку в байтах
# Создадим байтовую строку:

print(b'bytes')  # b'bytes'

print('Байты'.encode('utf-8'))  # b'\xd0\x91\xd0\xb0\xd0\xb9\xd1\x82\xd1\x8b'

print(bytes('bytes', encoding = 'utf-8'))  # b'bytes'

print(bytes([ord('H'), ord('e'), ord('l'), ord('l'), ord('o'), ord(' '), ord('W'), ord('o'), ord('r'), ord('l'), ord('d'), ord('!')]))  # b'Hello World!'

# Функция bytes принимает список чисел от 0 до 255 и возвращает байты, получающиеся применением функции chr
# Хотя байтовые строки поддерживают практически все строковые методы, с ними мало что нужно делать. Обычно их надо записать в файл/прочесть из файла и преобразовать во что-либо другое
# Для преобразования в строку используется метод decode:

print(b'\xd0\x91\xd0\xb0\xd0\xb9\xd1\x82\xd1\x8b'.decode('utf-8'))  # 'Байты'

b = bytearray(b'hello world!')
print(b)  # bytearray(b'hello world!')
print(b[0])  # 104
# b[0] = b'h'
# TypeError: an integer is required
b[0] = 105
print(b)  # bytearray(b'iello world!')
for i in range(len(b)):
    b[i] += i
print(b)  # bytearray(b'ifnos%}vzun,')

# 12. CLASS complex(real, imag = 0)
# real - число или строка, если число, представляет собой действительную часть числа. imag - только число, представляет собой мнимую часть числа, по умолчанию 0
# Класс complex() преобразует строку в комплексное число или вернет комплексное число с переданными значениями действительной и мнимой части:

print(complex())  # 0j
print(complex(3, 4))  # (3+4j)
print(complex(5))  # (5+0j)

print(complex('    5+0j'))  # (5+0j)

print(complex('.5+2e-2j   '))  # (0.5+0.02j)

print(complex('  2+2j ') + complex(' 1+2j  '))  # (3+4j)

# 13. @staticmethod и @classmethod
# @staticmethod используется для создания метода класса, который ничего не знает о классе или экземпляре класса, через который он вызван. Он просто получает переданные аргументы, без
# неявного первого аргумента(self), и его определение через наследование неизменяемо:


class ClassName:
    @staticmethod
    def method_name(arg1, arg2):
        arg1 += 1
        arg2 += 2

# Пример использования:


class MyClass():
    @staticmethod
    def staticmethod():
        print('static method called')


MyClass.staticmethod()  # static method called

my_obj = MyClass()
my_obj.staticmethod()  # static method called

# @staticmethod помогает в достижении инкапсуляции в классе, поскольку он не знает о состоянии текущего экземпляра. Кроме того, статический метод делает код намного более читабельным и
# намного более удобным для импорта


class Person():
    @staticmethod
    def is_adult(age):
        if age >= 18:
            return True
        else:
            return False


print(Person.is_adult(23))  # True

# @classmethod - это метод, который получает в качестве первого неявного аргумента класс, точно так же, как обычные методы получают в его качестве экземпляр
# Это означает, что мы можем использовать класс и все его методы внутри этого классового метода, а не конкретного экземпляра


class Class:
    @classmethod
    def method(cls, arg1, arg2):
        arg1 += 1
        arg2 += 2


class MyClass:
    @classmethod
    def classmethod(cls):
        print('class method called')


# Функцию classmethod также можно вызывать без создания экземпляра класса, но его определение следует за подклассом, а не за родительским классом, через наследование.
print(MyClass.classmethod())  # class method called

# @classmethod используется, когда нам нужно получить методы, не относящиеся к какому-то конкретному экземпляру класса, но тем не менее, каким-то образом привязанные к классу.
# Самое интересное в них то, что их можно переопределить дочерними классами.
# Поэтому, если сы хотим получить доступ к свойству класса в целом, а не к свойству конкретного экземпляра этого класса, используйте classmethod.


class MyClass():
    TOTAL_OBJECTS = 0

    def __init__(self):
        MyClass.TOTAL_OBJECTS = MyClass.TOTAL_OBJECTS + 1

    @classmethod
    def total_objects(cls):
        print('Total objects:', cls.TOTAL_OBJECTS)


# Создаем обьекты родительского класса
my_obj1 = MyClass()
my_obj2 = MyClass()
my_obj3 = MyClass()

print(MyClass.total_objects())  # Total objects: 3

# Теперь, если мы унаследуем этот класс в дочерний класс и объявим там переменную TOTAL_OBJECTS и вызовем метод класса из дочернего класса, он вернет общее количество объектов для дочернего класса.


# Создаем дочерний класс
class ChildClass(MyClass):
    TOTAL_OBJECTS = 0
    pass


ChildClass.total_objects()  # Total objects: 0

# @classmethod используется в суперклассе для определения того, как метод должен вести себя, когда он вызывается разными дочерними классами. В то время как @staticmethod используется,
# когда мы хотим вернуть одно и то же, независимо от вызываемого дочернего класса.

# 14. delattr(object, name), hasattr(object, name), gettattr(object, name, [default]) и setattr(object, name, value)

# hasattr() - функция, которая возвращает Trueб если атрибут содержится в обьекте и False в обратном случае

# delattr() - функция, удаляющая атрибут name обьекта object
class My:
    attr1 = 'yes'
    attr2 = 'no'


my = My()

print(hasattr(my, 'attr2'))  # True
delattr(my, 'attr1')
print(hasattr(my, 'attr2'))  # False

# getattr() - функция, возвращающая значение атрибута name обьекта object, default - значение, которое вернутся по умолчанию, если подано и если object не располагает атрибутом name, name - str

class My:
    attr1 = 'yes'


my = My()
print(getattr(my, 'attr1'))  # yes           то же, что и my.attr

# print(getattr(my, 'attribute2'))   AttributeError
print(getattr(my, 'attr2', 'no'))  # no

print(getattr(My, 'attr2', 'no'))  # no

# setattr() - дополнение getattr(), которое присваивает атрибуту name обьекта object значение value
class My:
    attr1 = 'yes'


my = My()

print(getattr(my, 'attr1'))  # yes
setattr(my, 'att1', 'maybe')
print(getattr(my, 'attr1'))  # maybe

print(getattr(my, 'attr2'))  # AttributeError
setattr(my, 'att2', 'hoho')
print(getattr(my, 'attr2'))  # hoho

# атрибут будет добавлен, если обьект поддерживает это действие

# 15. CLASS dict()
# Словарие - неупорядоченная коллекция произвольных обьектов с доступом по ключу. Создать словарь можно разными способами:
dict1 = {'key1': 'value1', 'key2': 'value2'}

dict2 = dict(short = 'dict', long = 'dictionary')

dict3 = dict.fromkeys([5, 25])  # dict3 = {5: None, 25: None}
dict4 = dict.fromkeys([5, 25], 125)  # dict4 = {5: 125, 25: 125}

dict5 = {a: a ** 2 for a in range(7)}  # dict5 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
# Методы словарей

# dict.clear()  # очищает словарь
# dict.copy()  # возвращает копию словаря
# classmethod dict.fromkeys(sequence, [value]) - cоздает список с ключами из последовательности sequence и значениями value, по умолчанию None
# dict.get(key, [default]) - возвращает значение ключа key, но если его нет, возвращает не ошибку, а значение default, по умолчанию None
# dict.setdefault(key, [default]) - возвращает значение ключа key, но если его нет, не возвращает ошибку, а создает ключ со значением default, по умолчанию None
# dict.items() - возвращает пары (ключ, значение), dict.keys() - ключи, dict.values() - значения
# dict.pop(key, [default]) - удаляет ключ и возвращает значение, ему соответствующее, если ключа нет, возвращает default, по умолчанию ошибка
# dict.popitem() - удаляет и возвращает пару значений ключ-значение, если словарь пусть, возвращает ошибку
# dict.update(other) - обновляет словарь, добавляя пары ключ-значение из словаря other. Одинаковые ключи перезаписываются. Возвращает None, а не обновленный словарь!!

# 16. dir([object])
# Функция dir() в Python пытается вернуть список допустимых атрибутов для данного объекта. Если аргумент не указан, он возвращает список имен в текущей локальной области.
# Если объект содержит функцию __dir __(), то эта функция будет вызвана. Функция должна возвращать список атрибутов. Список имен атрибутов отсортирован в алфавитном порядке.
# dir() with no argument: ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
# t = (1, 2), l = [1, 2],
# dir(t) with tuple argument: ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
# dir(l) with list argument: ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
# from collections import namedtuple
# n = namedtuple('Vowels', 'a,e,i,o,u')
#dir(n) with module object argument: ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '_asdict', '_fields', '_fields_defaults', '_make', '_replace', 'a', 'count', 'e', 'i', 'index', 'o', 'u']
# class Color:
#     def __dir__(self):
#         print('__dir__() function called')
#         return ['Red', 'Green', 'Blue']
# c = Color()
# dir(c) with __dir__ method defined in object: __dir__() function called
# ['Blue', 'Green', 'Red']

# 17. divmod(a, b)
# Возвращает пару частное-остаток в виде кортежа от деления аргументов
# a - делимое, b - делитель. Если аргументы являются разными типами, применяются правила двоичной арифметики
# Для целых результат аналогичен divmod(int1, int2)  --> tuple(int1 // int2, int1 % int2)
# Для чисел с плавающей запятой результат аналогичен (q, a % b), где q обычно равен math.floor(a / b), однако может быть и на единицу меньше.
# Так или иначе, q * b + a % b приближено к a, если a % b не нуль, то имеет тот же знак, что и b, и 0 <= abs(a % b) < abs(b).

print(divmod(1, 2))  # (0, 1)
print(divmod(-1, 2))  # (-1, 1)
print(divmod(-1, -2))  # (0, -1)
print(divmod(1.0, 2))  # (0.0, 1.0)

# 18. enumerate(iterable, start = 0)
# iterable - любая последовательность, итератор, или обьект, поддерживающий атрибут __next__(), start - int, начальное число счетчика
# Возвращает кортеж, содержащий пары ('счетчик','элемент') для элементов указанной последовательности
#
#
# 19. eval(expression, [globals = None, locals = None])

# 20. exec(expression, [globals = None, locals = None], /, *, [closure = None])

# 21. filter(function, iterable)

# 22. CLASS float(x = 0.0)

# 23. format(value, format_spec = '')

# 24. CLASS set([iterable]) и frozenset(iterable = set())

# 25. globals()

# 26. hash(object)

# 27. help([request])

# 28. hex(x)

# 29. id(object)

# 30. input([prompt])

# 31. CLASS int(x = 0, [base = 10])

# 32. isinstance(object, classinfo)

# 33. issubclass(class, classinfo)

# 34. len(s)

# 35. locals()

# 36. map(function, iterable, *iterables)

# 37. max(iterable, *, [default], key = None), max(arg1, arg2, *args, key = None)
#     min(iterable, *, [default], key = None), min(arg1, arg2, *args, key = None)

# 38. CLASS memoryview(object)

# 39. CLASS object

# 40. oct(x)

# 41. open(file, mode = 'r', buffering = - 1, encoding = None, errors = None, newline = None, closefd = True, opener = None)

# 42. ord(c)

# 43. pow(base, exp, mode = None)

# 44. print(*objects, sep = ' ', end = '\n', file = None, flush = False)

# 45. CLASS property(fget = None, fset = None, fdel = None, doc = None)

# 46. CLASS range([start], stop, step = 1)

# 47. repr(object)

# 48. reversed(sequence)

# 49. round(number, ndigits = None)

# 50. CLASS slice([start], stop, step = 1)

# 51. sorted(iterable, /, *, key = None, reverse = False)

# 52. CLASS str(object = '')
#           str(object = b'', encoding = 'utf-8', errors = 'strict')

# 53. sum(iterable, /, start = 0)

# 54. CLASS super([type], [object or type = None])

# 55. CLASS tuple([iterable])

# 56. CLASS type(object)
#           type(name, bases, dict, **kwds)

# 57. vars([object])

# 58. zip(*iterables, strict = False)

# 59. __import__(name, globals = None, locals = None, fromlist = (), level = 0)

# 60. lambda-function
# Лямбда функции - функции, которые задаются таким образом: lambda *args: expression. Причем выходное значение выражение у нее всегда может быть только одно. Лямбда-функция применяется зачастую когда
# нужно использовать разово функцию и вернуть ее результат, причем это удобнее делать без зараннего обозначения функции. Часто используется с такими функциями, как map, filter, reduce

double = lambda x: x * 2
print(double(5))  # 10
# Эквивалентно
def double(x):
    return x * 2
# Примеры использования лямбда-функций:
my_list = [1, 3, 4, 7, 8, 10, 11]
even_my_list = filter(lambda x: (x % 2 == 0), my_list)
print(even_my_list)  # [4, 8, 10] - Отфильтровали список по признаку делимости на 2

my_list = list('трицератопс')
doubled_my_list = list(map(lambda x: (x * 2), my_list))
print(doubled_my_list)  # ['тт', 'рр', 'ии', 'цц', 'ее', 'рр', 'аа', 'тт', 'оо', 'пп', 'сс']