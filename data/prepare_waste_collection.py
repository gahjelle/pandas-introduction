"""Download and prepare data about waste collection in Switzerland"""

# %% Imports
import pathlib

import pandas as pd
import requests

# %% Download waste collection data from openerz.org
URL = (
    "https://openerz.metaodi.ch/api/calendar.json?offset=0&limit=10000&lang=en"
    "&start=2022-01-01&end=2022-09-01"
)
OUTPUT_PATH = pathlib.Path("waste_collection.json")

# %% Download data from server
response = requests.get(URL)
if not response:
    response.raise_for_status()

# %% Parse waste collection data into DataFrame
waste_collection = (
    pd.DataFrame(response.json()["result"]).fillna({"zip": 0}).astype({"zip": int})
)

# %% Store waste collection information as a JSON file
waste_collection.to_json(OUTPUT_PATH, orient="records")
