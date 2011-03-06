#handles reading and writing to files

from sys import *

class ProductPriceModel(object):
    
    def __init__(self):
        
        self.pricelist = {}
        try:
            self.pricelist["packs_buy"] = open("c:/users/darkray16/desktop/my dropbox/mtgo bot/pricelist/packs/buy.txt", "r")
        except IOError:
            sys.exit("Pack buy price file not found at pricelist/packs/buy/")
        try:
            self.pricelist["packs_sell"] = open("c:/users/darkray16/desktop/my dropbox/mtgo bot/pricelist/packs/sell.txt", "r")
        except IOError:
            sys.exit("Pack sell price file not found at pricelist/packs/sell/")
        try:
            self.pricelist["cards_buy"] = open("c:/users/darkray16/desktop/my dropbox/mtgo bot/pricelist/cards/buy.txt", "r")
        except IOError:
            sys.exit("Card buy price file not found at pricelist/packs/buy/")
        try:
            self.pricelist["cards_sell"] = open("c:/users/darkray16/desktop/my dropbox/mtgo bot/pricelist/cards/sell.txt", "r")
        except IOError:
            sys.exit("Card sell price file not found at pricelist/packs/buy/")
    
    def get_prices(self, pricelist):
        """valid strings for pricelist = "packs_buy", "packs_sell", "cards_buy", "cards_sell" """
        #this will return a dictionary containg all the buy or sell prices for requested products
        
        pricelist_dict = {}
        
        raw_feed = self.pricelist[pricelist]
        
        while True:
            newline = raw_feed.readline()
            if newline == "/n" or newline == "":
               break
            single_product = newline.split(" $")
            try:
                int(single_product[1])
            except ValueError:
                sys.exit("A non-number found as a price for " + single_product[0] + " in in response to a " + pricelist + " request")
                
            pricelist_dict[single_product[0]] = int(single_product[1])
        
        return pricelist_dict