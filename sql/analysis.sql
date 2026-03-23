-- 1. Total listings
SELECT COUNT(*) AS total_listings
FROM listings;

-- 2. Average price by neighborhood
SELECT neighbourhood_cleansed, ROUND(AVG(price)::numeric, 2) AS avg_price
FROM listings
GROUP BY neighbourhood_cleansed
ORDER BY avg_price DESC
LIMIT 10;

-- 3. Top 10 most reviewed listings
SELECT name, number_of_reviews, price
FROM listings
ORDER BY number_of_reviews DESC
LIMIT 10;

-- 4. Average rating and reviews per month
SELECT
    ROUND(AVG(review_scores_rating)::numeric, 2) AS avg_rating,
    ROUND(AVG(reviews_per_month)::numeric, 2) AS avg_reviews_per_month
FROM listings;

-- 5. Listings by room type
SELECT room_type, COUNT(*) AS listing_count
FROM listings
GROUP BY room_type
ORDER BY listing_count DESC
