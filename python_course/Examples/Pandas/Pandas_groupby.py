import pandas as pd

#example data
data = {
    'Date': ['2021-01-01', '2021-01-01', '2021-01-01', '2021-01-02', '2021-01-02'],
    'City': ['Roma', 'Milano', 'Napoli', 'Roma', 'Milano'],
    'Product': ['Mouse', 'Keyboard', 'Mouse', 'Keyboard', 'Mouse'],
    'Sale': [100, 200, 150, 300, 250]
}

df = pd.DataFrame(data)

#using groupby to aggregate data
grouped_df = df.groupby("Product").sum()

print(grouped_df)