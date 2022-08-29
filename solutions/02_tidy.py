# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Exercises: Work With Tidy Data

# %%
import pandas as pd

# %% [markdown]
# ## 1. Tidy the Grades dataset
#
# Convert the following `grades` dataset to a tidy form

# %%
grades = pd.DataFrame(
    [
        {"quiz_1": "B", "quiz_2": "A", "final": "A"},
        {"quiz_2": "C", "final": "C"},
        {"quiz_1": "C", "quiz_2": "D", "final": "D"},
    ],
    index=["Guido", "Wes", "Geir Arne"],
)

# %%
(
    grades.melt(ignore_index=False)
    .reset_index()
    .rename(columns={"index": "person", "variable": "event", "value": "grade"})
    .dropna()
)

# %% [markdown]
# ## 2. Tidy the Weather dataset
#
# Read Hadley Wickham's `weather` dataset and convert it to a tidy form.

# %%
weather = pd.read_fwf(
    "https://raw.githubusercontent.com/hadley/tidy-data/master/data/weather.txt",
    colspecs=[
        (0, 21),
        (21, 26),
        (29, 34),
        (37, 42),
        (45, 50),
        (53, 58),
        (61, 66),
        (69, 74),
        (77, 82),
        (85, 90),
        (93, 98),
        (101, 106),
        (109, 114),
        (117, 122),
        (125, 130),
        (133, 138),
        (141, 146),
        (149, 154),
        (157, 162),
        (165, 170),
        (173, 178),
        (181, 186),
        (189, 194),
        (197, 202),
        (205, 210),
        (213, 218),
        (221, 226),
        (229, 234),
        (237, 242),
        (245, 250),
        (253, 258),
        (261, 266),
    ],
    header=None,
).rename(columns={0: "info"})

# %%
from datetime import datetime

(
    weather.melt(id_vars=["info"], var_name="day")
    .assign(
        year=lambda df: df["info"].str[11:15].astype(int),
        month=lambda df: df["info"].str[15:17].astype(int),
        variable=lambda df: df["info"].str[17:21],
    )
    .replace(-9999, pd.NA)
    .dropna(subset=["value"])
    .assign(
        date=lambda df: df.loc[:, ["year", "month", "day"]].apply(
            lambda row: datetime(*row), axis="columns"
        )
    )
    .loc[:, ["date", "variable", "value"]]
    .sort_values(by="date")
    .reset_index(drop=True)
)
