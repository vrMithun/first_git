from functools import wraps

def my_decorator(func):
    @wraps(func)  # Preserve metadata of the original function
    def wrapper(*args, **kwargs):
        print("Before the function call.")
        result = func(*args, **kwargs)
        print("After the function call.")
        return result
    return wrapper

@my_decorator
def greet(name):
    """Greet someone by name."""
    return f"Hello, {name}!"

print(greet("Alice"))
print(greet.__name__)  # Output: greet
print(greet.__doc__)   # Output: Greet someone by name.