#handles reading and writing to pricelist files
path_to_bot = ""

from sys import *

class ProductPriceModel(object):
    
    def __init__(self):
        
        self.pricelist_files = {}
        try:
            self.pricelist_files["packs_buy"] = open(path_to_bot + "pricelist/packs/buy.txt", "r")
        except IOError:
            print("Pack buy price file not found at pricelist/packs/buy/")
        try:
            self.pricelist_files["packs_sell"] = open(path_to_bot + "pricelist/packs/sell.txt", "r")
        except IOError:
            print("Pack sell price file not found at pricelist/packs/sell/")
        try:
            self.pricelist_files["cards_buy"] = open(path_to_bot + "pricelist/cards/buy.txt", "r")
        except IOError:
            print("Card buy price file not found at pricelist/cards/buy/")
        try:
            self.pricelist_files["cards_sell"] = open(path_to_bot + "pricelist/cards/sell.txt", "r")
        except IOError:
            print("Card sell price file not found at pricelist/cards/buy/")
    
    def get_prices(self, pricelist):
        """valid strings for pricelist = "packs_buy", "packs_sell", "cards_buy", "cards_sell" """
        #this will return a dictionary containg all the buy or sell prices for requested products
        
        pricelist_dict = {}
        
        raw_feed = self.pricelist_files[pricelist]
        
        while True:
            newline = raw_feed.readline()
            if newline == "/n" or newline == "":
               break
            single_product = newline.split(" $")
            try:
                int(single_product[1])
            except ValueError:
                sys.exit("A non-number found as a price for " + single_product[0] + " in in response to a " + pricelist + " request")
            product_name = str(single_product[0])
            
            #if there is no price next to the name of the product, then 
            try:
                product_price = int(single_product[1])
            except IndexError:
                pass
            except ValueError:
                pass
            else:
                pricelist_dict[product_name.upper()] = product_price
        
        pricelist_dict["Rack"] = 15
        return pricelist_dict