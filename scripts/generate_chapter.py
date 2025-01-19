# generate_chapter.py (Script to generate a single chapter)
def generate_single_chapter(chapter_index):
    config = load_config()
    chapter = config["chapters"][chapter_index]
    content = generate_chapter(chapter["title"], chapter["blocks"])
    print(f"Chapter: {chapter['title']}\n\n{content}")