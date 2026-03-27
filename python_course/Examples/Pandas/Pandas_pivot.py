import pandas as pd

#example data
data = {
    'Date': ['2021-01-01', '2021-01-01', '2021-01-01', '2021-01-02', '2021-01-02'],
    'City': ['Roma', 'Milano', 'Napoli', 'Roma', 'Milano'],
    'Product': ['Mouse', 'Keyboard', 'Mouse', 'Keyboard', 'Mouse'],
    'Sale': [100, 200, 150, 300, 250]
}

df = pd.DataFrame(data)

#pivot
#creating the pivot table
#applies the function to values, organizing data so each row represents the index and each column reports the data corresponding to columns
pivot_df = df.pivot_table(values='Sale', index='Product', columns='City', aggfunc='mean')

print(pivot_df)