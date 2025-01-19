# generate_block.py (Script to generate a single block)
def generate_single_block(chapter_index, block_index):
    config = load_config()
    block = config["chapters"][chapter_index]["blocks"][block_index]
    content = generate_block(block["description"], block["word_count"])
    print(f"Block: {block['description']}\n\n{content}")