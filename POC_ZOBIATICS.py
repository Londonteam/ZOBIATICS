# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 07:42:45 2023

@author: personal
"""

import pandas as pd

file_path = 'C:/Users/personal/Desktop/Personal/customers.csv'  
df = pd.read_csv(file_path)

file_path1 = 'C:/Users/personal/Desktop/Personal/products.csv'  
df1 = pd.read_csv(file_path1)

file_path2 = 'C:/Users/personal/Desktop/Personal/purchases.csv'  
df2 = pd.read_csv(file_path2)

# Display the first few rows of the DataFrame
print(df.head())

print(df1.head())

print(df2.head())