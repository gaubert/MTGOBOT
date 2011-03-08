path_to_bot = ""
import sys
sys.path.append(path_to_bot + "model")
import ProductPriceModel


class PackPricesDAL(object):
    #DAL layer for pricelist for buying and selling packs
    def __init__(self):
        price_model = ProductPriceModel.ProductPriceModel()
        self.buy = price_model.get_prices("packs_buy")
        self.sell = price_model.get_prices("packs_sell")
        
    #set prices is to be done in gui bot settings prior to transaction
    def set_buy_price(self, name, price):
        self.buy[name.upper()] = price
    def set_sell_price(self, name, price):
        self.sell[name.upper()] = price
    
    def get_buy_price(self, name):
        return self.buy[name.upper()]
    def get_sell_price(self, name):
        return self.sell[name.upper()]