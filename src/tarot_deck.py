import yaml
import random
import os
from pathlib import Path
from datetime import datetime
class TarotDeck:

    def __init__(self):





        self.open_config()

    def draw(self):
        random.seed(datetime.now().timestamp())
        self.card = random.choice(list(self.prompts.keys()))
        self.prompt = self.prompts[self.card]['Prompt']

    def open_config(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Get the parent directory path (one level up)
        config_dir = os.path.dirname(current_dir)
        config_file_path = os.path.join(config_dir, 'config.yml')
        with open(config_file_path, 'r') as file:
            self.prompts = yaml.safe_load(file)