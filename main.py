import time
current_time = time.time()
print(f"Current time : {current_time}\n")

def speed_calc_decorator(function):
    def wrapper_function():
      before_time = time.time()
      function()
      after_time = time.time()
      print(f"{function.__name__} run speed: {after_time - before_time}")
    return wrapper_function

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()