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
## Tools Used
- Python
- pandas
- PostgreSQL
- SQLAlchemy
- psycopg2
- SQL
- Git/GitHub
- PyCharm

## Pipeline Workflow

```text
Raw Data (CSV)
    ↓
Data Cleaning (Python / pandas)
    ↓
Cleaned Data (CSV)
    ↓
Load to PostgreSQL
    ↓
SQL Analysis
```

## What I Built
This project currently performs the following steps:

1. Reads raw Airbnb listing data from a compressed CSV file
2. Explores the dataset to understand columns and structure
3. Selects 18 relevant columns for analysis
4. Cleans the data by:
    - converting price to numeric format
    - handling missing values
    - dropping rows missing key fields
5. Saves the cleaned dataset as `cleaned_listings.csv`
6. Loads the cleaned data into a PostgreSQL database
7. Runs SQL queries to analyze listing counts, room types, review patterns, and neighborhood pricing

## How to Run the Pipeline

```bash
python scripts/pipeline.py
```

This pipeline:
1. Cleans and transforms raw Airbnb data
2. Saves the cleaned dataset
3. Loads the data into PostgreSQL  

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

## Key Learning Outcomes
Through this project, I practiced:
- working with real-world raw data
- cleaning and transforming data with pandas
- designing a PostgreSQL table schema
- loading data from Python into PostgreSQL
- writing SQL queries for analysis

## Future Improvements
- Add scheduling (cron / Airflow)
- Implement incremental loading (instead of full replace)
- Add logging and monitoring
- Expand dataset (calendar, reviews)  