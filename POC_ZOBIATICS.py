# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 07:42:45 2023

@author: personal
"""

import pandas as pd

file_path = 'C:/Users/personal/Desktop/Personal/customers.csv'  
customers_data = pd.read_csv(file_path)

file_path1 = 'C:/Users/personal/Desktop/Personal/products.csv'  
products_data = pd.read_csv(file_path1)

file_path2 = 'C:/Users/personal/Desktop/Personal/purchases.csv'  
purchases_data = pd.read_csv(file_path2)

# Display the first few rows of the DataFrame
print(customers_data.head())

print(products_data.head())

print(purchases_data.head())

# Display basic statistics about numerical columns using describe()
customers_data.describe()

products_data.describe()

purchases_data.describe()

# Display summary information using the .info() method
customers_data.info() 

products_data.info()

purchases_data.info()





