import pandas as pd
import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Loading cleaned dataset for validation...")
df = pd.read_csv("data/cleaned_listings.csv")

# Check 1: dataset is not empty
if df.empty:
    logging.error("Validation failed: cleaned dataset is empty.")
    sys.exit(1)

# Check 2: no nulls in critical columns
critical_columns = ["id", "price", "bedrooms", "beds"]

for col in critical_columns:
    if df[col].isnull().any():
        logging.error(f"Validation failed: null values found in critical column '{col}'.")
        sys.exit(1)

# Check 3: id values are unique
if not df["id"].is_unique:
    logging.error("Validation failed: duplicate IDs found in cleaned dataset.")
    sys.exit(1)

logging.info("Data validation passed successfully.")