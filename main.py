import pandas as pd

from DataCalc.dc import DataCalculation


def main():
    dictionary_df = pd.read_excel("data/dictionary.xlsx")
    employees_df = pd.read_excel("data/Сотрудники.xls")
    data_df = pd.read_excel("data/2016_2021_AR.xlsx")

    dc = DataCalculation(dictionary_df, employees_df, data_df)
    print(dc.count_values())
    print(dc.count_proportion())
