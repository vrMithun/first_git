def greet(name):
    return f"Hello, {name}!"

# Assign function to a variable
my_func = greet
print(my_func("Alice"))  # Output: Hello, Alice!

# Pass function as an argument
def call_function(func, arg):
    return func(arg)

print(call_function(greet, "Bob"))  # Output: Hello, Bob!

# Return a function from another function
def get_greeter():
    return greet

new_func = get_greeter()
print(new_func("Charlie"))  # Output: Hello, Charlie!