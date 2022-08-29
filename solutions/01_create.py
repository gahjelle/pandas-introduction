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
# # Exercises: Create DataFrames

# %%
import pandas as pd

# %% [markdown]
# ## 1. Create a DataFrame from Python structures
#
# Create a DataFrame with the following data:
#
# |           | quiz_1   | quiz_2   | final   |
# |:----------|:---------|:---------|:--------|
# | Guido     | B        | A        | A       |
# | Wes       | -        | C        | C       |
# | Geir Arne | C        | D        | D       |

# %%
grades = [
    {"quiz_1": "B", "quiz_2": "A", "final": "A"},
    {"quiz_2": "C", "final": "C"},
    {"quiz_1": "C", "quiz_2": "D", "final": "D"},
]
pd.DataFrame(grades, index=["Guido", "Wes", "Geir Arne"])

# %% [markdown]
# ## 2. Read a DataFrame from files
#
# Read the file `../data/waste_collection.json` as a Python DataFrame.

# %%
pd.read_json("../data/waste_collection.json")

# %%
