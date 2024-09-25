#### Preamble ####
# Purpose: Tests the cleaned data of Ferry ticket sales for Toronto Islands
# Author: Denise Chang
# Date: 24 September 2024
# Contact: dede.chang@mail.utoronto.ca
# License: MIT
# Pre-requisites: 01-download_data.R and 02-data_cleaning.R

#### Workspace setup ####
library(tidyverse)
library(arrow)

#### Test Data ####

# read the cleaned data
clean_ferry_data <-
  read_parquet(file = "outputs/data/clean_ferry_data.parquet")

# check that the number of redeemed tickets is greater or equal to 0
all(clean_ferry_data$tickets_redeemed >= 0)

# check that the number of sold tickets is greater or equal to 0
all(clean_ferry_data$tickets_sold >= 0)

# check the date range
clean_ferry_data$date |>
  min() == "2022-01-01"

clean_ferry_data$date |>
  max() == "2023-12-31"

# check that every entry in the date column is unique
n_distinct(unique(clean_ferry_data$date)) == nrow(clean_ferry_data)

# check that every date in range is represented in the dataset
n_distinct(unique(clean_ferry_data$date)) == 365*2


