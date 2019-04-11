# def myfunc(myarg):
#     print(myarg)
#     
# f = myfunc
# print(f)
# print(myfunc)

# f(2)

# def caller(f, arg):
#     f(arg) 

# caller(myfunc, 42)


# ---
# def deco(func):
#     def inner():
#         print('running inner()')
#     return inner
#
#
# @deco
# def target():
#     print('running target()')

# target()

# Inspection reveals that target is a now a reference to inner
# print(target)

# decorators are just syntactic sugar
# target = deco(target)

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

# print('registry ->', registry)
# [f() for f in registry]

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
