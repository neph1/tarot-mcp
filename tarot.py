import random

from card import Card
from descriptions import Descriptions

SUITS = [
    "Wands", 
    "Cups", 
    "Swords", 
    "Pentacles"
]

# Define the Rank Values (Order matters for shuffling/iteration)
RANKS = [
    "Ace", 
    "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
    "Page", "Knight", "Queen", "King"
]


MAJOR_ARCANA = [
    "The Fool",
    "The Magician",
    "The High Priestess",
    "The Empress",
    "The Emperor",
    "The Hierophant",
    "The Lovers",
    "The Chariot",
    "Strength",
    "The Hermit",
    "Wheel of Fortune",
    "Justice",
    "The Hanged Man",
    "Death",
    "Temperance",
    "The Devil",
    "The Tower",
    "The Star",
    "The Moon",
    "The Sun",
    "Judgement",
    "The World"
]

class Tarot():

    def __init__(self):
        self.minor_arcana = self._generate_minor_arcana()
        self.reset()
    
    def shuffle(self):
        random.shuffle(self.full_deck)

    def next_card(self) -> Card:
        return self.full_deck.pop()
    
    def next_position(self):
        return self.celtic_cross.pop(0)
    
    def _get_cards_for_suit(self, suit_name):
        suit_cards = []
        for rank in RANKS:
            card_name = f"{rank} of {suit_name}"
            suit_cards.append(card_name)
        return suit_cards

    def _generate_minor_arcana(self):
        all_cards = []
        for suit in SUITS:
            all_cards.extend(self._get_cards_for_suit(suit))
        return all_cards
    
    def reset(self):
        self.full_deck = []
        for card in MAJOR_ARCANA:
            self.full_deck.append(Card(card, random.randint(0, 1) == 1))
        for card in self.minor_arcana:
            self.full_deck.append(Card(card, random.randint(0, 1) == 1))


        self.shuffle()

        self.celtic_cross = [
            "1. Past Influences",
            "2. Cross Influences",
            "3. Crown",
            "4. The Recent Past",
            "5. The Present",
            "6. The Near Future",
            "7. Hopes and Fears",
            "8. Relationships",
            "9. Work, Environment",
            "10. Outcome"]
