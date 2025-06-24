# codegen/self_coder.py
import openai
from codex.ingestion import load_codex_memory
from introspection.reflection_journal import record_reflection

def generate_code(prompt: str):
    context = load_codex_memory()
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": context},
                  {"role": "user", "content": prompt}]
    )
    code = response['choices'][0]['message']['content']
    record_reflection("Generated new code:\n" + code)
    return code
