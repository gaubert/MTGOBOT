
class CardPricesDAL(object):
    #DAL layer for pricelist for buying and selling single cards
    
    def __init__(self):
        price_model = ProductPriceModel()
        self.pack_buy = price_model.get_prices("cards_buy")
        self.pack_sell = price_model.get_prices("cards_sell")