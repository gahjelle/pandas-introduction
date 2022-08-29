# Introduction to pandas

This repository contains material for the tutorial I presented at the [EuroSciPy 2022](https://www.euroscipy.org/2022/) conference in Basel.

## Topics

The tutorial cover the following topics:

1. DataFrames as Panels of Data
2. Create DataFrames
3. Work With Tidy Data
4. Manipulate DataFrames
5. Share Results and Insights

The workshop consists of 90 minutes of live code demonstrations and hands-on exercises.

## Data

The demos and examples use three public datasets:

1. [`data/postal_codes.csv`](data/postal_codes.csv): Postal Codes in Switzerland
2. [`data/waste_collection.json`](data/waste_collection.json): Waste collection data for Zürich, Thalwil, Basel, and St. Gallen
3. [`data/billboard_songs.csv`](data/billboard_songs.csv) and [`data/billboard_ranks.csv`](data/billboard_ranks.csv): Top 100 songs on Billboard in 2000

See [`data/`](data/) for more information, including licenses and links to the original datasets.

## Preparations

You should create a virtual environment and install pandas and other necessary dependencies.

> **Note:** Demonstrations were done on Linux Ubuntu with Python 3.10.6 and packages and versions specified in [`requirements.txt`](requirements.txt).

### Conda/Anaconda

If you have installed the full **Anaconda** distribution, you already have all the necessary dependencies on your system.

If you're running **Miniconda** or want to set up a separate environment for this tutorial, you can use `conda` to do so:

```console
$ conda env create -n euroscipy-pandas -f environment.yml
$ conda activate euroscipy-pandas
```

Remember to activate your Conda environment.

### Pip

If you're using a plain Python distribution, then you can use `venv` to create a [virtual environment](https://realpython.com/python-virtual-environments-a-primer/):

```console
$ python -m venv venv
$ source venv/bin/activate
(venv) $ python -m pip install -r requirements.in
```

On Windows, you don't need `source` when activating your virtual environment. You can type `venv\Scripts\activate` instead.

## Exercises

You'll find the exercises in the [`exercises/`](exercises/) folder. You can open the `.py` files in your favorite editor. It may be helpful if your editor supports cells in script files. For example, [VS Code](https://code.visualstudio.com/) and [Spyder](https://www.spyder-ide.org/) support these cells and make it more convenient to run your solutions.

If you prefer to solve the exercises in Jupyter, you can convert the exercise files to notebooks using [`jupytext`](https://jupytext.readthedocs.io/):

```console
(venv) $ cd exercises/
(venv) $ jupytext --sync *.py
```

`jupytext` will convert all exercise files to notebooks that you can open in Jupyter Lab, or any other compatible notebook environment.

You can find solutions to all exercises in the [`solutions`](solutions/) folder.

## Demonstrations

The workshop mostly consists of live code demonstrations. You can find simple notes from the demos in the file [`pandas_introduction.py`](pandas_introduction.py). Use `jupytext` to convert the notes to a Jupyter Notebook if you prefer.

---

Demonstration code, exercises, and solutions are licensed under an [MIT license](LICENSE).