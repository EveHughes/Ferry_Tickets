#### Preamble ####
# Purpose: Download and save data from https://open.toronto.ca/dataset/toronto-island-ferry-ticket-counts/
# Author: Denise Chang
# Date: 21 September 2024
# Contact: dede.chang@mail.utoronto.ca
# License: MIT
# Pre-requisites: None

#### Workspace setup #### 
library(tidyverse)
library(opendatatoronto)
library(arrow)

#### Download data ####
raw_ticket_data <-
  list_package_resources("toronto-island-ferry-ticket-counts") |>
  filter(name == 
           "Toronto Island Ferry Ticket Counts.csv") |>
  get_resource()

#### Save data ####
write_parquet(
  x = raw_ticket_data,
  sink = "inputs/data/raw_ticket_data.parquet"
)