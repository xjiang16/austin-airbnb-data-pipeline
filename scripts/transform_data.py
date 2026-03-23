import pandas as pd

df = pd.read_csv("data/listings.csv.gz")

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
df["price"] = df["price"].replace("[$,]", "", regex=True).astype(float)

# Drop rows missing key fields
df = df.dropna(subset=["price", "bedrooms", "beds"])

# Fill review-related missing values with 0
df["review_scores_rating"] = df["review_scores_rating"].fillna(0)
df["reviews_per_month"] = df["reviews_per_month"].fillna(0)

# Fill host_name missing values with Unknown
df["host_name"] = df["host_name"].fillna("Unknown")

print(df.head())
print("\nShape:", df.shape)
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Save cleaned file
df.to_csv("data/cleaned_listings.csv", index=False)
print("\nCleaned data saved to data/cleaned_listings.csv")