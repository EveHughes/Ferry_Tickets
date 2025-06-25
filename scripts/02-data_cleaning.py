#### Preamble ####
# Purpose: Cleans the raw ferry ticket data downloaded from Open Data Toronto
# Author: Denise Chang
# Date: 21 September 2024
# Contact: dede.chang@mail.utoronto.ca
# License: MIT
# Pre-requisites: 01-download_data.py

#### Workspace setup ####
import pandas as pd
import numpy as np

#### Clean data ####

# read in the raw data
raw_ferry_data = pd.read_csv("inputs/data/raw_ticket_data.csv")

# make the columns readable
raw_ferry_data = raw_ferry_data.rename(columns=lambda x: x.lower().replace(" ", "_"))

# convert timestamp to datetime.date
raw_ferry_data["timestamp"] = pd.to_datetime(raw_ferry_data["timestamp"]).dt.date

# select columns and filter by date
clean_ferry_data = (
    raw_ferry_data.loc[
        (raw_ferry_data["timestamp"] >= pd.to_datetime("2022-01-01").date()) &
        (raw_ferry_data["timestamp"] <= pd.to_datetime("2023-12-31").date()),
        ["timestamp", "redemption_count", "sales_count"]
    ]
    .groupby("timestamp", as_index=False)
    .agg(
        total_redemption_count=("redemption_count", "sum"),
        total_sales_count=("sales_count", "sum")
    )
    .rename(
        columns={
            "timestamp": "date",
            "total_redemption_count": "tickets_redeemed",
            "total_sales_count": "tickets_sold"
        }
    )
)

#### Save Data ####
clean_ferry_data.to_csv("outputs/data/clean_ferry_data.csv", index=False)
