from DataCalc.dc import DataCalculation


class DataCalculationWoS(DataCalculation):
    def count_values(self):
        employees_dict = self.get_employees_dict()
        for authors in self.data_df["Authors"].to_list():
            for i in authors.split("; "):
                name = self.find_in_dictionary(i)
                if not name:
                    print(i)
                    break
                for keys, values in employees_dict.items():
                    if values.get(name):
                        if self.department_values.get(keys):
                            self.department_values[keys] += values[name]
                        else:
                            self.department_values |= {keys: values[name]}
        return self.department_values