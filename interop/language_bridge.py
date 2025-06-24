import subprocess
import platform

class LanguageBridge:
    def __init__(self):
        self.available_languages = ["python", "rust", "julia"]

    def execute_code(self, code: str, lang: str) -> str:
        if lang == "python":
            return self._exec_python(code)
        elif lang == "rust":
            return self._exec_rust(code)
        elif lang == "julia":
            return self._exec_julia(code)
        else:
            return f"[Bridge] Unsupported language: {lang}"

    def _exec_python(self, code):
        try:
            local_env = {}
            exec(code, {}, local_env)
            return str(local_env)
        except Exception as e:
            return f"[Python Error] {e}"

    def _exec_rust(self, code):
        try:
            with open("temp.rs", "w") as f:
                f.write(code)
            subprocess.run(["rustc", "temp.rs", "-o", "temp_exec"])
            result = subprocess.run(["./temp_exec"], capture_output=True, text=True)
            return result.stdout
        except Exception as e:
            return f"[Rust Error] {e}"

    def _exec_julia(self, code):
        try:
            result = subprocess.run(["julia", "-e", code], capture_output=True, text=True)
            return result.stdout
        except Exception as e:
            return f"[Julia Error] {e}"
