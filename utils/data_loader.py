import json
import os

def load_json(file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(base_dir, "data", file_name)
    with open(file_path, encoding="utf-8") as f:
        return json.load(f)
