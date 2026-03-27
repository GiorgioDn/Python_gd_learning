import pandas as pd
import numpy as np

file_path = "python_course/Exercises/Pandas/dataset/work.csv"

# dataset creation from file
df = pd.read_csv(file_path)
print("\n=====INITIAL TABLE=====\n")
print(df)

# numeric column filter
numbers = df.select_dtypes(include=["float64", "int64"])
print(numbers)

# describe: descriptive statistics
print("\n=====TABLE DESCRIBE=====\n")
desc = df.describe()
print(desc)

# info: DataFrame summary
print("\n=====TABLE INFO=====\n")
desc = df.info()
print(desc)

# value count: number of occurrences per row
print("\n=====TABLE VALUE COUNTS=====\n")
val_count = df.value_counts()
print(val_count)

# removal or replacement
print("\n=====CORRECTION OF ANOMALIES AND NULL VALUES=====\n")
for col in numbers.columns:
    median = df[col].median()
    if col == "ID_Cliente":
        rand_id = np.random.randint(10000000, 99999999)
        df[col] = df[col].fillna(rand_id)
    elif col == "Età":
        df.loc[(df[col] < 0) | (df[col] > 100), "Età"] = np.nan
        df[col] = df[col].fillna(median)
    elif col == "Durata_Abbonamento":
        df.loc[df["Durata_Abbonamento"] < 0, "Durata_Abbonamento"] = 0
        df[col] = df[col].fillna(0)
    elif col == "Dati consumati":
        df.loc[df[col] <= 0, "Dati_Consumati"] = np.nan
        df[col] = df[col].fillna(median)
    else: 
        df[col].dropna()

df = df.dropna(subset=["Churn"])
    
print(df)

# cost per GB creation 
print("\n=====COST PER GB COLUMN=====\n")
df["Costo_Per_GB"] = df["Tariffa_Mensile"] / df["Dati_Consumati"]
print(df)

# churn conversion to numeric
print("\n=====CHURN CONVERSION TO NUMERIC=====\n")
df["Churn"] = df["Churn"].replace({"Sì": 1, "No": 0})
print(df)

# groupby relationship
print("\n=====RELATION AGE, SUBSCRIPTION DURATION, MONTHLY RATE, CHURN=====\n")
relation = df.groupby(["Età", "Durata_Abbonamento", "Tariffa_Mensile"])["Churn"].mean()
print(relation)

# correlations between variables corr()
print("\n=====CORRELATION BETWEEN VARIABLES=====\n")
corr = numbers.corr()
print(corr)

# normalization
print("\n=====NORMALIZATION=====\n")
df[numbers.columns] = (numbers - numbers.mean()) / numbers.std()
print(df)