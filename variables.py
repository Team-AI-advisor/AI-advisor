import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib import font_manager
from scipy.stats import skew, kurtosis

f_path = "C:/windows/Fonts/malgun.ttf"
font_manager.FontProperties(fname=f_path).get_name()
rc("font", family="Malgun Gothic")


class Variable:
    def __init__(self, data_path):
        self.data = pd.read_csv(data_path)
        for column in self.data.columns:
            unique_count = self.data[column].nunique()
            if (self.data[column].dtype == "int64") or (
                self.data[column].dtype == "int32"
            ):
                if unique_count < len(self.data) / 2:
                    self.data[column] = self.data[column].astype("object")
        self.columns = self.data.columns

    def variable_statistic(self, idx):
        if self.data[self.columns[idx]].dtype != "object":
            self.mean = round(self.data[self.columns[idx]].mean(), 3)
            self.std = round(self.data[self.columns[idx]].std(), 3)
            self.q1 = self.data[self.columns[idx]].quantile(0.25)
            self.median = self.data[self.columns[idx]].median()
            self.q3 = self.data[self.columns[idx]].quantile(0.75)
            self.min = self.data[self.columns[idx]].min()
            self.max = self.data[self.columns[idx]].max()
            self.missing = self.data[self.columns[idx]].isnull().sum()
            self.skewness = round(
                skew(self.data[self.columns[idx]], nan_policy="omit"), 3
            )
            self.kurtosis = round(
                kurtosis(self.data[self.columns[idx]], nan_policy="omit"), 3
            )
            static_dict = {
                "평균": self.mean,
                "표준편차": self.std,
                "최솟값": self.min,
                "25%": self.q1,
                "중앙값": self.median,
                "75%": self.q3,
                "최댓값": self.max,
                "결측치 수": self.missing,
                "왜도": self.skewness,
                "첨도": self.kurtosis,
            }
            return static_dict
        else:
            self.distinct_count = self.data[self.columns[idx]].nunique()
            self.missing = self.data[self.columns[idx]].isnull().sum()
            static_dict = {"변수 값의 종류": self.distinct_count, "결측치 수": self.missing}
            return static_dict

    def variable_plot(self, idx):
        if self.data[self.columns[idx]].dtype != "object":
            plt.figure(figsize=(8, 6))
            plt.hist(self.data[self.columns[idx]].dropna(), bins=20)
            plt.xlabel(self.columns[idx])
            plt.ylabel("빈도")
            plt.title(f"{self.columns[idx]}의 분포")
            plt.show()
        else:
            self.value_counts = self.data[self.columns[idx]].value_counts()
            num_categories = len(self.value_counts)
            if num_categories >= len(self.data) / 2:
                self.value_counts = self.value_counts.head(10)
            plt.figure(figsize=(8, 6))
            self.value_counts.plot(kind="bar")
            plt.xlabel(self.columns[idx])
            plt.ylabel("빈도")
            if num_categories >= len(self.data) / 2:
                plt.title(f"Top 10 {self.columns[idx]} 범주의 빈도수")
            else:
                plt.title(f"{self.columns[idx]}의 빈도수")
            plt.show()

    def variable_sentence(self, idx):
        if self.data[self.columns[idx]].dtype != "object":
            sen1 = (
                f"When examing the distribution of the {self.columns[idx]} variable, "
            )
            sen2 = f"we find that the mean is {self.mean}, the standard deviation is {self.std}, "
            sen3 = f"the minimum value is {self.min}, the 1st quartile is {self.q1}, the median is {self.median}, the 3rd quartile is {self.q3}, the maximum value is {self.max}, the skewness is {self.skewness}, the kurtosis is {self.kurtosis}."
            return sen1 + sen2 + sen3
        else:
            value_sentence = dict(self.value_counts)
            sen1 = (
                f"when examing the distribution of the {self.columns[idx]} variable, "
            )
            sen2 = f"there are {self.distinct_count} categories, and the respective frequency counts are {value_sentence}."
            return sen1 + sen2
