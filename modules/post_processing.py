# post_processing.py (Formatting, refining, and assembly)
def format_book(chapters):
    return "\n\n".join([f"# {ch['title']}\n{ch['content']}" for ch in chapters])
