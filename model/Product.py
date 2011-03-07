class Product(object):
    #an object which holds all the information for a single product in a trade
    def __init__(self, name, quantity, buy, sell):
        self.__stats = {"quantity": quantity, "buy":buy, "sell":sell, "name":name}
    
    def __getitem__(self, index):
        return self.__stats[index]