import pandas as pd

from DataCalc.dc_Scopus import DataCalculationScopus
from DataCalc.dc_WoS import DataCalculationWoS
from DataCalc.dc_Elibrary import DataCalculationElibrary


def main():
    dictionary_df = pd.read_excel("data/dictionary.xlsx")
    employees_df = pd.read_excel("data/Сотрудники.xls")
    data_df = pd.read_excel("data/WoS 2021 AR E.xls")
    # elib_df = pd.read_excel("data/Elibrary 2021 A.xlsx")

    dc_wos = DataCalculationWoS(dictionary_df, employees_df, data_df)
    count_values = dc_wos.count_values()
    # dc_scopus = DataCalculationScopus(dictionary_df, employees_df, data_df)
    # count_values = dc_scopus.count_values()

    # dc_elibrary = DataCalculationElibrary(dictionary_df, employees_df, elib_df)
    # count_values = dc_elibrary.count_values()
    result_df = pd.DataFrame({"Кафедра": count_values.keys(), "Значения": count_values.values()})
    result_df.to_excel("data/result WoS 2021 AR E.xlsx", index=False)


