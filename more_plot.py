from pandasai.llm.openai import OpenAI
import pandas as pd
from pandasai import SmartDataframe


class MorePlot:
    def __init__(self, openai_api_key):
        self.llm = OpenAI(api_token=openai_api_key)

    def generate_plot(self, prompt, data_path):
        data = pd.read_csv(data_path)
        data = SmartDataframe(data, config={"llm": self.llm})
        data.chat(prompt)
