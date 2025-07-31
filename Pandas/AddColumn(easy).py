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

df = pd.DataFrame(data)
df['Total_Value'] = df['Price'] * df['Quantity']
print(df.head())
