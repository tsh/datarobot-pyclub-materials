# class LineItem:
#     def __init__(self, description, weight, price):
#         self.description = description
#         self.weight = weight
#         self.price = price
#
#     def subtotal(self):
#         return self.weight * self.price


# raisins = LineItem('Golden raisins', 10, 6.99)
# print(raisins.subtotal())
#
# raisins.weight = -20
# print(raisins.subtotal())


# --- Property ---

# class LineItem:
#     def __init__(self, description, weight, price):
#         self.description = description
#         self.weight = weight
#         self.price = price
#
#     def subtotal(self):
#         return self.weight * self.price
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, value):
#         if value > 0:
#             self.__weight = value
#         else:
#             raise ValueError('weight must be greater than 0')
#
# walnuts = LineItem('walnuts', 0, 10.00)
# print(walnuts.subtotal())



# --- Old style property ---

# class LineItem:
#     def __init__(self, description, weight, price):
#         self.description = description
#         self.weight = weight
#         self.price = price
#
#     def subtotal(self):
#         return self.weight * self.price
#
#     def get_weight(self):
#         return self.__weight
#     def set_weight(self, value):
#
#         if value > 0:
#             self.__weight = value
#         else:
#             raise ValueError('value must be > 0')
#
#     weight = property(get_weight, set_weight)
#
# walnuts = LineItem('walnuts', 0, 10.00)
# print(walnuts.subtotal())


# --- Descriptors ---

"""A descriptor is a class that implements a protocol consisting of the __get__ , __set__ ,
and __delete__ methods. If any of those methods are defined for an object, it is said to be a descriptor"""


# class MyDescriptor():
#     def __init__(self, initial_value=None):
#         self.value = initial_value
#
#     def __get__(self, obj, objtype):
#         print('[DESCRIPTOR] Getting value')
#         return self.value
#
#     def __set__(self, obj, value):
#         print('[DESCRIPTOR] Setting value ', value)
#         self.value = value
#
#
# class MyClass():
#     desc = MyDescriptor()
#     normal = 10
#
#
# c = MyClass()
# print('Descriptor:', c.desc)
# print('Normal value: ', c.normal)
# c.desc = 100
# print('Descriptor after modification: ', c.desc)

# --- Task #1 ---
# Implement descriptor that doesnt allow setting negative values. Use it on LineItem class

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

# --- Solution #1 ---

# class Quantity:
#     def __get__(self, obj, obj_type):
#         return self.value
#
#     def __set__(self, instance, value):
#         if value > 0:
#             self.value = value
#         else:
#             raise ValueError('value must be > 0')
#
#
# class LineItem:
#     weight = Quantity()
#     price = Quantity()
#
#     def __init__(self, description, weight, price):
#         self.description = description
#         self.weight = weight
#         self.price = price
#
#     def subtotal(self):
#         return self.weight * self.price
#
# truffle = LineItem('White truffle', 100, 1)
# print (truffle.weight)


# --- Problems with settings values on a Descriptor?? ---

# truffle = LineItem('White truffle', weight=10, price=120)
# truffle2 = LineItem('Black truffle', weight=20, price=250)
# print ('Truffle1 price: ', truffle.price)
# print ('Truffle2 price: ', truffle2.price)


# --- Descriptor with weakref dict ---

# from weakref import WeakKeyDictionary
# # https://docs.python.org/3/library/weakref.html#weakref.WeakKeyDictionary
#
# class MyDescriptor:
#     def __init__(self, default=None):
#         self.values = WeakKeyDictionary()
#         self.default = default
#
#     def __get__(self, obj, objtype):
#         print('[DESCRIPTOR] Getting value of object {} and type {}: '.format(obj, objtype))
#         return self.values.get(obj, self.default)
#
#     def __set__(self, obj, value):
#         print('[DESCRIPTOR] Setting value {} on object {}'.format(value, obj))
#         self.values[obj] = value
#
#     def __delete__(self, obj):
#         print('del is called')
#         try:
#             del self.values[obj]
#         except KeyError:
#             pass
#
# class MyClass():
#     desc = MyDescriptor()
#
#
# var1 = MyClass()
# var2 = MyClass()
# var1.desc = 100
# var2.desc = -999
#
# print(var1.desc)
# print (var2.desc)

# del var1.desc
