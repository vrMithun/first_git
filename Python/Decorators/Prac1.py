'''
1)Write a function add(a, b) that returns the sum of two numbers.
2)Assign it to a variable called my_add.
3)Pass add to a function execute(func, x, y) 
that calls the function with arguments x and y.
4)Write a function choose_operation(op) that returns 
either add or a subtract function based on the value of op (e.g., "add" or "subtract").
'''

def add(a,b):
    return (a+b)

def sub(a,b):
    return (a-b)

my_add=add

def func_arg(func,x,y):
    return func(x,y)

def choose_operation(op):
    if op.lower()=="add":
        return add
    return sub


def generator_function(n): 
    for i in range(n): 
        yield i**2
my_generator = generator_function(3) 
print(next(my_generator)) 
print(next(my_generator))

