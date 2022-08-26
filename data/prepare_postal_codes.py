"""Download and prepare data about postal codes in Switzerland"""

# %% Imports
import io
import pathlib
import zipfile

import pandas as pd
import requests

# %% Download Switzerland data from geonames.org
COUNTRY = "CH"
URL = f"https://download.geonames.org/export/zip/{COUNTRY}.zip"
OUTPUT_PATH = pathlib.Path("postal_codes.csv")

# %% Download ZIP file from server
response = requests.get(URL)
if not response:
    response.raise_for_status()

# %% Read postal codes from ZIP file
with zipfile.ZipFile(io.BytesIO(response.content), mode="r") as archive:
    raw_codes = archive.read(f"{COUNTRY}.txt").decode(encoding="utf-8")

# %% Parse postal codes and store as CSV
codes = pd.read_csv(
    io.StringIO(raw_codes),
    sep="\t",
    names=[
        "country",
        "postal_code",
        "name",
        "canton",
        "canton_code",
        "district",
        "district_code",
        "municipality",
        "municipality_code",
        "latitude",
        "longitude",
        "accuracy",
    ],
).drop(columns=["accuracy"])

# %% Store postal codes as a regular CSV file
codes.to_csv(OUTPUT_PATH, index=False)
