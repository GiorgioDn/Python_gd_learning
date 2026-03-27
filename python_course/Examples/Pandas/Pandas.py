import pandas as pd
import numpy as np

#csv file path
file_path = "Sales.csv"

#loading data into dataframe
df = pd.read_csv(file_path)

#first rows of the dataframe to confirm
print(df.head())

#example DataFrame, including missing values and duplicates
data = {
    'Nome': ['Alice', 'Bob', 'Carla', 'Bob', 'Carla', 'Alice', None],
    'Età': [25, 30, 22, 30, np.nan, 25, 29],
    'Città': ['Roma', 'Milano', 'Napoli', 'Milano', 'Napoli', 'Roma', 'Roma']
}

df = pd.DataFrame(data)

#printing original DataFrame
print("Original DataFrame:")
print(df)

#selecting rows where age is over 23, creating a copy of the dataframe
df_older = df[df['Età'] > 23]

#printing selected rows
print("\nPeople older than 23 years:")
print(df_older)

#adding a new column for adult (over 18)
df['Maggiorenne'] = df['Età'] >= 18

#printing DataFrame with 'Maggiorenne' column
print("\nDataFrame with 'Maggiorenne' column:")
print(df)

#removing duplicates
df = df.drop_duplicates()

#handling missing data
#removing rows where at least one element is missing
df_cleaned = df.dropna()

#we can replace missing data with a default value
#inplace modifies the dataset if set to True, it's better to set it to False first to see how data is modified
df['Età'].fillna(df['Età'].mean(), inplace=True)

#printing cleaned DataFrame

print("\nDataFrame after cleaning:")
print(df_cleaned)

#printing DataFrame with replaced missing data
print("\nDataFrame with replaced missing data:")
print(df)

#adding a new column for adult (over 18)
df['Maggiorenne'] = df['Età'] >= 18

#printing DataFrame with 'Maggiorenne' column after replacement
print("\nDataFrame with 'Maggiorenne' column after replacement:")
print(df)

#printing original DataFrame
print("Original DataFrame:")
print(df)