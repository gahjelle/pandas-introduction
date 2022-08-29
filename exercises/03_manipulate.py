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
# # Exercises: Manipulate DataFrames

# %%
import pandas as pd

postal_codes = pd.read_csv("../data/postal_codes.csv")
waste_collection = pd.read_json("../data/waste_collection.json")

# %% [markdown]
# ## 1. Filter
#
# A. Show date, type, and region in the `waste_collection` dataset:

# %%

# %% [markdown]
# B. Find postal codes inside the **Basel** municipality.

# %%

# %% [markdown]
# C. Find information about postal codes in all cantons with **Basel** in their name.

# %%

# %% [markdown]
# D. Find information about waste collection in the **basel** region.

# %%

# %% [markdown]
# ## 2. Aggregate
#
# A. Find the average latitude and longitude of all postal code data.

# %%

# %% [markdown]
# B. Find the average latitude and longitude of all postal codes in the **Basel** municipality.

# %%

# %% [markdown]
# C. Find the average latitude and longitude of all cantons.

# %%

# %% [markdown]
# D. Merge `postal_codes` and `waste_collection` on the postal code.

# %%

# %% [markdown]
# ## 3. Transform
#
# A. Remove the word `Kanton` from the canton column in `postal_codes`.

# %%

# %% [markdown]
# B. Add the canton code to the name in parentheses in `postal_codes`. For example, Aarau in Kanton Aargau becomes `Aarau (AG)`.

# %%

# %% [markdown]
# ## 4. Sort
#
# A. Sort postal codes alphabetically by name.

# %%

# %% [markdown]
# B. Sort postal codes by latitude from North to South.

# %%

# %% [markdown]
# C. Sort postal codes, first descending by district code, then ascending by municipality name.

# %%
