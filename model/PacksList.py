path_to_bot = ""
import sys
sys.path.append(path_to_bot + "model")
from List import *

class PacksList(List):
    def __init__(self):
        super(PacksList, self).__init__()
        buylist = ["SOM", "ZEN", "WWK", "ME4", "M11", "ROE"]
    
    def get_buy_list(self):
         #returns a prioritized list of packs wanted, starting with most wanted
        return self._buy_list
    
    def add_pack_to_have(self, packname, amount):
        self._have[packname] = amount