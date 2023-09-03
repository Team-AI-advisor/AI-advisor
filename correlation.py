import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats


class Correlation:
    def __init__(self, data_path):
        self.data = pd.read_csv(data_path)
        self.num_data = self.data[
            self.data.columns[self.data.dtypes != "object"]
        ].dropna(axis=0)
        self.alpha = 0.05

    def plot_correlation(self):
        correlation_matrix = self.data.corr()
        mask = np.zeros_like(correlation_matrix, dtype=np.bool_)
        mask[np.triu_indices_from(mask)] = True
        plt.figure(figsize=(10, 8))
        sns.heatmap(
            correlation_matrix,
            mask=mask,
            annot=True,
            cmap="Blues",
            fmt=".2f",
            vmin=-1,
            vmax=1,
        )
        plt.title("Heat map")
        plt.show()

    def find_correlation(self, threshold_min, threshold_max):
        pairs = ""
        corr_pairs = []
        num_variables = len(self.num_data.columns)
        for i in range(num_variables):
            for j in range(i + 1, num_variables):
                variable1 = self.num_data.columns[i]
                variable2 = self.num_data.columns[j]
                correlation_coefficient, p_value = stats.pearsonr(
                    self.num_data[variable1], self.num_data[variable2]
                )
                if (p_value < self.alpha) and (
                    threshold_min <= correlation_coefficient < threshold_max
                ):
                    corr_pairs.append(
                        (variable1, variable2, correlation_coefficient, p_value)
                    )

        if len(corr_pairs) >= 1:
            for pair in corr_pairs:
                pairs += f"{pair[0]} and {pair[1]}, "  # ({round(pair[2],2)})
            return pairs
        else:
            return "not."

    def generate_correlation_sentence(self):
        negative = (
            "Among the pairs with significant correlations of variables, a pair of variables with a low negative correlation is "
            + str(self.find_correlation(-0.4, -0.2))
            + "a pair of variables with a somewhat higher negative correlation is "
            + str(self.find_correlation(-0.7, -0.4))
            + "a pair of variables with a high negative correlation is "
            + str(self.find_correlation(-1.0, -0.7))
        )
        positive = (
            "Among the pairs with significant correlations of variables, a pair of variables with a low positive correlation is "
            + str(self.find_correlation(0.2, 0.4))
            + "a pair of variables with a somewhat higher positive correlation is "
            + str(self.find_correlation(0.4, 0.7))
            + "a pair of variables with a high positive correlation is "
            + str(self.find_correlation(0.7, 1.0))
        )
        return negative + positive
