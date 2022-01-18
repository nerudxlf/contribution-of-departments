from pandas import DataFrame


class DataCalculation:
    department_values = {}

    def __init__(self, dictionary_df: DataFrame, employees_df: DataFrame, data_df: DataFrame):
        """
        :param x: исходный словарь
        :param y: словарь для объединения со словарем x
        :return: возвращает объединенный словарь
        """
        self.dictionary = dict(zip(dictionary_df["Сотрудник"].to_list(), dictionary_df["names"].to_list()))
        self.employees = employees_df
        self.data_df = data_df

    def find_in_dictionary(self, names: str):
        """
        Класс родитель для подсчета показателей
        :function find_in_dictionary: метод для поиска человека в словаре
        :function __get_sum_dict_npr: статическая функция, для суммирования всех
        ставок одного нпр
        :__get_current_value_proportion_npr: статическая функция, для нахождения
        усредненной ставки
        :get_employees_dict: метод для получения нпр из списка с его текущей ставкой
        :count_values: метод для расчета показателей по кафедрам
        """
        for keys, values in self.dictionary.items():
            if values.find(names.lower()) != -1:
                return keys
        else:
            return None

    @staticmethod
    def _get_sum_dict_npr(dictionary: dict) -> dict:
        tmp_dict = {}
        for values in dictionary.values():
            for keys_v, values_v in values.items():
                if tmp_dict.get(keys_v):
                    tmp_dict[keys_v] += values_v
                else:
                    tmp_dict |= {keys_v: values_v}
        return tmp_dict

    @staticmethod
    def _get_current_value_proportion_npr(dictionary_tmp: dict, current_dict: dict) -> dict:
        for keys, values in current_dict.items():
            for keys_v, values_v in values.items():
                current_dict[keys][keys_v] = values_v / dictionary_tmp[keys_v]
        return current_dict

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
        tmp_dict = self._get_sum_dict_npr(result_dict)
        return_dict = self._get_current_value_proportion_npr(tmp_dict, result_dict)
        return return_dict

    def count_values(self):
        pass
