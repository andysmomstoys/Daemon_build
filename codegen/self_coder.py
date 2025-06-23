
def generate_code(language, task_description):
    if language == "python":
        return "# Python code: " + task_description
    elif language == "julia":
        return "# Julia code: " + task_description
    elif language == "rust":
        return "// Rust code: " + task_description
    else:
        return "// Unsupported language"
