def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"{func.__name__} has been called {wrapper.calls} times")
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper 
@count_calls
def introduce(name):
    print(f"Hello, {name}!")
introduce("Pranay")
introduce("Mahanthi")
introduce("Madhu")
