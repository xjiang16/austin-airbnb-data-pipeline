# 🏙️ Austin Airbnb Data Pipeline

## Overview
This project is an end-to-end data engineering project using Austin Airbnb listing data from Inside Airbnb. The pipeline extracts raw data, transforms and cleans it using Python (pandas), and loads it into a PostgreSQL database for analysis using SQL.

The goal is to build a simple data pipeline that:
- extracts raw Airbnb listing data
- transforms and cleans the dataset using Python and pandas
- prepares the data for loading into a relational database
- supports future SQL analysis and pipeline automation

## Dataset
Source: Inside Airbnb  
City: Austin, Texas  
File used: `listings.csv.gz`

## Configuration

Database settings are managed with environment variables in a local `.env` file.

Example:
```env
DB_USER=Gin
DB_HOST=localhost
DB_PORT=5433
DB_NAME=airbnb
```

## Tech Stack
- Python (pandas)
- PostgreSQL
- SQLAlchemy
- psycopg2
- SQL
- Git/GitHub

## Project Structure
```text
austin-airbnb-data-pipeline/
├── data/
├── scripts/
│   ├── transform_data.py
│   ├── load_to_postgres.py
│   ├── pipeline.py
├── sql/
│   └── analysis.sql
├── README.md
├── requirements.txt
├── .gitignore
```

## Pipeline Workflow

```text
Raw Data (CSV)
    ↓
Data Cleaning (Python / pandas)
    ↓
Cleaned Data (CSV)
    ↓
Staging Table (PostgreSQL)
    ↓
Upsert into Main Table
    ↓
SQL Analysis
```

## What I Built
This project currently performs the following steps:

1. Reads raw Airbnb listing data from a compressed CSV file
2. Selects 18 relevant columns for analysis
3. Cleans the dataset:
   - converts price to numeric format
   - handles missing values
   - drops rows missing key fields
4. Saves cleaned data as `cleaned_listings.csv`
5. Validates the cleaned dataset:
   - checks that the dataset is not empty
   - checks for nulls in critical columns
   - checks that listing IDs are unique
6. Loads data into a PostgreSQL staging table
7. Performs upsert (insert/update) into the main `listings` table
8. Enables SQL-based analysis on structured data
9. Reads database configuration from environment variables for flexible local setup


## How to Run the Pipeline

```bash
python scripts/pipeline.py
```

This pipeline:
1. Cleans and transforms raw Airbnb data
2. Saves the cleaned dataset
3. Loads the data into PostgreSQL  


## Incremental Loading

The pipeline uses a staging table (`listings_staging`) and PostgreSQL `ON CONFLICT` logic to simulate incremental loading.

Each run:
- loads data into a staging table
- inserts new records
- updates existing records based on primary key (`id`)

This approach avoids full table replacement and reflects real-world ETL practices.


## Data Cleaning Summary
- Raw dataset: `10,533 rows × 79 columns`
- Cleaned dataset: `10,496 rows × 18 columns`
- Converted price to numeric format
- Handled missing values and standardized schema


## Example SQL Analysis

### Total Listings
```sql
SELECT COUNT(*) FROM listings;
```

### Listings by Room Type
```sql
SELECT room_type, COUNT(*) 
FROM listings
GROUP BY room_type;
```

### Average Price by Neighborhood
```sql
SELECT neighbourhood_cleansed, AVG(price)
FROM listings
GROUP BY neighbourhood_cleansed
ORDER BY AVG(price) DESC;
```

## Key Takeaways
- Built an end-to-end ETL pipeline using Python and PostgreSQL
- Cleaned and transformed a real-world dataset
- Designed and queried a relational database using SQL
- Implemented incremental loading using staging tables and upsert logic
- Added structured logging for pipeline observability
- Added data quality checks for empty datasets, nulls, and duplicate IDs
- Externalized database configuration using environment variables

## Future Improvements
- Add scheduling (cron / Airflow)
- Add data quality validation checks
- Expand dataset (calendar, reviews)
- Build dashboard or API layer  