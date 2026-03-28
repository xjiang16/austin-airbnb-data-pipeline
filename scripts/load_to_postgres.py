import pandas as pd
from sqlalchemy import create_engine
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Loading cleaned CSV...")

# Load cleaned CSV
df = pd.read_csv("data/cleaned_listings.csv")

logging.info(f"Loaded {len(df)} rows")

# Connect to PostgreSQL
engine = create_engine("postgresql+psycopg2://Gin@localhost:5433/airbnb")

logging.info("Writing data to PostgreSQL...")

# Load data into the listings table
df.to_sql("listings", engine, if_exists="replace", index=False)

print("Data loaded into PostgreSQL successfully.")