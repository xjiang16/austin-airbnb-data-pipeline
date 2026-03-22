import pandas as pd

df = pd.read_csv("data/listings.csv.gz")

# Keep only selected columns
columns_to_keep = [
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
    "reviews_per_month"
]

df = df[columns_to_keep]

print(df.head())
print("\nShape:", df.shape)
print("\nMissing Values:")
print(df.isnull().sum())