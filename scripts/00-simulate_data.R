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
library(tidyverse)

#### Start simulation ####

## Create simulated data

set.seed(304) #random seed

# simulate data for 1 year (365 days)
sim_data <-
  tibble(
    date = rep(x = as.Date("2023-01-01") + c(0:364), times = 1),
    redemption_count = sample(x = 0: 2000,
                             size = 365,
                             replace = TRUE),
    sales_count = sample(x = 0:2000,
                 size = 365,
                 replace = TRUE))


#### Data testing ####

# check that redemption_count is greater or equal to 0
all(sim_data$redemption_count >= 0)

# check that sales_count is greater or equal to 0
all(sim_data$sales_count >= 0)

# check the date range
sim_data$date |>
  min() == "2023-01-01"

sim_data$date |>
  max() == "2023-12-31"