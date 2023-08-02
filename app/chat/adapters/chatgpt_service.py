import os

import openai


class ChatService:
    def __init__(self, api_key):
        self.api_key = os.getenv("OPENAI_API_KEY")
        openai.api_key = api_key

    def get_response(self, prompt):
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.2,
        )

        return completion.choices[0].message
