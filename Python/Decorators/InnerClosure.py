# inner function

def outer():
    def inner():
        print("hello")
    return inner

caller=outer()
caller()

# closure function

def func1(prefix):
    def func1(suffix):
        print(prefix+" "+suffix)
    return func1

myname=func1("Mithun")

myname("raja")