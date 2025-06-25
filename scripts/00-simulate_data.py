#### Preamble ####
# Purpose: Simulate dataset of Ferry ticket sales for Toronto Islands
# Author: Denise Chang
# Data: 21 September 2024
# Contact: dede.chang@mail.utoronto.ca
# License: MIT
# Pre-requisites: None

#### Data Expectations ####
# 'date' should be a valid date in YYYY-MM-DD format
# 'redemption_count' should be an integer grater or equal to 0
# 'sales_count' should be an integer grater or equal to 0
# Columns: date, redemption_count, sales_count

#### Workspace setup ####
import pandas as pd
import numpy as np

#### Start simulation ####

## Create simulated data

np.random.seed(304)  # random seed

# simulate data for 1 year (365 days)
sim_data = pd.DataFrame({
    "date": pd.date_range(start="2023-01-01", periods=365, freq='D'),
    "redemption_count": np.random.randint(0, 2001, size=365),
    "sales_count": np.random.randint(0, 2001, size=365)
})

#### Data testing ####

# check that redemption_count is greater or equal to 0
print((sim_data["redemption_count"] >= 0).all())

# check that sales_count is greater or equal to 0
print((sim_data["sales_count"] >= 0).all())

# check the date range
print(sim_data["date"].min() == pd.to_datetime("2023-01-01"))

print(sim_data["date"].max() == pd.to_datetime("2023-12-31"))
