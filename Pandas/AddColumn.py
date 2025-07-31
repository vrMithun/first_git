import pandas as pd
'''
Add a new column named "Total Value" to the DataFrame,
which should be the product of Price and Quantity for each row.
'''
data = {
    'Product': ['Laptop', 'Tablet', 'Smartphone', 'Monitor', 'Keyboard'],
    'Price': [1200, 300, 800, 150, 100],
    'Quantity': [5, 10, 8, 3, 15]
}

mycol={"Total_Value":[i*j for i,j in zip(data['Price'],data['Quantity'])]}
df1 = pd.DataFrame(data)

df2=pd.DataFrame(mycol)

df=pd.concat([df1,df2],axis=1)
print(df.head())