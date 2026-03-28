import pandas as pd
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Reading raw Airbnb listings data...")

df = pd.read_csv("data/listings.csv.gz")

logging.info("Selecting relevant columns...")
# Keep only useful columns
df = df[
    [
        "id",
        "name",
        "host_id",
        "host_name",
        "neighbourhood_cleansed",
        "latitude",
        "longitude",
        "property_type",
        "room_type",
        "accommodates",
        "bedrooms",
        "beds",
        "price",
        "minimum_nights",
        "availability_365",
        "number_of_reviews",
        "review_scores_rating",
        "reviews_per_month",
    ]
]

# Clean price: remove $ and commas, then convert to float
logging.info("Cleaning price column...")
df["price"] = df["price"].replace("[$,]", "", regex=True).astype(float)

# Drop rows missing key fields
logging.info("Dropping rows missing key fields...")
df = df.dropna(subset=["price", "bedrooms", "beds"])

# Fill review-related missing values with 0
logging.info("Filling missing review values with 0...")
df["review_scores_rating"] = df["review_scores_rating"].fillna(0)
df["reviews_per_month"] = df["reviews_per_month"].fillna(0)

# Fill host_name missing values with Unknown
logging.info("Filling missing host names...")
df["host_name"] = df["host_name"].fillna("Unknown")

logging.info(f"Final shape: {df.shape}")
logging.info("Missing values after cleaning:")
logging.info(f"\n{df.isnull().sum()}")

# Save cleaned file
logging.info("Saving cleaned dataset to data/cleaned_listings.csv...")
df.to_csv("data/cleaned_listings.csv", index=False)

logging.info("Transformation completed successfully.")