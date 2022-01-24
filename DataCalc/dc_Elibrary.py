import re

from DataCalc.dc import DataCalculation


class DataCalculationElibrary(DataCalculation):
    def __get_name(self, name: str):
        if bool(re.search('[а-яА-Я]', name)):
            return name
        else:
            name = self.find_in_dictionary(name)
            if name:
                name_list = name.split()
                if len(name_list) == 2:
                    return f"{name_list[0]} {name_list[1][0]}."
                elif len(name_list) == 3:
                    return f"{name_list[0]} {name_list[1][0]}.{name_list[2][0]}."
            return None

    def get_employees_dict(self):
        department_list = self.employees["Подразделение"].to_list()
        names_list = self.employees["ФИО"].to_list()
        proportion_list = self.employees["Ставка"].to_list()
        result_dict = {}
        for i in range(len(department_list)):
            if department_list[i].find("Кафедра") != -1:
                if result_dict.get(department_list[i]):
                    names_list_split = names_list[i].split()
                    if len(names_list_split) == 2:
                        name = f"{names_list_split[0]} {names_list_split[1][0]}."
                    else:
                        name = f"{names_list_split[0]} {names_list_split[1][0]}.{names_list_split[2][0]}."
                    result_dict[department_list[i]] |= {name: proportion_list[i]}
                else:
                    names_list_split = names_list[i].split()
                    if len(names_list_split) == 2:
                        name = f"{names_list_split[0]} {names_list_split[1][0]}."
                    else:
                        name = f"{names_list_split[0]} {names_list_split[1][0]}.{names_list_split[2][0]}."
                    result_dict |= {department_list[i]: {name: proportion_list[i]}}
        tmp_dict = self._get_sum_dict_npr(result_dict)
        return_dict = self._get_current_value_proportion_npr(tmp_dict, result_dict)
        return result_dict

    def count_values(self):
        employees_dict = self.get_employees_dict()
        for authors in self.data_df["Авторы"].to_list():
            tmp_dict = {}
            s = 0
            tmp_authors = []
            for i in authors.split(", "):
                name = self.__get_name(i)
                if not name or name in tmp_authors:
                    continue
                tmp_authors.append(name)
                for keys, values in employees_dict.items():
                    if values.get(name):
                        if tmp_dict.get(keys):
                            s += values[name]
                            tmp_dict[keys] += values[name]
                        else:
                            s += values[name]
                            tmp_dict |= {keys: values[name]}
            for keys, values in tmp_dict.items():
                if self.department_values.get(keys):
                    self.department_values[keys] += values / s
                else:
                    self.department_values |= {keys: values / s}
        return self.department_values



