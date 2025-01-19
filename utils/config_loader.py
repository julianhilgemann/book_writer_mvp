# config_loader.py (Loads and validates user configurations)
def validate_config(config):
    if "book_title" not in config or "chapters" not in config:
        raise ValueError("Invalid configuration file.")
    return config
