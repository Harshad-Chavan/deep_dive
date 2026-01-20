
def add_func(time_sleep=0):
    def outer_wrapper(func):
        def wrapper(*args, **kwargs):
            print("Before calling the function : sleeping for", time_sleep, "seconds")
            result = func(*args, **kwargs)
            print("After calling the function")
            return result
        return wrapper
    return outer_wrapper


# add_func(time_sleep)(read_out_message)(message)
# outer_wrapper(read_out_message)(message)
# wrapper(message)
@add_func(time_sleep=2)
def read_out_message(message):
    print(f"Message:{message.upper()}")


read_out_message("Hello")

