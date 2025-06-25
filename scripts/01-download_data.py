#### Preamble ####
# Purpose: Download and save data from https://open.toronto.ca/dataset/toronto-island-ferry-ticket-counts/
# Author: Denise Chang
# Date: 21 September 2024
# Contact: dede.chang@mail.utoronto.ca
# License: MIT
# Pre-requisites: None


#### Workspace setup ####
import requests
import pandas as pd
from io import StringIO

#### Download data ####

base_url = "https://ckan0.cf.opendata.inter.prod-toronto.ca"
url = base_url + "/api/3/action/package_show"
params = { "id": "toronto-island-ferry-ticket-counts"}
package = requests.get(url, params = params).json()

# To get resource data:
for idx, resource in enumerate(package["result"]["resources"]):
       if resource["datastore_active"]:

           # To get all records in CSV format:
           url = base_url + "/datastore/dump/" + resource["id"]
           resource_dump_data = requests.get(url).text
           df = pd.read_csv(StringIO(resource_dump_data))
           print(resource_dump_data)


#### Save data ####
df.to_csv("inputs/data/raw_ticket_data.csv", index=False)