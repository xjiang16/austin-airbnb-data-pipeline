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
```
## Progress So Far
* Set up project folder structure 
* Connected project to GitHub 
* Explored raw Airbnb listings data 
* Selected 18 useful columns for analysis 
* Cleaned missing values 
* Saved a cleaned dataset for the next pipeline stage

## Tools Used
* Python
* pandas
* GitHub
* PyCharm

## Next Steps
* install PostgreSQL
* load cleaned data into a database
* write SQL analysis queries
* automate the pipeline