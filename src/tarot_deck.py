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
        with open('config.yml', 'r') as file:
            self.prompts = yaml.safe_load(file)