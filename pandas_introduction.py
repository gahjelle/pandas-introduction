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
# # Introduction to pandas
#
# **EuroSciPy 2022, Basel**
#
# Contact: **Geir Arne Hjelle**, `geirarne@gmail.com`, <https://github.com/gahjelle/pandas-introduction>
#
# **Agenda:**
#
# 1. DataFrames as Panels of Data
# 2. Create DataFrames
# 3. Work With Tidy Data
# 4. Manipulate DataFrames
# 5. Share Results and Insights

# %% [markdown]
# ## DataFrames as Panels of Data
#
# A **DataFrame** is the main data structure used in pandas. A DataFrame is analogous to a structured spread sheet. In particular:
#
# - A DataFrame is a **two-dimensional** table of rows and columns
# - Each column has a **name**
# - All values in a column have the **same data type**
# - Each row has an **index**, in general indicies do _not_ need to be unique
#
# Here are some examples of tables organized as DataFrames:
#
# | Time                | HS118                                             | HS120                                             |
# |:--------------------|:--------------------------------------------------|:--------------------------------------------------|
# | 2022-08-29 08:30:00 | Getting Started With JupyterLab                   | Increase Citations, Ease Review and Collaboration |
# | 2022-08-29 10:30:00 | Introduction to Python for Scientific Programming | Time Series Forecasting With scikit-learn         |
# | 2022-08-29 13:30:00 | Introduction to NumPy                             | Evaluating Your Machine Learning Models           |
# | 2022-08-29 15:30:00 | Introduction to pandas                            | Introduction to Audio and Speech Recognition      |
# | 2022-08-30 08:30:00 | Introduction to SciPy                             | Introduction to PyTorch                           |
# | 2022-08-30 10:30:00 | Introduction to scikit-learn I                    | Introduction to Geospatial Data Analysis          |
# | 2022-08-30 13:30:00 | Introduction to scikit-learn II                   | Image Processing With scikit-image                |
# | 2022-08-30 15:30:00 | Effectively Using MatPlotLib                      | Network Science With Python                       |
#
# A subset of the data can be presented as follows:
#
# | Room   | 2022-08-29 08:30:00                               | 2022-08-29 10:30:00                               | 2022-08-29 13:30:00                     | 2022-08-29 15:30:00                          |
# |:-------|:--------------------------------------------------|:--------------------------------------------------|:----------------------------------------|:---------------------------------------------|
# | HS118  | Getting Started With JupyterLab                   | Introduction to Python for Scientific Programming | Introduction to NumPy                   | Introduction to pandas                       |
# | HS120  | Increase Citations, Ease Review and Collaboration | Time Series Forecasting With scikit-learn         | Evaluating Your Machine Learning Models | Introduction to Audio and Speech Recognition |
#

# %% [markdown]
# ## Create DataFrames
#
# At a high level, you can create DataFrames in two ways:
#
# 1. From an existing Python data structure in memory, typically nested `dict` and/or `list`
# 2. From a data source like a file, database, etc
#
# You use `pd.DataFrame()` to convert an existing Python data structure. There are several `read_*()` functions in pandas that construct DataFrames from different data sources.

# %%
import pandas as pd

# %%
# Create a DataFrame from a list of dictionaries
tutorials = [
    {
        "HS118": "Getting Started With JupyterLab",
        "HS120": "Increase Citations, Ease Review and Collaboration",
    },
    {
        "HS118": "Introduction to Python for Scientific Programming",
        "HS120": "Time Series Forecasting With scikit-learn",
    },
    {
        "HS118": "Introduction to NumPy",
        "HS120": "Evaluating Your Machine Learning Models",
    },
    {
        "HS118": "Introduction to pandas",
        "HS120": "Introduction to Audio and Speech Recognition",
    },
]
pd.DataFrame(tutorials, index=["08:30", "10:30", "13:30", "15:30"])

# %%
# Create a DataFrame from a dictionary of lists
tutorials = {
    "HS118": [
        "Getting Started With JupyterLab",
        "Introduction to Python for Scientific Programming",
        "Introduction to NumPy",
        "Introduction to pandas",
    ],
    "HS120": [
        "Increase Citations, Ease Review and Collaboration",
        "Time Series Forecasting With scikit-learn",
        "Evaluating Your Machine Learning Models",
        "Introduction to Audio and Speech Recognition",
    ],
}
pd.DataFrame(tutorials, index=["08:30", "10:30", "13:30", "15:30"])

# %%
# Create a DataFrame from a CSV file
pd.read_csv("data/billboard_songs.csv")

# %%
[function for function in dir(pd) if function.startswith("read_")]

# %% [markdown]
# ## Work With Tidy Data
#
# Hadley Wickham introduced the term **tidy data** (<https://tidyr.tidyverse.org/articles/tidy-data.html>). Data tidying is a way to **structure DataFrames to facilitate analysis**.
#
# A DataFrame is tidy if:
#
# - Each variable is a column
# - Each observation is a row
# - Each DataFrame contains one observational unit
#
# Note that tidy data principles are closely tied to normalization of relational databases.
#
# Is the following DataFrame tidy?

# %%
schedule = pd.DataFrame(tutorials, index=["08:30", "10:30", "13:30", "15:30"])
schedule

# %% [markdown]
# What about the following DataFrame?

# %%
schedule.T

# %% [markdown]
# What are the variables in the dataset? Time slots, rooms, and tutorial titles. They should each be their own column. Tidy the dataset:

# %%
(
    schedule.melt(ignore_index=False)
    .reset_index()
    .rename(columns={"index": "time", "variable": "room", "value": "title"})
    .sort_values(by=["time", "room"])
    .reset_index(drop=True)
)

# %% [markdown]
# Being conscious of tidy data lets you standardize your **data cleaning** and **analysis**:
#
# 1. Tidy your data set
# 2. Clean your data (e.g. check outliers, parse dates, impute missing values)
# 3. Analyze
# 4. Share and visualize
#
# **Note:** Datasets from Hadley Wickham's Tidy Data paper are at <https://github.com/hadley/tidy-data/tree/master/data>

# %% [markdown]
# ## Manipulate DataFrames
#
# pandas DataFrames have many methods you can use to manipulate your data. They fall into several categories:
#
# - **Filter**: remove observations
# - **Transform**: add or modify variables based on existing variables
# - **Aggregate**: collapse multiple values into a single value
# - **Sort**: change the order of observations

# %%
schedule = pd.read_csv("data/schedule.csv", parse_dates=["timestamp"])
schedule

# %%
songs = pd.read_csv("data/billboard_songs.csv")
ranks = pd.read_csv("data/billboard_ranks.csv", parse_dates=["date"])
songs

# %% [markdown]
# ### Filter

# %%
songs.loc[:, ["artist", "track", "time"]]

# %%
schedule.loc[:, ["timestamp", "title"]]

# %%
schedule.drop(columns=["room"])

# %%
schedule.set_index("timestamp").loc["2022-08-29"]

# %%
schedule.query("room == 'HS118'")

# %%
schedule.query("timestamp.dt.hour == 10")

# %%
schedule.query("title.str.startswith('Intro')")

# %%
schedule.query("title.str.contains('scikit')")

# %%
billboard.query("artist == 'Jay-Z'").loc[:, ["track", "time"]]

# %%
ranks.select_dtypes(include="number")

# %% [markdown]
# ### Aggregate

# %%
ranks.sum()

# %%
ranks.select_dtypes(include="number").mean()

# %%
ranks.groupby("id").size().sort_values(ascending=False)

# %%
ranks.groupby("id").first()

# %%
ranks.groupby("id").agg({"date": "first", "rank": "min"})

# %%
billboard = songs.merge(ranks, left_on="id", right_on="id")
billboard

# %%
for song_id, info in billboard.groupby("id"):
    if info["rank"].min() == 1:
        print(info.query("rank == 1"))

# %% [markdown]
# ### Transform

# %%
schedule.assign(date=schedule.timestamp.dt.date, time=schedule.timestamp.dt.time)

# %%
(
    songs.set_index("id")
    .assign(
        date_entered=ranks.groupby("id").agg({"date": "min"}),
        peak_position=ranks.groupby("id").agg({"rank": "min"}),
        num_weeks=ranks.groupby("id").size(),
        avg_position=ranks.loc[:, ["id", "rank"]].groupby("id").mean(),
        score=lambda df: df.num_weeks * (100 - df.avg_position),
    )
    .drop(columns=["time", "genre"])
)

# %% [markdown]
# ### Sort

# %%
scored_billboard = (
    songs.set_index("id")
    .assign(
        num_weeks=ranks.groupby("id").size(),
        avg_position=ranks.loc[:, ["id", "rank"]].groupby("id").mean(),
        score=lambda df: df.num_weeks * (100 - df.avg_position),
    )
    .drop(columns=["time", "genre"])
)

# %%
scored_billboard.sort_index()

# %%
scored_billboard.sort_values(by="artist")

# %%
scored_billboard.sort_values(by="artist", key=lambda artist: artist.str.lower())

# %%
scored_billboard.sort_values(by="num_weeks", ascending=False)

# %%
scored_billboard.sort_values(by=["num_weeks", "avg_position"], ascending=[False, True])

# %%
scored_billboard.sort_values(by="score", ascending=False)

# %% [markdown]
# ## Share Results and Insights
#
# When you want to share your insights, you often want to **untidy** your data again:

# %%
schedule.pivot_table(index="timestamp", columns="room", values="title", aggfunc="first")

# %% [markdown]
# In the same way you can use pandas to read from many different data sources, you can also write to many different outputs.

# %%
[method for method in dir(schedule) if method.startswith("to_")]

# %%
scored_billboard.sort_values(by="score", ascending=False).head(10).loc[
    :, ["artist", "track", "num_weeks"]
].to_csv("top_songs_2000.csv", index=False)

# %%
ranks.plot.scatter(x="date", y="rank", alpha=0.4)

# %%
ranks.query("id < 5").groupby("id").plot.line(x="date", y="rank", marker="+")

# %%
