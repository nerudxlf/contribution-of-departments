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

    def get_value_kbpr(self):
        name_list = self.employees["ФИО"].to_list()
        return len(set(name_list))

    def count_values(self):
        employees_dict = self.get_employees_dict()
        for authors in self.data_df["Авторы"].to_list():
            for i in authors.split(", "):
                name = self.find_in_dictionary(i)
                if not name:
                    break
                for keys, values in employees_dict.items():
                    if values.get(name):
                        if self.department_values.get(keys):
                            self.department_values[keys] += values[name]
                        else:
                            self.department_values |= {keys: values[name]}
        return self.department_values

    def count_proportion(self):
        kbpr_value = self.get_value_kbpr()
        return_result = self.department_values
        for keys, values in return_result.items():
            return_result[keys] = round(values, 2) / kbpr_value
        return return_result
