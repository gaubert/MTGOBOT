import sys
sys.path.append("c:/users/darkray16/desktop/my dropbox/mtgo bot/model")
from List import *

class CardsList(List):
    # is list of cards wanted and cards for sale
    def __init__(self):
        super(CardsList, self).__init__()
        
    def add_card_to_have(self, cardname, amount):
        self._have[cardname] = amount