import pandas as pd
import numpy as np

products = [ "Computer", "Laptop", "Tablet"]
cities = [ "Bologna", "Turin", "Rome"]

size_data = 21

# random dataframe creation
df = pd.DataFrame({
    "Product": np.random.choice(products, size_data),
    "Data": np.random.randint(1, 31, size_data),
    "City": np.random.choice(cities, size_data),
    "Sales": np.random.randint(0, 11, size_data),
})

print("\n=====INITIAL TABLE=====\n")
print(df)

# pivot table for average sales
print("\n=====AVERAGE SALES PIVOT=====\n")
pivot_df = df.pivot_table(values='Sales', index='Product', columns='City', aggfunc='mean', fill_value=0).reset_index()
print(pivot_df)

# groupby table for total sales
print("\n=====TOTAL SALES GROUPBY=====\n")
total_sales = df.groupby("Product")["Sales"].sum().reset_index()
print(f"{total_sales}\n")