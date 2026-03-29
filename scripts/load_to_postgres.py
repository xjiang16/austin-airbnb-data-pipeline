import pandas as pd
from sqlalchemy import create_engine, text
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

# Step 1: load into staging table
logging.info("Loading data into staging table...")
df.to_sql("listings_staging", engine, if_exists="replace", index=False)

with engine.connect() as conn:

    logging.info("Upserting into main listings table...")

    # Create main table if not exists
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS listings AS
        SELECT * FROM listings_staging WHERE 1=0;
    """))

    # Add primary key if not exists
    conn.execute(text("""
        DO $$
        BEGIN
            IF NOT EXISTS (
                SELECT 1
                FROM pg_constraint
                WHERE conname = 'listings_pkey'
            ) THEN
                ALTER TABLE listings ADD PRIMARY KEY (id);
            END IF;
        END
        $$;
    """))

    # UPSERT logic
    conn.execute(text("""
        INSERT INTO listings
        SELECT * FROM listings_staging
        ON CONFLICT (id)
        DO UPDATE SET
            name = EXCLUDED.name,
            host_id = EXCLUDED.host_id,
            host_name = EXCLUDED.host_name,
            neighbourhood_cleansed = EXCLUDED.neighbourhood_cleansed,
            latitude = EXCLUDED.latitude,
            longitude = EXCLUDED.longitude,
            property_type = EXCLUDED.property_type,
            room_type = EXCLUDED.room_type,
            accommodates = EXCLUDED.accommodates,
            bedrooms = EXCLUDED.bedrooms,
            beds = EXCLUDED.beds,
            price = EXCLUDED.price,
            minimum_nights = EXCLUDED.minimum_nights,
            availability_365 = EXCLUDED.availability_365,
            number_of_reviews = EXCLUDED.number_of_reviews,
            review_scores_rating = EXCLUDED.review_scores_rating,
            reviews_per_month = EXCLUDED.reviews_per_month;
    """))

logging.info("Data successfully upserted into PostgreSQL.")

