import pandas as pd

df = pd.read_csv("data/listings.csv.gz")

print(df.head())
print("\nShape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())