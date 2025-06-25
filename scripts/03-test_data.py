#### Preamble ####
# Purpose: Tests the cleaned data of Ferry ticket sales for Toronto Islands
# Author: Denise Chang
# Date: 24 September 2024
# Contact: dede.chang@mail.utoronto.ca
# License: MIT
# Pre-requisites: 01-download_data.py and 02-data_cleaning.py

#### Workspace setup ####
import pandas as pd

#### Test Data ####

# read the cleaned data
clean_ferry_data = pd.read_csv("outputs/data/clean_ferry_data.csv")

# check that the number of redeemed tickets is greater or equal to 0
print((clean_ferry_data["tickets_redeemed"] >= 0).all())

# check that the number of sold tickets is greater or equal to 0
print((clean_ferry_data["tickets_sold"] >= 0).all())

# check the date range
clean_ferry_data["date"] = pd.to_datetime(clean_ferry_data["date"])

print(clean_ferry_data["date"].min() == pd.to_datetime("2022-01-01"))
print(clean_ferry_data["date"].max() == pd.to_datetime("2023-12-31"))

# check that every entry in the date column is unique
print(clean_ferry_data["date"].nunique() == len(clean_ferry_data))

# check that every date in range is represented in the dataset
print(clean_ferry_data["date"].nunique() == 365 * 2)
