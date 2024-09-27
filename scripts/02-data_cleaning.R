#### Preamble ####
# Purpose: Cleans the raw ferry ticket data downloaded from Open Data Toronto
# Author: Denise Chang
# Date: 21 September 2024
# Contact: dede.chang@mail.utoronto.ca
# License: MIT
# Pre-requisites: 01-download_data.R

#### Workspace setup ####
library(tidyverse)
library(arrow)
library(janitor)

#### Clean data ####

# read in the raw data
raw_ferry_data <-
  read_parquet(file = "inputs/data/raw_ticket_data.parquet",)

clean_ferry_data <-
  # make the columns readable
  clean_names(raw_ferry_data) |>
  # select columns of interest
  select(timestamp, redemption_count, sales_count) |>
  # keeps year and month timestamp
  mutate(timestamp = as_date(ymd_hms(timestamp))) |>
  # keep data from 2022 to 2023 inclusively
  filter(timestamp <= as.Date("2023-12-31") &
           timestamp >= as.Date("2022-01-01")) |>
  # combine redemption_count and sales_count based on new timestamp
  group_by(timestamp) |>
  summarise(
    total_redemption_count = sum(redemption_count, na.rm = TRUE),
    total_sales_count = sum(sales_count, na.rm = TRUE)
  ) |>
  # rename column headings for better readability
  rename(date = timestamp,
         tickets_redeemed = total_redemption_count,
         tickets_sold = total_sales_count)

#### Save Data ####
write_parquet(x = clean_ferry_data,
              sink = "outputs/data/clean_ferry_data.parquet")