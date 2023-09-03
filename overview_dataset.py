import os

import pandas as pd


class OverviewDataset:
    def __init__(self, data_path):
        self.data = pd.read_csv(data_path)
        self.num_variables = len(self.data.columns)
        self.num_rows = len(self.data)
        self.num_missing_cells = self.data.isnull().sum().sum()
        self.file_size_mb = os.path.getsize(data_path) / (1024 * 1024)
        self.variable_types = self.data.dtypes.value_counts()
        self.categorical_num = len(self.data.dtypes[self.data.dtypes == "object"])
        self.numerical_num = self.num_variables - self.categorical_num

    def generate_summary_dict(self):
        summary_dict = {
            "변수의 수": self.num_variables,
            "행의 수": self.num_rows,
            "결측치인 셀의 수": self.num_missing_cells,
            "파일 메모리 크기": round(self.file_size_mb, 3),
            "범주형 변수의 수": self.categorical_num,
            "수치형 변수의 수": self.numerical_num,
        }
        return summary_dict

    def generate_summary_sentence(self):
        sentence = f"The data consists of {self.num_variables} columns, {self.num_rows} rows, {self.num_missing_cells} missing cells, {round(self.file_size_mb,3)}(MB) memory size, {self.categorical_num} categorical variables, and {self.numerical_num} numerical variables."
        return sentence
