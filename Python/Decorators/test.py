def my_function(): 
    try: result = 10 / 0 
    except ZeroDivisionError: return "Division by zero" 
    finally: return "Finally block"
#print(my_function()) 


import numpy as np

myarr=np.array([])
print(myarr[-1])