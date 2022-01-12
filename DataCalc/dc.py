from pandas import DataFrame


class DataCalculation:
    department_values = {}

    def __init__(self, dictionary_df: DataFrame, employees_df: DataFrame, data_df: DataFrame):
        self.dictionary = dict(zip(dictionary_df["Сотрудник"].to_list(), dictionary_df["names"].to_list()))
        self.employees = employees_df
        self.data_df = data_df

    def find_in_dictionary(self, names: str):
        for keys, values in self.dictionary.items():
            if values.find(names.lower()) != -1:
                return keys
        else:
            return None

    def get_employees_dict(self) -> dict:
        department_list = self.employees["Подразделение"].to_list()
        names_list = self.employees["ФИО"].to_list()
        proportion_list = self.employees["Ставка"].to_list()
        result_dict = {}
        for i in range(len(department_list)):
            if department_list[i].find("Кафедра") != -1:
                if result_dict.get(department_list[i]):
                    result_dict[department_list[i]] |= {names_list[i]: proportion_list[i]}
                else:
                    result_dict |= {department_list[i]: {names_list[i]: proportion_list[i]}}
        return result_dict

    def count_values(self):
        pass

