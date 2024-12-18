def fun(s,length):
    if length==0:
        return s[0]
    return s[length]+fun(s,length-1)
print(fun("hello",4))
def fun(s, length=None):
    # Set length to the last index if it's not provided
    if length is None:
        length = len(s) - 1
    # Base case: when length reaches 0
    if length == 0:
        return s[0]
    # Recursive case: build the reversed string
    return s[length] + fun(s, length - 1)

# Now you can call the function with just the string
print(fun("hello"))
