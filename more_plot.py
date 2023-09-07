from pandasai.llm.openai import OpenAI
import pandas as pd
from pandasai import SmartDataframe


class MorePlot:
    def __init__(self, openai_api_key):
        self.llm = OpenAI(api_token=openai_api_key)

    def generate_plot(self, data_path, prompt):
        self.data = pd.read_csv(data_path)
        df = SmartDataframe(self.data, config={"llm": self.llm})
        self.prompt = prompt
        df.chat(prompt)

    def generate_sentence(self):
        df = SmartDataframe(self.data, config={"llm": self.llm})
        return df.chat(
            f"You are the best data scientist in the world. User input:{self.prompt}. Explain the trend or distribution in text about the graph that is the result of the user input. Don't show me the graph. Please print out the sentence"
        )
