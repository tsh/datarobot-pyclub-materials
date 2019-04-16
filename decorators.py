
# def myfunc(myarg):
#     print(myarg)

# f = myfunc
# print(f)
# print(myfunc)

# f(2)

# def caller(f, arg):
#     f(arg)

# caller(f, 42)


# ---
# def deco(func):
#     print('running deco')
#     def inner():
#         print('running inner()')
#     return inner

#
#
# @deco
# def target():
#     print('running target()')

# decorated = deco(target)

# Inspection reveals that target is a now a reference to inner
# print(target())

# target()

# decorators are just syntactic sugar

# ---
# Decorators run at import time (when module loaded by python)

# registry = []
#
# def register(func):
#     print('registered: (%s)' % func)
#     registry.append(func)
#     return func
#
# @register
# def f1():
#     print('running f1()')
#
# @register
# def f2():
#     print('running f2()')
#
# def f3():
#     print('running f3()')
#
# print('registry ->', registry)
# print([f() for f in registry])

# --- proper decorator

# import time
#
# def timed(func):
#     def inner(*args):
#         t0 = time.perf_counter()
#         # https://docs.python.org/3/library/string.html#format-specification-mini-language
#         result = func(*args)  # call function
#         print('time elapsed: {:5f}s'.format(time.perf_counter() - t0))
#         return result
#     return inner
#
# @timed
# def sum_to_number(number):
#     return sum([n for n in range(number)])
#
# print(sum_to_number(100))


# ---
# higher order function
# write func that accepts 1 integer arguments and returns same arguments multiplied by 2
# use map for example, substitute with lambda
# write func that accepts one argument, and return True if the argument is even. Apply this with `filter` function to array.

# def decorator_with_arguments(myarg):
#     def wrap(f):
#         print ("Inside wrap()")
#         def inner(*args):
#             print ("Inside wrapped_f(), decorator argument: ", myarg)
#             f(*args)
#             print ("After f(*args)")
#         return inner
#     return wrap
#
# @decorator_with_arguments(42)
# def say_number(a1, a2, a3, a4):
#     print ("say_number arguments: ", a1, a2, a3, a4)
#
# say_number(1,2,3,4)
