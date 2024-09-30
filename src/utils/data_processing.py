import pandas as pd

def load_data(path):
    return pd.read_csv(path)


df = load_data("./data/donnees_pays.csv")


data_world_sunbrust = load_data("./data/donnees_sun.csv")