# 🏙️ Austin Airbnb Data Pipeline

## Overview
This project is an end-to-end data engineering project using Austin Airbnb listing data from Inside Airbnb.

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
├── sql/
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

## Data Cleaning Summary
- Raw dataset shape: `10,533 rows x 79 columns`
- Cleaned dataset shape: `10,496 rows x 18 columns`

## Example SQL Questions Answered
- How many listings are in the dataset?
- Which neighborhoods have the highest average prices?
- What are the most reviewed listings?
- What is the average rating and average reviews per month?
- How many listings are entire homes vs private rooms?

## Key Learning Outcomes
Through this project, I practiced:
- working with real-world raw data
- cleaning and transforming data with pandas
- designing a PostgreSQL table schema
- loading data from Python into PostgreSQL
- writing SQL queries for analysis

## Next Steps
- automate the transform + load process with a pipeline script
- improve the SQL analysis section
- potentially expand the project with calendar or reviews data