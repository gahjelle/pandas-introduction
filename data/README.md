# Datasets for Introduction to pandas

The **Introduction to pandas** workshop uses three public datasets in demonstrations and exercises.

## Postal Codes in Switzerland

- **Description:** <https://www.geonames.org/postalcode-search.html?country=ch>
- **Original data:** <https://download.geonames.org/export/zip/CH.zip>
- **Prepared data:** [`postal_codes.csv`](postal_codes.csv)

[`prepare_postal_codes.py`](prepare_postal_codes.py) downloads and converts the original data.

Postal code data are from the [GeoNames geographical database](https://www.geonames.org/) and licensed under a [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/).

## Waste collection data for Zürich, Thalwil, Basel, and St. Gallen

- **Description:** <https://openerz.metaodi.ch/documentation>
- **Original data:** <https://openerz.metaodi.ch/api/calendar.json?offset=0&limit=10000&lang=en&start=2022-01-01&end=2022-09-01>
- **Prepared data:** [`waste_collection.json`](waste_collection.json)

[`prepare_waste_collection.py`](prepare_waste_collection.py) downloads and converts the original data.

Waste collection data are from [OpenERZ](https://github.com/metaodi/openerz) API [based on data](https://github.com/metaodi/openerz/tree/master/csv) from Open Data Portals in Zürich and Basel and licensed under Creative Commons licenses.

## Top 100 Billboard in the year 2000

- **Description:** <https://tidyr.tidyverse.org/reference/billboard.html>
- **Original data:** <https://raw.githubusercontent.com/hadley/tidy-data/master/data/billboard.csv>
- **Prepared data:** [`billboard_songs.csv`](billboard_songs.csv), [`billboard_ranks.csv`](billboard_ranks.csv)

[`prepare_billboard.py`](prepare_billboard.py) downloads and converts the original data.
