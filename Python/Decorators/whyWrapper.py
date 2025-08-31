from functools import wraps

# Decorator WITH @wraps
def log_args(func):
    @wraps(func)  # Preserve metadata
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper

# Decorator WITHOUT @wraps
def bad_log_args(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_args
def add(a, b, c=0):
    """Add three numbers."""
    return a + b + c

@bad_log_args
def multiply(a, b, c=1):
    """Multiply three numbers."""
    return a * b * c

# Test with @wraps
print(add(1, 2, c=3))      # Output: Calling add with args=(1, 2), kwargs={'c': 3}
                            #         6
print(add.__name__)         # Output: add
print(add.__doc__)          # Output: Add three numbers.

# Test without @wraps
print(multiply(2, 3, c=4))  # Output: Calling multiply with args=(2, 3), kwargs={'c': 4}
                            #         24
print(multiply.__name__)    # Output: wrapper
print(multiply.__doc__)     # Output: None