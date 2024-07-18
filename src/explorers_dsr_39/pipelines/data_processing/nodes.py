import pandas as pd


def impute_data(Xtrain):
    return Xtrain.dropna(axis=0)
