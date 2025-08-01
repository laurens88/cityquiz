import polars as pl
import pandas as pd

class DataReader:
    def __init__(self):
        self.data = pl.from_pandas(pd.read_csv("data/cities.csv", sep=";"))

    def prepare_data(self):
        self.data = self.data.filter(pl.col("Population") >= 1000).select("Name", "Population").sort(by="Population", descending=True)

    def get_data(self):
        return self.data

