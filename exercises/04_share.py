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
# # Exercises: Share Your Insights

# %%
import pandas as pd

postal_codes = pd.read_csv("../data/postal_codes.csv")
waste_collection = pd.read_json("../data/waste_collection.json")

# %% [markdown]
# ## 1. Create a Waste Collection Calendar
#
# Pivot the `waste_collection` data for the **basel** region to show which **type** of waste is collected for each **date** and **area**.

# %%

# %% [markdown]
# ## 2. Plot the most commonly collected waste
#
# Group the waste collection information by **type** and plot a horisontal bar diagram.

# %%

# %% [markdown]
# ## 3. Create a Table with an overview of waste collection
#
# Create a table showing the number of waste collections in each **region** for each waste **type**. Export the table to LaTeX.

# %%
