import pandas as pd

file_path = "Sales.csv"

# dataset creation from file
df = pd.read_csv(file_path)
print(df)

# adding a new column with total sales
print("\n=====ADDING A COLUMN=====\n")
df["Total Sales"] = df["Quantita"] * df ["Prezzo unitario"]
print(df)

# product data grouping
print("\n=====TOTAL PRODUCT SALES=====\n")
# groupby groups the columns and selects the total sales column for each group
# reset_index displays the row index for a view similar to a dataframe
result = df.groupby("Prodotto")["Total Sales"].sum().reset_index()
print(result)

# best-selling product
print("\n=====PRODUCT WITH HIGHEST SALES=====\n")
max_sell = df.groupby("Prodotto")["Quantita"].sum()
# returns the product value corresponding to the maximum quantity value
max_sell_id = max_sell.idxmax()
max_quantity = max_sell.max()
print(max_sell_id, max_quantity)

# city with highest total sales
print("\n=====CITY WITH HIGHEST TOTAL SALES=====\n")
max_sell_city = df.groupby("Città")["Total Sales"].sum()
max_sell_id_city = max_sell_city.idxmax()
max_tot_city = max_sell_city.max()
print(max_sell_id_city, max_tot_city)

# dataframe with sales higher than a value
print("\n=====FILTERED SALES=====\n")
df_2 = df[df["Total Sales"]>5000]
print(df_2)

# sort total sales columns in descending order
print("\n=====TOTAL SALES COLUMNS IN DESCENDING ORDER=====\n")
df = df.sort_values(by="Total Sales", ascending=False)
print(df)

# view total sales for each city
print("\n=====TOTAL SALES FOR EACH CITY=====\n")
total_city_sales = df.groupby("Città")["Total Sales"].sum()
print(total_city_sales)