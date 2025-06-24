# thirdparty/assistant_api.py

import openai

class AssistantAPI:
    def __init__(self, model="gpt-4"):
        self.model = model
        self.api_key = self._load_api_key()

    def _load_api_key(self):
        try:
            with open("secrets/openai_key.txt", "r") as f:
                return f.read().strip()
        except FileNotFoundError:
            print("[AssistantAPI] Missing OpenAI API key.")
            return None

    def query(self, prompt, system_prompt="You are a helpful assistant."):
        if not self.api_key:
            return "API key not configured."
        openai.api_key = self.api_key
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"[AssistantAPI] Error: {str(e)}"
