import json
import logging


class Descriptions():

    def __init__(self):
        file = open('card_data.json', "r")
        json_data = json.load(file)

        cards = json_data['cards']
        self.descriptions = dict()
        
        for card in cards:
            self.descriptions[card['name'].lower()] = card
        
        logging.info("Card descriptions loaded ")  

    def getDescription(self, card : str) -> str:
        return self.descriptions[card.lower()]