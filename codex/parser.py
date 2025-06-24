def parse_codex_entry(text):
    """Convert raw Codex text into structured data (e.g., title, tags, summary)."""
    lines = text.strip().split('\n')
    title = lines[0] if lines else "Untitled"
    summary = lines[1] if len(lines) > 1 else "No summary available."
    tags = [word.strip("#") for word in text.split() if word.startswith("#")]
    return {"title": title, "summary": summary, "tags": tags}
