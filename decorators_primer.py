# # tining Fucnitns
#
# import functools
# import time
#
#
# def timer(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         start_time = time.perf_counter()
#         value = func(*args, **kwargs)
#         end_time = time.perf_counter()
#         run_time = end_time - start_time
#         print(f"Runtime for {func.__name__} is {run_time:.4f} sec")
#         return value
#
#     return wrapper
#
#
# @timer
# def waste_some_time(num_times):
#     for _ in range(num_times):
#         sum([i**2 for i in range(10000)])
#
# waste_some_time(5)
import functools


# import random
# PLUGINS = dict()
#
# def register(func):
#     """Register a function as a plug-in"""
#     PLUGINS[func.__name__] = func
#     return func
#
# @register
# def say_hello(name):
#     return f"Hello {name}"
#
# @register
# def be_awesome(name):
#     return f"Yo {name}, together we are the awesomest!"
#
# def randomly_greet(name):
#     greeter, greeter_func = random.choice(list(PLUGINS.items()))
#     print(f"Using {greeter!r}")
#     return greeter_func(name)


# def repeat(num_times):
#     def decorator_repeat(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for _ in range(num_times):
#                 func(*args, **kwargs)
#
#         return wrapper
#
#     return decorator_repeat
#
#
# @repeat(num_times=4)
# def greet(name):
#     print(f"Hello {name}")
#
#
# greet("BOb")


#Classes as Decorators
class Counter:
    def __init__(self,start=0):
        self.count = start

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"{self.count}")


counter = Counter()
