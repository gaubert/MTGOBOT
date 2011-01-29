#password to MTGO account
PASSWORD = "nancy214"
#how long to wait for login process, depends on internet connection
LOGIN_WAIT = 45
#ad to post in the classified section

ADVERTISEMENT = "Buying memoricide [s1] | Liliana Vess [s2] | Sorin Markov [s5]"
#class hierarchy:
#               (top level)
#                   Bot-----(errorhandler)
#                    |  
#  (packprices)      |
#       |            |    
#       |            |   
#  (packslist)--(controller)--(cardslist)--(cardprices)
#                   /|\             
#                  / | \             
#                 /  | (interface)---------------------------(classified)
#            (image) |                \         \         \
#                (session)             \         \         \
#                   /\                (chat)     (login)  (trade)
#                  /  \
#                 /    \
#                /      \
#         (customer) (datastorage)
#                           |
#                           |
#                    (write-to-file)


class ErrorHandler(Exception):
    #custom Exception class to handle errors
    #ErrorHandler, during transactions, should send record of transaction
    #and cancel trade to ensure no mistakes are made
    pass

class Images:
    #stores the all images to be used by bot into tuples
    #used as a library object, primarily by the interface object
    """returns the images to be used for pixel search"""
    
    #stores image of a ticket
    __ticket =  "../Images/ticket.png"
    def get_ticket(self):
        return self.__ticket
    
    #store images of each number in a tuple
    __number = ()
    def get_number(self, filename):
        return self.__number[filename]
    
    #stores images for the classified window
    __classified = {'posting': "../Images/posting_text_area.png", "submit_posting": "../Images/submit_posting_button.png", 'cancel_edit': "../Images/cancel_edit_button.png", 'submit_edit': "../Images/submit_edit_button.png", 'edit_posting': "../Images/edit_posting_button.png"}
    def get_classified(self, filename):
        return self.__classified[filename]
    
    #stores the screencaps for trade window
    __trade = {"incoming_request": "../Images/incoming_request.png", "accept_request": "../Images/trade_yes.png",  "turn_right": "../Images/turn_right.png", "turn_left": "../Images/turn_left.png", 'filter': {} }
    def get_trade(self, filename):
        return self.__trade[filename]
    
    #stores the screencaps for chat window
    __chat = {'buddies': "../Images/buddies_tab.png", 'my_cart': "../Images/my_cart_tab.png", 'games': "../Images/games_tab.png", 'card': "../Images/card_tab.png"}
    def get_chat(self, filename):
        return self.__chat[filename]
    
    #stores the images of each card
    __cards = {}
    def get_cards(self, filename):
        if filename:
            return self.__cards[filename]
        else:
            return self.__cards
            
    #stores the images of each pack
    __packs = {}
    def get_packs(self, filename):
        if filename :
            return self.__packs[filename]
        else:
            return self.__packs
            
    #stores image of login screen
    __login = {'password_field': "../Images/password_field.png" , 'login_success': "../Images/login_success.png" , 'login_fail': "../Images/login_fail.png" , 'login_button': "../Images/login_button.png" }
    def get_login(self, filename):
        return self.__login[filename]
    
    #stores image of menu options
    __menu = {'community': "../Images/community_button.png", 'menu': "../Images/menu_button.png", 'collection': "../Images/collection_button.png", 'home': "../Images/home_button.png", 'marketplace': "../Images/marketplace_button.png", 'classified': "../Images/classified_button.png"}
    def get_menu(self, filename):
        return self.__menu[filename]

class Prices:
    #parent class for all price lists
    def __init__(self)
    
class PackPrices(Prices):
    #pricelist for buying and selling packs
    
    def __init__(self):
        self.__prices = {}
    def setPrices(self, prices):
        pass
    def getPrices(self):
        return self.__prices
    
class CardPrices(Prices):
    #pricelist for buying and selling single cards
    
    def __init__(self):
        self.__prices = {}
    def setPrices(self, prices):
        pass
    def getPrices(self):
        return self.__prices
    
class List:
    #parent class for cards and packs wanted classes
    __wanted = {}
    __have = {}
    
    def get_wanted(self):
        return self.__wanted
    def get_have(self):
        return self.__have
	
class PacksList(List):
    # is list of packs wanted and packs for sale
    
    def add_pack_to_have(self, packname, amount):
        self.__have[packname] = amount
    
    #request excel file of packs wanted
class CardsList(List):
    # is list of cards wanted and cards for sale
    
    def add_card_to_have(self, cardname, amount):
        self.__have[cardname] = amount
    
    #request excel file of cards wanted
    
class Bot:
    #this is at the highest level and owns all other classes
    #its a wrapper class that will encompass every other class
    
    def __init__(self):
        #initialize instance variables
        self.__primary_controller = Controller()
    def main(self):
        #run when script starts
        self.__primary_controller.startup()
    def do_function(self):
        self.__primary_controller.post_ad()
        
class Interface(object):
    #parent class for all Interface classes
    
    def __init__(self):
        #change this to self.__images = Images()
        self.images = Images()

    def define_region(self):
        #defines the region of the screen where the Magic Online app is located
        #limiting the interaction to a region will help improve performance
        self.__region = selectRegion("Draw a rectangle around the App")
        if(self.__region):
            return True
        else:
            return False

    def slow_click(self, target):
        #need to create parent class that has slow_click to pass on
        #does a slower click down and release to ensure app registers it
        wait(1)
        hover(target)
        wait(0.5)
        mouseDown(Button.LEFT)
        wait(0.3)
        mouseUp(Button.LEFT)

class ISignIn(Interface):
    #methods for interaction with login window
    global PASSWORD
    global LOGIN_WAIT

    def __init__(self):
        super(ISignIn, self).__init__()
        #remove the below line
        self.__images = self.images
    def log_in(self):
    	switchApp('Magic Online')
    	wait(0.5)
        self.slow_click(self.__images.get_login('password_field'))
    	type(PASSWORD)
        self.slow_click(self.__images.get_login('login_button'))
        print("waiting for success or fail")
    	if(exists(self.__images.get_login("login_success"), LOGIN_WAIT)):
    	    print("succeeded")
    	    return True
    	elif(exists(self.__images.get_login("login_fail"), 10)):
    	    print("failed")
            return False
class IClassified(Interface):
    #methods for interacting with classified
    #in final version, should contain methods to post ads, search classified, remove ads
    global ADVERTISEMENT
    
    def __init__(self):
        super(IClassified, self).__init__()
        #remove the below line
        self.__images = self.images
    def set_posting(self):
        #set the ad to be displayed in classified
        """parameters: ad = the message to be posted in classified, images = images object"""

        #in case there is already a post, then edit it
        if(exists(self.images.get_classified("edit_posting"))):
            self.slow_click(self.images.get_classified("edit_posting"))
        if(exists(self.images.get_classified("posting"))):
            self.slow_click(self.images.get_classified("posting"))
            wait(0.5)
            type(ADVERTISEMENT)
            self.slow_click(self.images.get_classified("submit_posting"))
            wait(1)
            if(not exists(self.images.get_classified("submit_posting"))):
                return True
            else:
                raise ErrorHandler("Clicked submit but submit button still shown")
        else:
            raise ErrorHandler("Cannot find posting area")
            return False
    def remove_posting(self):
        #removes advertisement
        if(exists(self.images.get_classified("remove_posting"))):
            self.slow_click(self.images.get_classified("remove_posting"))
            return True
        else:
            raise ErrorHandler("No posting found, cannot remove")
            return False
class ITrade(Interface):
    #methods for interaction in trade window
    
    def __init__(self):
        super(ITrade, self).__init__()
        #remove the below line
        self.__images = self.images
    def start_wait(self, type = "incoming_request"):
        #wait for whatever is passed in type parameter to show up
        #usually this will be used to wait for trade request
        wait(self.images.get_trade(type), FOREVER)
        return True
    def accept_trade(self):
        #click on the accept button for a trade
        if(self.images.get_trade("accept_request")):
            self.slow_click(self.images.get_trade("accept_request"))
            return True
        else:
            raise Error
    def record_confirmation_window(self):
        
        #set region to items buying
        
        #scan the region for items and record
        
        #set region to items selling
        
        #scan the region for items and record, quadruple check
        
        return products
    def turn_page(self, direction):
        #turns the page if no elements of interest found on current page
        """Returns true if string is left or right and successfully turns page, returns false otherwise"""
        if(direction == "left"):
            self.slow_click(self.images.get_trade("turn_left"))
            #insert an image into wait to use to confirm that the page has been turned
            wait()
            return True
        elif(direction == "right"):
            self.slow_click(self.images.get_trade("turn_right"))
            #insert an image into wait to use to confirm that the page has been turned
            wait()
            return True
        else:
            return False

class FrontInterface(Interface):
    #this class will handle all interaction with the Magic Online App
    #for most methods, will require the Images library object
    #this class will contain methods which deal with the general ui of Magic
    #while other interface objects will contain methods for specific windows
    def __init__(self):
        super(FrontInterface, self).__init__()
        #remove the below line
        self.__images = self.images
        FrontInterface.__trade_interface = ITrade()
        FrontInterface.__login_interface = ISignIn()
        FrontInterface.__classified = IClassified()
        
    #methods to do on startup
    def load_card_list(self):
	    #scan the cards that I have into the CardList class
        pass
    def load_pack_list(self, packs):
        """takes the Images library object and PacksList object, returns an updated PacksList object"""
        #scan the packs that I have into the PackList class
        """takes dictionary of pack images library as parameter and scans each pack to compile the 'have' list"""
        #go to the collection window and filter out everything except packs
        
        for name in range(len(self.images.get_packs())):
            #takes each possible pack of boosters and scans the current page to see if there are any matches
            #need to find way to make more efficient, taking each images from library and finding it on the
            #current collection page may prove to be too slow.
            if(exists(self.images.get_packs[name])):
                #scan the tradeable number below pack thumbnail into variable tradeable
                packs.addPackstoHave(name, tradeable)
        if(self.turn_page("right")):
            #if it can turn to the next page, do so and scan the entire next page of packs
            self.load_pack_list()
        else:
            #no more pages end the pack scan
            #for debugging, remove in final
            print("finished loading packs")

    def log_in(self):
    	#switch to Magic Online app and log into account
    	"""function returns true if it can log into account, returns false otherwise"""
        if(FrontInterface.__login_interface.log_in()):
            return True
        else:
            return False
        
    def wait_for(self, type = "incoming_request"):
        #wait for visual element, default is to wait for a trade request
        if(FrontInterface.__trade_interface.start_wait()):
            return True
    def accept_request(self):
        #accept a trade request
        if(FrontInterface.__trade_interface.accept_trade()):
            return True
        else:
            return False
    def post_ad(self):
        #post an ad to the classified using IClassified object
        self.slow_click(self.images.get_menu("menu"))
        self.slow_click(self.images.get_menu("community"))
        self.slow_click(self.images.get_menu("marketplace"))
        self.slow_click(self.images.get_menu("classified"))
        if(FrontInterface.__classified.set_posting()):
            return True
        else:
            return False
class Customer:
    def __init__(self, name):
        #set the name of customer upon initialization
        self.__name = name
    def set_name(self, name):
        #Set the name of the customer, e.g. their screen name
        self.__name = name
    def get_name(self):
        #Get the name of the customer, e.g. their screen name
        return self.__name
    def set_mode(self, mode):
        #find whether customer wants to buy or sell
        self.__mode = mode
    def get_mode(self):
        return self.__mode

class DataStorage:
    #object that will handle exporting transaction history
    #you must have the program that you want to send the transaction to, open
    #methods of storage being considered, xml, excel, mysql
    
    def __init__(self, program):
        """ program parameter is the executable file of the program to write data to, e.g. notepad.exe"""
        DataStorage.__program = program
    def write(self, transaction):
        switch(DataStorage.__program)
        type(self.ConvertTransToString(transaction))
        wait(0.5)
        switch("Magic Online")
    def convert_trans_to_string(self, transaction):
        string = ""
        """takes the transaction variable created in Session class and converts it to string"""
        #note, repr will not work because it doesn't remove curly brackets and colons
        for key in range(len(transaction)):
            string += key + transaction[key]
        return string

class RecordToFile:
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

class Session:
    #object to contain info on each trade session
    
    __DBAL = DataStorage("notepad.exe")

    def send_session_info(self):
        #send the session info to storage
        #calls the DataStorage class in order to send to storage
        Session.__DBL.write(self.__info)
    #all the get and set methods
    def get_session_info(self):
        #get session info
        return self.__info
    def set_customer(self, name):
        self.__customer = Customer(name)
    def get_customer(self):
        return self.__customer
    def set_transaction(self, trans):
        """This function receives a dictionary of items sold, and items bought, and at what price"""
        """Example : trans { "buyer" : "john", "bought": { "Magic 2011 Booster":"4", "Scars of Mirrodin Booster":"4", "Magic 2011":"4"}, "sold": {"Frost Titan":"20", "Venser, the Sojouner":"25"}"""
        self.__transaction = trans
    def get_transaction(self):
        return self.__transaction
    def set_time(self, time):
        self.__time = time
    def get_time(self):
        return self.__time

class Controller:
    #this class will control and instanciate all the other classes
    #it will contain the logic and manipulate all the data
    #and pass data between the classes it owns
    
    #initialize class variables and objects, properties that won't be changing throughout app
    __interface = FrontInterface()
    
    def __init__(self):
        #run the controllers startup method on instanciation
        self.status = "default"
    
    def startup(self):
        #log into Magic Online
        Controller.__interface.define_region()
        if (Controller.__interface.log_in()):
            print("logged in")
            if(Controller.__interface.post_ad()):
                print("ad posted")
            if(Controller.__interface.wait_for("incoming_request")):
                print("trade requested")
                Controller.__interface.trade = Session()
                Controller.__interface.packs = PacksList()
                Controller.__interface.cards = CardsList()
                if(Controller.__interface.accept_request()):
                    print("now trading...")
    
    def setMode(self, mode):
        #set the bot mode to sell or buy
        controller.__status = mode
    def getMode(self):
        #get the current mode
        if self.__status:
            return self.__status
        else:
            raise ErrorHandler("Current Mode Uknown")
    def turn_page(self, direction):
        #turns the page if no elements of interest found on current page
        """Returns true if string is left or right and successfully turns page, returns false otherwise"""
        if(direction == "left"):
            slow_click(Bot.images.get_trade("turn_left"))
            #confirm page turned
            wait()
            return True
        elif(direction == "right"):
            slow_click(Bot.images.get_trade("turn_right"))
            #confirm page turned
            wait()
            return True
        else:
            return False
    def post_ad(self):
        self.__interface.post_ad()
    def load_card_list(self):
        #scan the cards that I have into the CardList class
        pass
    def load_pack_list(self, packs):
        #scan the packs that I have into the PackList class
        """takes dictionary of pack images library as parameter and scans each pack to compile the 'have' list"""
        #go to the collection window and filter out everything except packs
        
        for name in range(len(packs)):
            if(exists(pack[name])):
                #scan the tradeable number below pack thumbnail into variable tradeable
                self.packs.addPackstoHave(name, tradeable)
        if(self.turn_page("right")):
            self.load_pack_list()
        else:
            #for debugging, remove in final
            print("finished loading packs")

    
    
#run the bot
App = Bot()
App.main()