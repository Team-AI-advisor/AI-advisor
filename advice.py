import openai


class ChatGpt:
    def __init__(self, openai_api_key):
        openai.api_key = openai_api_key
        self.model = "gpt-3.5-turbo"

    def generate_advice(self, prompt, question):
        messages = [
            {"role": "system", "content": prompt},
            {"role": "user", "content": question},
        ]
        response = openai.ChatCompletion.create(model=self.model, messages=messages)
        return response["choices"][0]["message"]["content"]
