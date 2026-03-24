import pandas as pd
from sqlalchemy import create_engine

# Load cleaned CSV
df = pd.read_csv("data/cleaned_listings.csv")

# Connect to PostgreSQL
engine = create_engine("postgresql+psycopg2://Gin@localhost:5433/airbnb")

# Load data into the listings table
df.to_sql("listings", engine, if_exists="replace", index=False)

print("Data loaded into PostgreSQL successfully.")