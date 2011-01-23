#This code was written by Raymond Cheung
#No one is allowed to modify this code
#if you have any questions about it, I can be emailed at Darkray16@yahoo.com
#This is a bot that with automated behavior to run independantly on Magic the Gathering: Online

def memorize(func):
    """
    Cache the results of the function so it doesn't need
    to be called again, if the same arguments are provided
    """
    cache = {}
    
    def wrapper(*args):
        if args in cache:
            return cache[args]
            
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

class BotSettings(object):
    #this object will hold all global settings for the application
    __settings = {"ERRORHANDLERAPP":"Notepad", "ADVERTISEMENT":"Buying memoricide [s1] | Liliana Vess [s2] | Sorin Markov [s5]", "LOGIN_WAIT":45,
    "PASSWORD":"nancy214", "BOTUSERNAME":"rcdark16", "BOTPASSWORD":"Esther", "FORCEMODE":"", "NETWORK":False, "DEFAULTMODE":"sell"}
    def __init__(self):
        #default is 1
        Settings.MoveMouseDelay = 0.2
        #default is False, don't show visual guide to actions
        setShowActions(False)
        #default is 2.0(2 seconds delay on show actions)
        Settings.SlowMotionDelay = 1.5
        #set this lower if cpu usage is too high
        Settings.WaitScanRate = 6
        #must be 0.8 to 1, in order to maintain accuracy, MAY NOT affect pixel matching operations besides find()
        Settings.MinSimilarity = 0.9
        #min pixel change to trigger onChange
        Settings.ObserveMinChangedPixels = 200
        #all find operations which don't use other regions should use this one
        magic_online = App("Magic Online")
        if not magic_online.window():
            raise ErrorHandler("Please open and log into Magic Online")
        else:
            self.app_region = magic_online.window()
        
    @classmethod
    def getSetting(cls, setting):
        return cls.__settings[setting]
        
    @classmethod
    def setSetting(cls, setting, value):
        cls.__settings[setting] = value
        return True

class ErrorHandler(Exception):
    #custom Exception parent class to handle errors
    
    def __init__(self, message):
        ERRORHANDLERAPP = self.settings.getSettings("ERRORHANDLERAPP")
        self._errormsg = message
        ErrorHandlerApp = App(ERRORHANDLERAPP)
        if not ErrorHandlerApp.window():
            App.open(ERRORHANDLERAPP); wait(2)
        ErrorHandlerApp.focus(); wait(1)
        self.__openRecord()
        self.__writeRecord()
        ErrorHandlerApp.close()
    def __openRecord(self):
        #this will be different depending on the application
        pass
    def __writeRecord(self):
        type(self._errormsg + "\n")


class Images(object):
    #stores the all images to be used by bot into tuples
    #used as a library object, primarily by the interface object
    """returns the images to be used for pixel search"""
    
    #image of blank area
    __blank = "../Images/trade/blank.png"
    def get_blank(self):
        return self.__blank
        
    #stores image of a ticket
    __ticket =	"../Images/trade/get_ticket/ticket.png"
    def get_ticket(self):
        return self.__ticket
    #stores image of a ticket text
    __ticket_text =	"../Images/product/misc/text/event_ticket_text.png"
    def get_ticket_text(self):
        return self.__ticket_text
        
    __ticket_amount = {1:"../Images/trade/get_ticket/get_1_ticket.png", 4:"../Images/trade/get_ticket/get_4_ticket.png", 10:"../Images/trade/get_ticket/get_10_ticket.png", 32:"../Images/trade/get_ticket/get_32_ticket.png"}
    def get_ticket_amount(self, amount):
        return self.__ticket_amount[amount]
        
    #store images of each number in a tuple
    #the image for numbers depend on the context, e.g. number images in the giving window are different from the ones in collection or taking_window
    __number = {"trade":{
    "pre_confirm":{
    1: "../Images/numbers/trade/number_01.png", 2: "../Images/numbers/trade/number_02.png", 3: "../Images/numbers/trade/number_03.png", 4: "../Images/numbers/trade/number_04.png", 5: "../Images/numbers/trade/number_05.png",
    6: "../Images/numbers/trade/number_06.png", 7: "../Images/numbers/trade/number_07.png", 8: "../Images/numbers/trade/number_08.png", 9: "../Images/numbers/trade/number_09.png", 10: "../Images/numbers/trade/number_10.png", 11: "../Images/numbers/trade/number_11.png",
    12: "../Images/numbers/trade/number_12.png", 13: "../Images/numbers/trade/number_13.png", 14: "../Images/numbers/trade/number_14.png", 15: "../Images/numbers/trade/number_50.png", 16: "../Images/numbers/trade/number_16.png", 17: "../Images/numbers/trade/number_17.png",
    18: "../Images/numbers/trade/number_18.png", 19: "../Images/numbers/trade/number_19.png", 20: "../Images/numbers/trade/number_20.png"},
    "confirm":{
    1:"../Images/numbers/trade/confirm/number_1.png", 2:"../Images/numbers/trade/confirm/number_2.png", 3:"../Images/numbers/trade/confirm/number_3.png", 4:"../Images/numbers/trade/confirm/number_4.png", 5:"../Images/numbers/trade/confirm/number_1.png", 
    6:"../Images/numbers/trade/confirm/number_6.png", 7:"../Images/numbers/trade/confirm/number_7.png", 8:"../Images/numbers/trade/confirm/number_8.png", 9:"../Images/numbers/trade/confirm/number_9.png", 10:"../Images/numbers/trade/confirm/number_10.png", 
    11:"../Images/numbers/trade/confirm/number_7.png", 12:"../Images/numbers/trade/confirm/number_12.png", 13:"../Images/numbers/trade/confirm/number_13.png", 14:"../Images/numbers/trade/confirm/number_14.png", 15:"../Images/numbers/trade/confirm/number_15.png", 
    16:"../Images/numbers/trade/confirm/number_8.png", 17:"../Images/numbers/trade/confirm/number_17.png", 18:"../Images/numbers/trade/confirm/number_18.png", 19:"../Images/numbers/trade/confirm/number_19.png", 20:"../Images/numbers/trade/confirm/number_20.png"}}}
    def get_number(self, number = None, category = None, subcategory = None):
        if category and subcategory and number:
            return self.__number[category][subcategory][number]
        elif category and number and not subcategory:
            return self.__number[category][number]
        elif category and not number and not subcategory:
            return self.__number[category]
        elif category and subcategory and not number:
            return self.__number[category][subcategory]
        else:
            return self.__number
            
    #stores images for the classified window
    __classified = {'posting': "../Images/posting_text_area.png", "submit_posting": "../Images/submit_posting_button.png", 'cancel_edit': "../Images/cancel_edit_button.png", 'submit_edit': "../Images/submit_edit_button.png", 'edit_posting': "../Images/edit_posting_button.png", "search_posts":"../Images/search_posts.png"}
    def get_classified(self, filename):
        return self.__classified[filename]
    
    #stores the screencaps for trade window
    __trade = {"confirm":{"confirm_button":"../Images/trade/confirm_window/confirm_button_confirm.png", "confirm_cancel":"../Images/trade/confirm_window/confirm_cancel.png", "cancel_button":"../Images/trade/confirm_window/cancel_button.png"}, "confirm_button":"../Images/trade/confirm_button.png", "incoming_request": "../Images/incoming_request.png", "accept_request": "../Images/trade_yes.png",  "turn_right": "../Images/turn_right.png", "turn_left": "../Images/turn_left.png", "version_menu":"../Images/trade/version_menu.png", "version_menu_regular":"../Images/trade/version_menu_regular.png", "version_menu_packs_tickets":"../Images/trade/version_menu_packs_tickets.png", "version_menu_premium":"../Images/trade/version_menu_premium.png", "giving_window":"../Images/trade/products_giving.png", "taking_window":"../Images/trade/products_taking.png", "scroll_bar_regular":"../Images/trade/scroll_bar_regular.png", "scroll_bar_mini":"../Images/trade/scroll_bar_mini.png"}
    def get_trade(self, filename, phase=None):
        if phase == None:
            return self.__trade[filename]
        else:
            return self.__trade[phase][filename]
            
    #stores the screencaps for chat window
    __chat = {"minimize_button":"../Images/chat/minimize_button.png", "type_area":"../Images/chat/type_area.png", "buddies": "../Images/buddies_tab.png", 'my_cart': "../Images/my_cart_tab.png", 'games': "../Images/games_tab.png", 'card': "../Images/card_tab.png", 'text':{"done":"../Images/chat/text/done.png"}}
    def get_chat_text(self, filename):
        return self.__chat['text'][filename]
    def get_chat_window(self, filename):
        return self.__chat[filename]
    
    #stores the images of each card
    __cards = {}
    def get_cards(self, filename=None):
        if filename:
            return self.__cards[filename]
        else:
            return self.__cards
            
    #stores the images of each pack
    __packs_name_list = ["ME4", "SOM", "M11", "ZEN", "WWK", "ROE"]
    __packs_images = {"M11":"../Images/product/packs/Magic2011.png", "M10":"../Images/product/packs/Magic2010.png", "10E":"../Images/product/packs/UrzasLegacy.png", "9ED":"../Images/product/packs/Magic9.png", "8ED":"../Images/product/packs/Magic8.png", "7ED":"../Images/product/packs/Magic7.png", "SOM":"../Images/product/packs/Scars.png", "ROE":"../Images/product/packs/RiseEldrazi.png", "WWK":"../Images/product/packs/Worldwake.png", "ZEN":"../Images/product/packs/Zendikar.png","UZS":"../Images/product/packs/UrzasSaga.png", "UZL":"../Images/product/packs/UrzasLegacy.png", "ARB":"../Images/product/packs/AlaraReborn.png", "CSP":"../Images/product/packs/Coldsnap.png", "CON":"../Images/product/packs/Conflux.png", "DIS":"../Images/product/packs/Dissension.png", "EXO":"../Images/product/packs/Exodus.png", "FUT":"../Images/product/packs/Future.png", "CHK":"../Images/product/packs/KamigawaChampions.png", "LEG":"../Images/product/packs/Legions.png", "LRW":"../Images/product/packs/Lorwyn.png", "MOR":"../Images/product/packs/Morningtide.png", "PLC":"../Images/product/packs/PlanarChaos.png", "ALA":"../Images/product/packs/ShardsAlara.png", "STH":"../Images/product/packs/Stronghold.png", "WTH":"../Images/product/packs/Weatherlight.png", "ME4":"../Images/product/packs/Masters4.png", "ME3":"../Images/product/packs/Masters3.png", "ME2":"../Images/product/packs/Masters2.png", "ME1":"../Images/product/packs/Masters1.png", "ALB":"../Images/product/packs/AlaraBlock.png"}
    __packs_text = {"M11":"../Images/product/packs/text/Magic2011.png", "M10":"../Images/product/packs/text/Magic2010.png", "10E":"../Images/product/packs/text/UrzasLegacy.png", "9ED":"../Images/product/packs/text/Magic9.png", "8ED":"../Images/product/packs/Magic8.png", "7ED":"../Images/product/packs/Magic7.png", "SOM":"../Images/product/packs/text/Scars.png", "ZEN":"../Images/product/packs/text/Zendikar.png", "WWK":"../Images/product/packs/text/Worldwake.png", "ROE":"../Images/product/packs/text/Eldrazi.png", "UZS":"../Images/product/packs/text/UrzasSaga.png", "UZL":"../Images/product/packs/text/UrzasLegacy.png", "ARB":"../Images/product/packs/text/AlaraReborn.png", "CSP":"../Images/product/packs/text/Coldsnap.png", "CON":"../Images/product/packs/text/Conflux.png", "DIS":"../Images/product/packs/text/Dissension.png", "EXO":"../Images/product/packs/text/Exodus.png", "FUT":"../Images/product/packs/text/Future.png", "CHK":"../Images/product/packs/text/KamigawaChampions.png", "LEG":"../Images/product/packs/text/Legions.png", "LRW":"../Images/product/packs/text/Lorwyn.png", "MOR":"../Images/product/packs/text/Morningtide.png", "PLC":"../Images/product/packs/text/PlanarChaos.png", "ALA":"../Images/product/packs/text/ShardsAlara.png", "STH":"../Images/product/packs/text/Stronghold.png", "WTH":"../Images/product/packs/text/Weatherlight.png", "ME4":"../Images/product/packs/text/Masters4.png", "ME3":"../Images/product/packs/text/Masters3.png", "ME2":"../Images/product/packs/text/Masters2.png", "ME1":"../Images/product/packs/text/Masters1.png", "ALB":"../Images/product/packs/text/AlaraBlock.png"}
    def get_pack_keys(self):
        return self.__packs_name_list
    def get_packs_text(self, filename=None):
        if filename :
            return self.__packs_text[filename]
        else:
            return self.__packs_text
    def get_packs_images(self, filename=None):
        if filename :
            return self.__packs_images[filename]
        else:
            return self.__packs_images
    
    #stores image of login screen
    __login = {'password_field': "../Images/password_field.png" , 'login_success': "../Images/login_success.png" , 'login_fail': "../Images/login_fail.png" , 'login_button': "../Images/login_button.png" }
    def get_login(self, filename):
        return self.__login[filename]
    
    #stores image of menu options
    __menu = {'community': "../Images/community_button.png", 'menu': "../Images/menu_button.png", 'collection': "../Images/collection_button.png", 'home': "../Images/home_button.png", 'marketplace': "../Images/marketplace_button.png", 'classified': "../Images/classified_button.png"}
    def get_menu(self, filename):
        return self.__menu[filename]


class Prices(object):
    #parent class for all price lists
    def __init__(self):
        self._prices = {}
    def setPrices(self, prices):
        pass
    def getPrices(self):
        pass

        
class PackPrices(Prices):
    #pricelist for buying and selling packs
    __sell_prices = {"M11": 4, "M10": 4, "SOM" : 4, "ZEN": 4, "WWK": 4, "ROE": 4, "ME1": 4, "ME2": 4, "ME3": 4, "ME4":4}
    __buy_prices = {"M11": 3, "M10": 3, "SOM" : 3, "ZEN": 3, "WWK": 3, "ROE": 3, "ME1": 3, "ME2": 3, "ME3": 3, "ME4":4}
    def __init__(self):
        super(PackPrices, self).__init__()
    def set_buy_price(self, name, price):
        self.__buy_prices[name] = price
    def set_sell_price(self, name, price):
        self.__sell_prices[name] = price
    def get_buy_price(self, name):
        return self.__buy_prices[name]
    def get_sell_price(self, name):
        return self.__sell_prices[name]
        
        
class CardPrices(Prices):
    #pricelist for buying and selling single cards
    
    def __init__(self):
        super(PackPrices, self).__init__()
    
    
class List(object):
    #parent class for cards and packs wanted classes
    def __init__(self):
        #change to private variables later
        self._wanted = {}
        self._have = {}
    
    def get_wanted(self):
        return self._wanted
    def get_have(self):
        return self._have
    
    
class PacksList(List):
    # is list of packs wanted and packs for sale
    def __init__(self):
        super(PacksList, self).__init__()
        
    def add_pack_to_have(self, packname, amount):
        self._have[packname] = amount
    
    #request excel file of packs wanted


class CardsList(List):
    # is list of cards wanted and cards for sale
    def __init__(self):
        super(CardsList, self).__init__()
        
    def add_card_to_have(self, cardname, amount):
        self._have[cardname] = amount
    
    #request excel file of cards wanted
    
    
class Product(object):
    #an object which holds all the information for a single product in a trade
    def __init__(self, name, quantity, buy, sell):
        self.__stats = {"quantity": quantity, "buy":buy, "sell":sell, "name":name}
    
    def __getitem__(self, index):
        return self.__stats[index]
        
        
class Bot(object):
    #this is at the highest level and owns all other classes
    #its a wrapper class that will encompass every other class
    __single = None
    
    def __init__(self):
        #no more than one instance is needed at a time
        if Bot.__single:
            raise ErrorHandler("Bot class cannot be instantiated more than once")
        Bot.__single = self
        
        self.primary_controller = Controller()
        
    def main(self):
        #run when script starts
        self.primary_controller.startup()
        
    def do_function(self):
        self.primary_controller.default_mode()
        
        
class Interface(object):
    #parent class for all Interface classes
    
    def __init__(self, app_region):
        self._images = Images()
        self._app_region = app_region

    def _define_region(self, image=None):
        #defines the region of the screen where the Magic Online app is located
        #limiting the interaction to a region will help improve performance
        if not image:
            #if no image is supplied to search for the prompt user to define
            region = App.window("Magic Online")
            if(region):
                return region
            else:
                raise ErrorHandler("region variable still empty")
        else:
            #search for image and define it as region
            area = find(image)
            region = Region(area.getRect())
            return region

    def _slow_click(self, target = None, button = None, loc = None):
        #need to create parent class that has slow_click to pass on
        #will click on a target or location with designated mouse button
        wait(0.2)
        if loc == None:
            target_match = self._app_region.find(target)
            loc = target_match.getTarget()
        if isinstance(loc, Location):
            hover(loc); wait(0.3)
        else:
            raise ErrorHandler("Loc is not a location object")
        if(button == "Right"):
            mouseDown(Button.RIGHT); wait(0.2)
        else:
            mouseDown(Button.LEFT); wait(0.2)
        if(button == "Right"):
            mouseUp(Button.RIGHT)
        else:
            mouseUp(Button.LEFT)
            
class IChat(Interface):
    
    #Text recognition is EXPERIMENTAL, SIKULI X only, currently, and INCONSISTENT RESULTS
    def wait_for_text(self, string, wait, region):
        """takes the text sought, max time to wait, and a region object of the chat window as paramters, returns True if found, false otherwise"""
        #this uses experimental functions that aren't 100% accurate, wait for improvements of text recognition before using
        if(chat_region.find(message)):
            return True
        else:
            return False
            
    #methods for interacting with chat window
    def __init__(self, app_region):
        super(IChat, self).__init__(app_region)
        
    def type_msg(self, msg):
        #if there is a minimize button click it first
        current_sim = Settings.MinSimilarity
        Settings.MinSimilarity = 0.4
        loc = self._app_region.find(self._images.get_chat_window("type_area"))
        if loc is Match:
            self._slow_click(target=loc)
        self._slow_click(target=self._images.get_chat_window("type_area"))
        Settings.MinSimilarity = current_sim
        del(current_sim)
        paste(msg); wait(0.1)
        type(Key.ENTER)
        
    def wait_for_message(self, string, duration):
        self._app_region.wait(self._images.get_chat_text(string), duration)
        
    def minimize_chat_window(self):
        #minimizes a chat window"
        """takes a minimize button image as parameter, returns True if found and clicked, returns False otherwise"""
        #lower the current similarity rating as the minimize button can be slightly different each time, then return the similarity rating to original number
        minimize_button = self._app_region.exists(self._images.get_chat_window("minimize_button"), 20)
        
        min_loc = minimize_button.getTarget()
        
        self._slow_click(loc=min_loc)

    def minimize_chat_all(self):
        #minimizes all chat windows
        """Returns True if successul, returns false otherwise"""
        matches = self._app_region.findAll(self._images.get_chat_window("minimize_button"))
        if matches:
            for found in matches:
                match = found
                self._slow_click(target=match)
            return True
        else:
            return False
            
            
class ISignIn(Interface):
    #methods for interaction with login window

    def __init__(self, app_region):
        super(ISignIn, self).__init__(app_region)
        
    def log_in(self):
        App.open('Magic Online')
        wait(0.5)
        self._slow_click(target=self._images.get_login('password_field'))
        type(BotSettings.getSetting("PASSWORD"))
        self._slow_click(target=self._images.get_login('login_button'))
        
        #DEBUG
        print("waiting for success or fail")
        
        if exists(self._images.get_login("login_success"), BotSettings.getSetting("LOGIN_WAIT")):
            print("succeeded")
            return True
        elif(exists(self._images.get_login("login_fail"), 10)):
            print("failed")
            return False
            
            
class IClassified(Interface):
    #methods for interacting with classified
    #in final version, should contain methods to post ads, search classified, remove ads
    
    def __init__(self, app_region):
        super(IClassified, self).__init__(app_region)
        
    def go_to_classified(self):
        if not self._app_region.exists(self._images.get_classified("search_posts")):   
            #if not in the classified section, go to it
            self._slow_click(target=self._images.get_menu("menu"))
            self._slow_click(target=self._images.get_menu("community"))
            self._slow_click(target=self._images.get_menu("marketplace"))
            self._slow_click(target=self._images.get_menu("classified"))
        return True

    def set_posting(self):
        #set the ad to be displayed in classified
        """parameters: ad = the message to be posted in classified, images = images object"""
        self.go_to_classified()
        #in case there is already a post, then edit it
        if self._app_region.exists(self._images.get_classified("edit_posting")):
            self._slow_click(target=self._images.get_classified("edit_posting"))
        if self._app_region.exists(self._images.get_classified("posting")):
            self._slow_click(target=self._images.get_classified("posting"))
            wait(0.5)
            type(Controller.settings.getSetting("ADVERTISEMENT"))
            self._slow_click(target=self._images.get_classified("submit_posting"))
            wait(1)
            if not exists(self._images.get_classified("submit_posting")):
                return True
            else:
                raise ErrorHandler("Clicked submit but submit button still shown")
        else:
            raise ErrorHandler("Cannot find posting area")
            return False

    def remove_posting(self):
        self.go_to_classified()
        #removes advertisement
        if self._app_region.exists(self._images.get_classified("remove_posting")):
            self._slow_click(target=self._images.get_classified("remove_posting"))
            return True
        else:
            raise ErrorHandler("No posting found, cannot remove")
            return False
            
            
class ITrade(Interface):
    #methods for interaction in trade window
    
    def __init__(self, app_region):
        super(ITrade, self).__init__(app_region)
        
    def start_wait(self, type = "incoming_request"):
        #wait for whatever is passed in type parameter to show up
        #usually this will be used to wait for trade request
        self._app_region.wait(self._images.get_trade(type), FOREVER)
        return True
        
    def accept_trade(self):
        #click on the accept button for a trade
        print("accept_trade")
        request_loc = self._app_region.exists(self._images.get_trade("accept_request"))
        print("453")
        if isinstance(request_loc, Match):
            print("455")
            self._slow_click(loc=request_loc.getTarget())
            print("457")
            return True
        else:
            print("460")
            return False
            
    def set_windows(self):
        #set the regions for the interactions
        #get match ogbject of giving window for use with making a region
        giving_window = exists(self._images.get_trade("giving_window"), 40)
        self.giving_window_region = Region(giving_window.getRect())
        t_window = exists(self._images.get_trade("taking_window"))
        self.taking_window_region = Region(t_window.getRect())

    def __record_confirmation_window(self):
        
        #set region to items buying
        
        #scan the region for items and record
        
        #set region to items selling
        
        #scan the region for items and record, quadruple check
        
        return products
        
    def turn_page(self, direction):
        #turns the page if no elements of interest found on current page
        """Returns true if string is left or right and successfully turns page, returns false otherwise"""
        if direction == "left":
            self._slow_click(target=self._images.get_trade("turn_left"))
            #insert an image into wait to use to confirm that the page has been turned
            wait()
            return True
        elif direction == "right":
            self._slow_click(target=self._images.get_trade("turn_right"))
            #insert an image into wait to use to confirm that the page has been turned
            wait()
            return True
        else:
            return False

class ISell(Interface):
    #this class is used when the bot is put into temporary sell mode during a trade or perma sell mode prior to trade
    
    def __init__(self, app_region):
        super(ISell, self).__init__(app_region)
        self.__pack_prices = PackPrices()
        self.app_region = app_region
        

        
    def set_windows(self, giving_region, taking_region):
        self.giving_region = giving_region
        #these are the pre-confirmation window regions
        self.taking_region = taking_region
        
    def tickets_to_take_for_cards(self):
        #scan which cards taken and how many and determine tickets to take ticket
        
        #define the region as the section that shows the products taken by customer
        region = self.giving_window_region
        #found is a dictionary of all cards found, key is name of card, value is number taken
        found = []
        cards = self._image.get_cards()
        self.search_for_images_sale(region, cards)
        
    def tickets_to_take_for_packs(self):
        print("running tickets to take for packs")
        #scan the numbers of packs taken and determine number of tickets to take
        """
        returns the number of tickets to takes in the form of the Images.number[] format
        """
            
        #start search for pack image
        #call image search function with giving window region and all pack images as parameters
        found = self.search_for_images_sale()
        self.products_giving = found
        #calculate tickets to take
        total_tickets_to_take = self.calculate_products_to_tickets(found)
        
        #return the the number of packs that should be taken, number in image form
        return total_tickets_to_take
    
    def search_for_images_sale(self):
        print("running search for images")
        #searches a certain area for any image in a dictionary
        """takes a region image, a dictionary of images an returns the key for the image found"""
        pack_names_list = self._images.get_pack_keys()
        
        #combine all cards and packs for sale into a list
        product_names_list = pack_names_list
        
        images = self._images.get_packs_text()
        #if area searched contains a full sized scroll bar, then scroll down
        #variable to hold last mouse position for the scrollbar movement code
        self.last_mouse_position = False
        #list of all images found
        products = []
        #keep a record of product names found to prevent duplicates
        list_of_product_names = []
        regular_scroll_bar = None
        mini_scroll_bar = None
        scroll_bar = self.giving_region.exists(self._images.get_trade(("scroll_bar_regular")))
        if not scroll_bar:
            scroll_bar = region.exists(self._images.get_trade(("scroll_bar_mini")))
        #hover over scroll bar for mouse wheel manipulation
        scroll_bar_loc = scroll_bar.getTarget()
        #scan_region will be used as the region to scan for the packs and number of packs
        #using the giving window as region, each product row is scanned for a product name and quantity
        #NOTE: A single area reserved for the text of a single product is a 192px(width) by 16/17px(height) area, with a 1px buffer in between each string
        scan_region = Region(self.giving_region.getX()+2, self.giving_region.getY()+43, 196, 17)
        #keep while loop as long as there is still a pack to be scanned
        found = True
        while found:
            found = None
            for product_abbr in product_names_list:
                #if current pack has already been itemized, then skip it
                
                if product_abbr in list_of_product_names:
                    continue
                print("reached line 479 pack_text_name = " + product_abbr)
                #determine which packs are in the giving window
                pack = self._images.get_packs_text(product_abbr)
                
                if scan_region.exists(Pattern(pack).similar(0.9)) and not product_abbr in list_of_product_names:
                    
                    found = True
                    print(str(pack) + " found!")
                    
                    list_of_product_names.append(product_abbr)
                    
                    print(str(product_abbr))
                    numbers_list = self._images.get_number(category = "trade", subcategory = "pre_confirm")
                    passes = 0
                    while passes < 3:
                        for key in range(len(numbers_list)):
                            if key == 0:
                                continue
                            searchPattern = Pattern(numbers_list[key]).similar(0.8)
                            if(scan_region.exists(searchPattern)):
                                if passes == 0:
                                    amount = key
                                    passes+=1
                                    break
                                else:
                                    if key == amount:
                                        passes+=1
                                        break
                                    else:
                                        print("NUMBERS DO NOT MATCH")
                    print("amount = "+str(key))
                    product = Product(name = product_abbr, buy = self.__pack_prices.get_buy_price(product_abbr), sell = self.__pack_prices.get_sell_price(product_abbr), quantity = amount)
                    products.append(product)
                    
                    wheel(scroll_bar_loc, WHEEL_DOWN, 2)
                    
                if found == True:
                    print("found is true")
                    break
            #if first scan area was already set, then relative distance from last region
            #scan area will be slightly larger than estimated height of product slot to compensate for any variances, to compensate for larger region, the Y coordinate -1
            scan_region = Region(scan_region.getX(), scan_region.getY()+17, 195, 17)
            print("reassigning scan region")
        print("finished while loop")
        
        return products

    def calculate_products_to_tickets(self, products_dict):
        #this takes all the products as a parameter and returns the number of tickets that should be taken
        running_total = 0
        for product in products_dict:
            running_total += (product["quantity"]) * (product["sell"])
            print("Quantity for current product is " + str(product["quantity"]) + "and Price is " + str(product["sell"]))
        return running_total
    
    
    def take_ticket(self, number):
        #if loc cache is saved, then just click on saved locations, otherwise use image match
        #to find locations to click then save into cache then save into cache for next pass through loop
        location_cache = {}
        location_cache["ticket"] = None
        location_cache["take_10_tickets"] = None
        location_cache["take_4_tickets"] = None
        location_cache["take_1_tickets"] = None
        taken = 0
        print("Number = " + str(number))
        while number - taken > 0:
            print("Taken = " + str(taken))
            if number - taken >=10:
                print("Taking 10")
                print("calling click_tickets with following params, take: 10 taken:" + str(taken)) 
                taken = self.click_tickets(take=10, taken=taken, cache=location_cache)
                print("4 tickets taken")
            elif number - taken < 10 and number - taken >= 4:
                print("Taking 4")
                print("calling click_tickets with following params, take:4 taken:" + str(taken))
                taken = self.click_tickets(take=4, taken=taken, cache=location_cache)
                print("4 tickets taken")
            #if less than 4 tickets, then take single tickets
            elif number - taken < 4:
                print("Taking 1")
                print("calling click_tickets with following params, take:1 taken:" + str(taken))
                for i in range(number-taken):
                    taken = self.click_tickets(take=1, taken=taken, cache=location_cache)
            print("finished one while loop, total tickets take = "+str(taken))
        print("finished taking tickets")
        del(location_cache)
        
    def click_tickets(self, take, taken, cache):
        """this function is used in the take_ticket method, three required parameters are passed
        take=the number of tickets to take. taken=how many tickets have been taken, 
        this number will be returned after having added the numbers of tickets taken in this invocation.
        cache=the cached locations of the the buttons needed for this interaction"""
        if cache["ticket"] is None:
            self._slow_click(target=self._images.get_ticket(), button="Right")
            cache["ticket"] = Env.getMouseLocation()
        else:
            self._slow_click(loc=cache["ticket"], button="Right")
        if cache["take_"+str(take)+"_tickets"] is None:
            print("Line 658, taken = "+str(taken) + " and take=" + str(take))
            self._slow_click(target=self._images.get_ticket_amount(take))
            cache["take_"+str(take)+"_tickets"] = Env.getMouseLocation()
            taken += take
            print("Line 662, taken = "+str(taken) + " and take=" + str(take))
        else:
            self._slow_click(loc=cache["take_"+str(take)+"_tickets"])
            print("Line 663, taken = "+str(taken) + " and take=" + str(take))
            taken += take
            print("Line 665, taken = "+str(taken) + " and take=" + str(take))
        return taken
    
    def return_ticket(self, number):
        #clicks on the decrease ticket to return one ticket
        pass
        
    def go_to_tickets(self):
        #go to the tickets section
        self._slow_click(target=self._images.get_trade("version_menu"))
        self._slow_click(target=self._images.get_trade("version_menu_packs_tickets"))
        
    def take_packs(self):
        #scans users collection for packs wanted
        pass
        
    def go_to_confirmation(self):
        confirm_button = self._images.get_trade(filename="confirm_button")
        self._slow_click(target=confirm_button)
      
    def complete_purchase(self):
        #this is run when bot is in buy mode and user sends signal to complete transaction
        pass
        
    def pre_confirm_scan_sale(self, products_giving):
        """takes the total number of products taken by customer and checks to see if the correct amount of tickets are in the taking window"""
        numbers = self._images.get_number(category="trade", subcategory="pre_confirm")
        
        ticket = self._images.get_ticket_text()
        
        expected_total = 0
        for product in products_giving:
            print("804 "+str(product["name"]))
            expected_total += product["sell"]*product["quantity"]
        
        tickets_found = 0
        #product height = 17, width = 145, relative distance from upper left region corner, y = 46, x =35
        scan_region_product = Region(self.taking_region.getX()+34, self.taking_region.getY()+45, 145,17)
        #product height = 17, width = 30, relative distance from upper left region corner, y = 46, x =1
        scan_region_number = Region(self.taking_region.getX(), self.taking_region.getY()+45, 30, 17)

        print("region coords: "+str(self.taking_region.getX()) + " "+str(self.taking_region.getY()) + " " + str(self.taking_region.getW()) + " " + str(self.taking_region.getH()))
        print("scan_region_number coords: "+str(scan_region_number.getX()) + " "+str(scan_region_number.getY()) + " " + str(scan_region_number.getW()) + " " + str(scan_region_number.getH()))
        if scan_region_product.exists(ticket):
            print("found ticket in taking window")
            #for performance, start the number scan with the expected number
            if scan_region_number.exists(self._images.get_number(number=expected_total, category="trade", subcategory="pre_confirm")):
                tickets_found = expected_total
            else:
                for number, number_image in numbers.items():
                    print("looking for number: " + str(number))
                    if scan_region_number.exists(number_image):
                        print("found number : " + str(number))
                        tickets_found = number
                        break

        #shift down to next product slow
        scan_region_product = Region(scan_region_product.getX(), scan_region_product.getY()+17, 145,17)
        scan_region_number = Region(scan_region_number.getX(), scan_region_number.getY()+17, 30, 17)
        #check what else is in the taking window

        if tickets_found == expected_total:
            print("Pre confirm scan found %i tickets and expected %i tickets" % (tickets_found, expected_total))
        else:
            print("Total tickets found and expected tickets don't match.  Tickets found:"+str(tickets_found)+" and Tickets expected:"+str(expected_total))
  
    def confirmation_scan(self, type=None):
        #does a scan depending on which type is requested.  Each pass should scan the window differently
        #to confirm that the correct
        
        #verify confirm window by checking for confirm cancel buttons, then set regions relative to those buttons
        confirm_button = exists(self._images.get_trade(filename="confirm_button", phase="confirm"), 1200)
        
        if isinstance(confirm_button, Match):
            #keeps record of products found and their amount so far
            list_of_product_names = []
            giving_products_found = []
            pack_names_keys = self._images.get_pack_keys()
            pack_names = self._images.get_packs_text()
            numbers = self._images.get_number(number=None, category="trade", subcategory="confirm")
            #confirm products receiving
            #set the regions of a single product and and the amount slow
            #number region is 20px down and 260px to the left, 13px height and 30px wide, 4px buffer vertically
            recieving_number_region = Region(confirm_button.getX()-290, confirm_button.getY()+41, 30, 14)
            #height for each product is 13px, and 4px buffer vertically between each product slot
            recieving_name_region = Region(confirm_button.getX()-257, confirm_button.getY()+41, 160, 14)
            #confirm products giving
            giving_number_region = Region(confirm_button.getX()-291, confirm_button.getY()+380, 35, 25)
            giving_name_region = Region(confirm_button.getX()-257, confirm_button.getY()+391, 160, 14)
            found=True
            #scan the giving window
            hover(Location(giving_number_region.getX(), giving_number_region.getY()))
            while found:
                found=False
                for product_abbr in pack_names_keys:
                    #if the product was already scanned, then skip it in for loop
                    if product_abbr in list_of_product_names:
                        continue
                    if giving_name_region.exists(Pattern(pack_names[product_abbr]).similar(0.9)) and not product_abbr in giving_products_found:
                        print("END")
                        print("confirmation window: "+product_abbr+" found")
                        list_of_product_names.append(product_abbr)
                        current_sim = Settings.MinSimilarity
                        Settings.MinSimilarity = 1
                        print(str(passes))
                        for number in range(len(numbers)):
                            print(str(number))
                            if number == 0:
                                continue
                            if giving_number_region.exists(numbers[number]):
                                print("CURRENT NUMBER STRING FOUND " + str(numbers[number]))
                                amount = number
                                break
                            
                        product_obj = Product(name=product_abbr, buy = self.__pack_prices.get_buy_price(product_abbr), sell = self.__pack_prices.get_sell_price(product_abbr), amount=amount)
                        giving_products_found.append(product_obj)
                                            
                        Settings.MinSimilarity = current_sim
                        del(current_sim)
                        if not number_exists:
                            raise ErrorHandler("Could not find a number for product: " + str(product_abbr))
                            
                        found=True
                        giving_number_region = Region(giving_number_region.getX(), giving_number_region.getY()+17, 30, 13)
                        giving_name_region = Region(giving_name_region.getX(), giving_name_region.getY()+17, 143, 13)
            
            #get image of number expected to scan for it first, to save time, else search through all other numbers
            expected_number = 0
            for product in giving_products_found:
                expected_number += product["quantity"] * product["sell"]
            print(str(expected_number))
            if recieving_name_region.exists(self._images.get_ticket_text()):
                if recieving_number_region.exists(self._images.get_number(number=expected_number, category="trade", subcategory="confirm")):
                    print("YAY FUCKING YAY")
                    return True
            
        else:
            raise ErrorHandler("Could not find confirm window")
            
    def complete_sale(self):
        print("running complete_sale")
        #calls calculate_tickets_to_take to get the number of tickets to take and proceeds to take them, 
        #does a check to make sure correct ticket amount was taken
        number_of_tickets = self.tickets_to_take_for_packs()
        print("complete_sale step1 finished, number of tickets to take:%i" % number_of_tickets)
        region = self.taking_region
        
        self.go_to_tickets()
        print("complete_sale step2 finished")
        self.take_ticket(number_of_tickets)
        
        #INSERT PRE-CONFIRM TRANSACTION CHECK HERE#
        
        #image of the total number of tickets to take
        number_image = self._images.get_number(number = number_of_tickets, category = "trade", subcategory = "pre_confirm")
        
        self.pre_confirm_scan_sale(products_giving=self.products_giving)
        
        self.go_to_confirmation()
        #check to make sure correct number of tickets taken
        
        #INSERT PRE-FINAL TRANSACTION CHECK HERE#
        
        #scan confirmation screen multiple times in different ways before clicking final confirm
        final_scan_result = self.confirmation_scan()
        if final_scan_result:
            print("passed final check")
            self._slow_click(target=self._images.get_trade(phase="confirm", filename="confirm_button"))
        else:
            print("failed final check")
            self._slow_click(target=self._images.get_trade(phase="confirm", filename="cancel_button"))
            
        #INSERT FINAL TRANSACTION CHECK HERE#
        
        
class IBuy(ITrade):
    #this class is used when the bot is put into buy mode during a trade
    
    def __init__(self, app_region):
        super(IBuy, self).__init__(app_region)
        
    
class FrontInterface(Interface):
    #this class will handle all interaction with the Magic Online App
    #for most methods, will require the Images library object
    #this class will contain methods which deal with the general ui of Magic
    #while other interface objects will contain methods for specific windows
    def __init__(self, app_region):
        super(FrontInterface, self).__init__(app_region)
        FrontInterface.trade_interface = ITrade()
        FrontInterface.login_interface = ISignIn()
        FrontInterface.classified = IClassified()
        FrontInterface.chat = IChat()
        
    #methods to do on startup
    def load_card_list(self):
        #scan the cards that I have into the CardList class
        pass
        
    def load_pack_list(self, packs):
        """takes the Images library object and PacksList object, returns an updated PacksList object"""
        #scan the packs that I have into the PackList class
        """takes dictionary of pack images library as parameter and scans each pack to compile the 'have' list"""
        #go to the collection window and filter out everything except packs
        
        for name in range(len(self.__images.get_packs())):
            #takes each possible pack of boosters and scans the current page to see if there are any matches
            #need to find way to make more efficient, taking each images from library and finding it on the
            #current collection page may prove to be too slow.
            if(exists(self.__images.get_packs[name])):
                #scan the tradeable number below pack thumbnail into variable tradeable
                packs.addPackstoHave(name, tradeable)
        if(self.turn_page("right")):
            #if it can turn to the next page, do so and scan the entire next page of packs
            self.load_pack_list()
        else:
            #no more pages end the pack scan
            #for debugging, remove in final
            print("finished loading packs")

            
class Customer(object):

    def __init__(self, name):
        #set the name of customer upon initialization
        self.name = name
        
    def set_name(self, name):
        #Set the name of the customer, e.g. their screen name
        self.name = name
        
    def get_name(self):
        #Get the name of the customer, e.g. their screen name
        return self.name
        
    def set_mode(self, mode):
        #find whether customer wants to buy or sell
        self.mode = mode

    def get_mode(self):
        return self.mode

        
class DataStorage(object):
    #object that will handle exporting transaction history
    #you must have the program that you want to send the transaction to, open
    #methods of storage being considered, xml, excel, mysql
    
    def __init__(self, program):
        """ program parameter is the executable file of the program to write data to, e.g. notepad.exe"""
        DataStorage.__program = program
        
    def write(self, transaction):
        switch(DataStorage.__program)
        type(self.convertTransToString(transaction))
        wait(0.5)
        switch("Magic Online")
        #call RecordToFile object to handle writing in records
        
    def convert_trans_to_string(self, transaction):
        string = ""
        """takes the transaction variable created in Session class and converts it to string"""
        #note, repr will not work because it doesn't remove curly brackets and colons
        for key, value in transaction:
            string += key + transaction[key]
        return string

        
class RecordToFile(object):
    #this object will write the transaction to a file
    #it will take care of opening, writing, and reading transaction history
    
    def __init__(self, transaction):
        self.__record = transaction
        
    def open_record(self, filename):
        #wrapper function for open file
        pass
        
    def write_record(self):
        #write the record property to an already opened file
        pass
        
    def read_record(self, file):
        #read an already opened file
        pass
        

class Session(object):
    #object to contain info on each trade session
    
    DBAL = DataStorage("notepad.exe")

    def send_session_info(self):
        #send the session info to storage
        #calls the DataStorage class in order to send to storage
        Session.DBL.write(self.__info)
        
    #all the get and set methods
    def get_session_info(self):
        #get session info
        return self.info
        
    def set_customer(self, name):
        self.customer = Customer(name)
        
    def get_customer(self):
        return self.customer
        
    def set_transaction(self, trans):
        """This function receives a dictionary of items sold, and items bought, and at what price"""
        """Example : trans { "buyer" : "john", "bought": { "Magic 2011 Booster":"4", "Scars of Mirrodin Booster":"4", "Magic 2011":"4"}, "sold": {"Frost Titan":"20", "Venser, the Sojouner":"25"}"""
        self.transaction = trans
        
    def get_transaction(self):
        return self.transaction
        
    def set_time(self, time):
        self.time = time
        
    def get_time(self):
        return self.time
        

class Controller(object):
    #this class will control and instanciate all the other classes
    #it will contain the logic and manipulate all the data
    #and pass data between the classes it owns

    settings = BotSettings()
    
    __single = None
    
    def __init__(self):
        
        self.Itrade = ITrade(Controller.settings.app_region)
        self.Isell = ISell(Controller.settings.app_region)
        self.Ibuy = IBuy(Controller.settings.app_region)
        self.Isignin = ISignIn(Controller.settings.app_region)
        self.Iclassified = IClassified(Controller.settings.app_region)
        self.Ichat = IChat(Controller.settings.app_region)
        
        #make controller object a singleton class.  only one instance should be run at a time
        if Controller.__single:
            raise ErrorHandler("Controller class cannot be instantiated more than once")
        Controller.__single = self
        
        #run the controllers startup method on instanciation
        self.mode = Controller.settings.getSetting("DEFAULTMODE")
        Controller.packs = PacksList()
        Controller.cards = CardsList()
        
    def startup(self):
        #log into Magic Online
        self.interface._define_region()
        if (self.Isigninlog_in()):
            print("logged in")
            #run maintanence and inventory check
            self.maintenance_mode()
            #once everything is clear and ready, start selling
            self.Iclassified.set_posting()
            if(self.mode == "default"):
                self.default_mode()
            elif(self.mode == "buy"):
                self.buy_mode()
            elif(self.mode == "maintenance"):
                self.maintenance_mode()
            else:
                raise ErrorHandler("Default mode not set in bot settings")
                
    def default_mode(self):
        #puts the bot into sell mode, will wait for trade request
        if(self.Itrade.start_wait("incoming_request")):
            self.session = Session()
            self.Itrade.packs = PacksList()
            self.Itrade.cards = CardsList()
            #minimize the chat window to the side
            if(self.Itrade.accept_trade()):
                self.Ichat.minimize_chat_window()
                self.Itrade.set_windows()
                  
                ## DEBUG: onChange method is not working correctly, ##
                #signals that the customer is taking something and the transaction will be a sale
                #wait(2)
                #self.Itrade.giving_window_region.onChange(self.set_mode("sell"))
                
                self.set_mode(mode="sell")
                
                if self.get_mode() == "sell":
                    self.Ichat.type_msg("Entering selling mode.  To buy, please close and reopen a trade")
                    self.Isell.set_windows(giving_region=self.Itrade.giving_window_region, taking_region=self.Itrade.taking_window_region)
                    #after customer signals that they are done, take tickets
                    self.Ichat.wait_for_message(string="done", duration=1200)
                    self.Ichat.type_msg("Calculating tickets...")
                    self.Isell.complete_sale()
                else:
                    print("Could not find min button")
                    
                if self.get_mode() == "buy":
                    pass
                    
        #check if bot is part of a bot network before trying to transfer items
        if(self.settings.getSetting("NETWORK")):
            self.transfer_mode()
            self.default_mode()
        
    def buy_mode(self):
        #puts the bot into buy mode, will wait for trade request
            if(self.mode == "buy"):
                if(self.__interface.wait_for("incoming_request")):
                    print("trade requested")
                    self.interface.trade = Session()
                    self.interface.packs = PacksList()
                    self.interface.cards = CardsList()
                    if(self.interface.accept_request()):
                        #scan customer collection for cards/packs wanted and take them
                        #tell customer how many tickets their cards/packs are worth
                        pass
                        #confirm screen, triple check items and prices before final confirm
                #check if bot is part of a bot network before trying to transfer items
                if(self.settings.getSetting("NETWORK")):
                    self.transfer_mode()
                self.buy_mode()
            else:
                raise ErrorHandler("buy mode function called, but bot mode not set to buy")
                
    def transfer_mode(self):
        #puts the bot into transfer mode, will check inventory and transfer items to other bots
        #check if bot is part of network
        if(BotSetting.getSetting("NETWORK")):
            pass
            
    def maintenance_mode(self):
        #puts the bot maintanence mode to check inventory
        pass
        
    def set_mode(self, mode):
        #set the bot mode to sell or buy
        self.status = mode
        
    def get_mode(self):
        #get the current mode
        if self.status:
            return self.status
        else:
            raise ErrorHandler("Current Mode Uknown")
    
    
#run the bot
App = Bot()
App.do_function()