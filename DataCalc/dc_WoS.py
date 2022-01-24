from DataCalc.dc import DataCalculation


class DataCalculationWoS(DataCalculation):
    def count_values(self):
        employees_dict = self.get_employees_dict()
        for authors in self.data_df["Authors"].to_list():
            tmp_dict = {}
            s = 0
            tmp_authors = []
            for i in authors.split("; "):
                name = self.find_in_dictionary(i)
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
