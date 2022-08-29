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
waste_collection.loc[:, ["date", "type", "region"]]

# %% [markdown]
# B. Find postal codes inside the **Basel** municipality.

# %%
postal_codes.query("municipality == 'Basel'").loc[:, ["postal_code"]]

# %% [markdown]
# C. Find information about postal codes in all cantons with **Basel** in their name.

# %%
postal_codes.query("canton.str.contains('Basel')")

# %% [markdown]
# D. Find information about waste collection in the **basel** region.

# %%
waste_collection.query("region == 'basel'")

# %% [markdown]
# ## 2. Aggregate
#
# A. Find the average latitude and longitude of all postal code data.

# %%
postal_codes.loc[:, ["latitude", "longitude"]].mean()

# %% [markdown]
# B. Find the average latitude and longitude of all postal codes in the **Basel** municipality.

# %%
postal_codes.query("municipality == 'Basel'").loc[:, ["latitude", "longitude"]].mean()

# %% [markdown]
# C. Find the average latitude and longitude of all cantons.

# %%
postal_codes.groupby("canton").mean().loc[:, ["latitude", "longitude"]]

# %% [markdown]
# D. Merge `postal_codes` and `waste_collection` on the postal code.

# %%
waste_collection.query("zip != 0").merge(
    postal_codes, left_on="zip", right_on="postal_code", how="left"
)

# %% [markdown]
# ## 3. Transform
#
# A. Remove the word `Kanton` from the canton column in `postal_codes`.

# %%
postal_codes.assign(canton=postal_codes["canton"].str.replace("Kanton ", ""))

# %% [markdown]
# B. Add the canton code to the name in parentheses in `postal_codes`. For example, Aarau in Kanton Aargau becomes `Aarau (AG)`.

# %%
postal_codes.assign(
    name=postal_codes.apply(
        lambda row: f"{row['name']} ({row['canton_code']})", axis="columns"
    )
)

# %% [markdown]
# ## 4. Sort
#
# A. Sort postal codes alphabetically by name.

# %%
postal_codes.sort_values(by="name")

# %% [markdown]
# B. Sort postal codes by latitude from North to South.

# %%
postal_codes.sort_values(by="latitude", ascending=False)

# %% [markdown]
# C. Sort postal codes, first descending by district code, then ascending by municipality name.

# %%
postal_codes.sort_values(by=["district_code", "municipality"], ascending=[False, True])
