from anki.loader import json_loader
from anki.loader import json_loader
from anki.db import Cards

import os

if __name__ == "__main__":
    cards_db = Cards()
    directory = './store/cache/'
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        data_list = json_loader(file_path)
        cards_db.insert_cards(data_list)
