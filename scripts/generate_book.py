# generate_book.py (Main script to generate a book)
from modules.chapter_generator import generate_chapter

def generate_book():
    config = load_config()
    chapters = []
    for chapter in config["chapters"]:
        content = generate_chapter(chapter["title"], chapter["blocks"])
        chapters.append({"title": chapter["title"], "content": content})
    book = format_book(chapters)
    with open("../data/output/book.txt", "w") as f:
        f.write(book)
    print("Book generated successfully.")