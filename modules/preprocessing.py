# preprocessing.py (Input preprocessing and validation)
import yaml
import json

def load_config():
    with open("../config/settings.yaml", "r") as f:
        return yaml.safe_load(f)

def load_prompts():
    with open("../config/prompts.json", "r") as f:
        return json.load(f)