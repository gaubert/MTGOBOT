class ImagesModel(object):
    #stores the all images to be used by bot into tuples
    #used as a library object, primarily by the interface object
    """returns the images to be used for pixel search"""
    
    #image of blank area
    __blank = "../Images/trade/blank.png"
    def get_blank(self):
        return self.__blank
    
    #image of the ok button, e.g. after completing a trade
    __ok_button = "../Images/ok_button.png"
    def get_ok_button(self):
        return self.__ok_button
        
    #stores image of a ticket
    __ticket =  "../Images/trade/get_ticket/ticket.png"
    def get_ticket(self):
        return self.__ticket
        
    #stores image of a ticket text
    __ticket_text = "../Images/product/misc/text/event_ticket_text.png"
    def get_ticket_text(self):
        return self.__ticket_text
        
    __amount = {1:"../Images/trade/context_menu/get_1.png", 4:"../Images/trade/context_menu/get_4.png", 10:"../Images/trade/context_menu/get_10.png", 32:"../Images/trade/context_menu/get_32.png"}
    def get_amount(self, amount):
        return self.__amount[amount]
        
    #store images of each number in a tuple
    #the image for numbers depend on the context, e.g. number images in the giving window are different from the ones in collection or taking_window
    __number = {"trade":{
    "preconfirm":{
    1: "../Images/numbers/trade/number_01.png", 2: "../Images/numbers/trade/number_02.png", 3: "../Images/numbers/trade/number_03.png", 4: "../Images/numbers/trade/number_04.png", 5: "../Images/numbers/trade/number_05.png",
    6: "../Images/numbers/trade/number_06.png", 7: "../Images/numbers/trade/number_07.png", 8: "../Images/numbers/trade/number_08.png", 9: "../Images/numbers/trade/number_09.png", 10: "../Images/numbers/trade/number_10.png", 11: "../Images/numbers/trade/number_11.png",
    12: "../Images/numbers/trade/number_12.png", 13: "../Images/numbers/trade/number_13.png", 14: "../Images/numbers/trade/number_14.png", 15: "../Images/numbers/trade/number_50.png", 16: "../Images/numbers/trade/number_16.png", 17: "../Images/numbers/trade/number_17.png",
    18: "../Images/numbers/trade/number_18.png", 19: "../Images/numbers/trade/number_19.png", 20: "../Images/numbers/trade/number_20.png"},
    "confirm":{
    1:"../Images/numbers/trade/confirm/number_01.png", 2:"../Images/numbers/trade/confirm/number_02.png", 3:"../Images/numbers/trade/confirm/number_03.png", 4:"../Images/numbers/trade/confirm/number_04.png", 5:"../Images/numbers/trade/confirm/number_05.png", 
    6:"../Images/numbers/trade/confirm/number_06.png", 7:"../Images/numbers/trade/confirm/number_07.png", 8:"../Images/numbers/trade/confirm/number_08.png", 9:"../Images/numbers/trade/confirm/number_09.png", 10:"../Images/numbers/trade/confirm/number_10.png", 
    11:"../Images/numbers/trade/confirm/number_11.png", 12:"../Images/numbers/trade/confirm/number_12.png", 13:"../Images/numbers/trade/confirm/number_13.png", 14:"../Images/numbers/trade/confirm/number_14.png", 15:"../Images/numbers/trade/confirm/number_15.png", 
    16:"../Images/numbers/trade/confirm/number_16.png", 17:"../Images/numbers/trade/confirm/number_17.png", 18:"../Images/numbers/trade/confirm/number_18.png", 19:"../Images/numbers/trade/confirm/number_19.png", 20:"../Images/numbers/trade/confirm/number_20.png",
    21:"../Images/numbers/trade/confirm/number_21.png", 22:"../Images/numbers/trade/confirm/number_22.png", 23:"../Images/numbers/trade/confirm/number_23.png", 24:"../Images/numbers/trade/confirm/number_24.png", 25:"../Images/numbers/trade/confirm/number_25.png", 
    26:"../Images/numbers/trade/confirm/number_26.png", 27:"../Images/numbers/trade/confirm/number_27.png", 28:"../Images/numbers/trade/confirm/number_28.png", 29:"../Images/numbers/trade/confirm/number_29.png", 30:"../Images/numbers/trade/confirm/number_30.png", 
    31:"../Images/numbers/trade/confirm/number_31.png", 32:"../Images/numbers/trade/confirm/number_32.png", 33:"../Images/numbers/trade/confirm/number_33.png", 34:"../Images/numbers/trade/confirm/number_34.png", 35:"../Images/numbers/trade/confirm/number_35.png",
    36:"../Images/numbers/trade/confirm/number_36.png", 37:"../Images/numbers/trade/confirm/number_37.png", 38:"../Images/numbers/trade/confirm/number_38.png", 39:"../Images/numbers/trade/confirm/number_39.png", 40:"../Images/numbers/trade/confirm/number_40.png",
    41:"../Images/numbers/trade/confirm/number_41.png", 42:"../Images/numbers/trade/confirm/number_42.png", 43:"../Images/numbers/trade/confirm/number_43.png", 44:"../Images/numbers/trade/confirm/number_44.png", 45:"../Images/numbers/trade/confirm/number_45.png", 
    46:"../Images/numbers/trade/confirm/number_46.png", 47:"../Images/numbers/trade/confirm/number_47.png", 48:"../Images/numbers/trade/confirm/number_48.png", 49:"../Images/numbers/trade/confirm/number_49.png", 50:"../Images/numbers/trade/confirm/number_50.png", 
    51:"../Images/numbers/trade/confirm/number_51.png", 52:"../Images/numbers/trade/confirm/number_52.png", 53:"../Images/numbers/trade/confirm/number_53.png", 54:"../Images/numbers/trade/confirm/number_54.png", 55:"../Images/numbers/trade/confirm/number_55.png",
    56:"../Images/numbers/trade/confirm/number_56.png", 57:"../Images/numbers/trade/confirm/number_57.png", 58:"../Images/numbers/trade/confirm/number_58.png", 59:"../Images/numbers/trade/confirm/number_59.png", 60:"../Images/numbers/trade/confirm/number_60.png",
    61:"../Images/numbers/trade/confirm/number_61.png", 62:"../Images/numbers/trade/confirm/number_62.png", 63:"../Images/numbers/trade/confirm/number_63.png", 64:"../Images/numbers/trade/confirm/number_64.png", 65:"../Images/numbers/trade/confirm/number_65.png", 
    66:"../Images/numbers/trade/confirm/number_66.png", 67:"../Images/numbers/trade/confirm/number_67.png", 68:"../Images/numbers/trade/confirm/number_68.png", 69:"../Images/numbers/trade/confirm/number_69.png", 70:"../Images/numbers/trade/confirm/number_70.png", 
    71:"../Images/numbers/trade/confirm/number_71.png", 72:"../Images/numbers/trade/confirm/number_72.png", 73:"../Images/numbers/trade/confirm/number_73.png", 74:"../Images/numbers/trade/confirm/number_74.png", 75:"../Images/numbers/trade/confirm/number_75.png",
    76:"../Images/numbers/trade/confirm/number_76.png", 77:"../Images/numbers/trade/confirm/number_77.png", 78:"../Images/numbers/trade/confirm/number_78.png", 79:"../Images/numbers/trade/confirm/number_79.png", 80:"../Images/numbers/trade/confirm/number_80.png",
    81:"../Images/numbers/trade/confirm/number_81.png", 82:"../Images/numbers/trade/confirm/number_82.png", 83:"../Images/numbers/trade/confirm/number_83.png", 84:"../Images/numbers/trade/confirm/number_84.png", 85:"../Images/numbers/trade/confirm/number_85.png", 
    86:"../Images/numbers/trade/confirm/number_86.png", 87:"../Images/numbers/trade/confirm/number_87.png", 88:"../Images/numbers/trade/confirm/number_88.png", 89:"../Images/numbers/trade/confirm/number_89.png", 90:"../Images/numbers/trade/confirm/number_90.png", 
    91:"../Images/numbers/trade/confirm/number_91.png", 92:"../Images/numbers/trade/confirm/number_92.png", 93:"../Images/numbers/trade/confirm/number_93.png", 94:"../Images/numbers/trade/confirm/number_94.png", 95:"../Images/numbers/trade/confirm/number_95.png",
    96:"../Images/numbers/trade/confirm/number_96.png", 97:"../Images/numbers/trade/confirm/number_97.png", 98:"../Images/numbers/trade/confirm/number_98.png", 99:"../Images/numbers/trade/confirm/number_99.png", 100:"../Images/numbers/trade/confirm/number_60.png",
    101:"../Images/numbers/trade/confirm/number_101.png", 102:"../Images/numbers/trade/confirm/number_102.png", 103:"../Images/numbers/trade/confirm/number_103.png", 104:"../Images/numbers/trade/confirm/number_104.png", 105:"../Images/numbers/trade/confirm/number_105.png", 
    106:"../Images/numbers/trade/confirm/number_106.png", 107:"../Images/numbers/trade/confirm/number_107.png", 108:"../Images/numbers/trade/confirm/number_108.png", 109:"../Images/numbers/trade/confirm/number_109.png", 110:"../Images/numbers/trade/confirm/number_110.png", 
    111:"../Images/numbers/trade/confirm/number_111.png", 112:"../Images/numbers/trade/confirm/number_112.png", 113:"../Images/numbers/trade/confirm/number_113.png", 114:"../Images/numbers/trade/confirm/number_114.png", 115:"../Images/numbers/trade/confirm/number_115.png"
    }}}
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
    __trade = {"confirm":{"confirm_button":"../Images/trade/confirm_window/confirm_button_confirm.png", "confirm_cancel":"../Images/trade/confirm_window/confirm_cancel.png", "cancel_button":"../Images/trade/confirm_window/cancel_button.png"}, "canceled_trade": "canceled_trade.png", "sort_name": "../Images/trade/sort_name.png", "list_view_collection_window":"../Images/trade/list_view_button_collection_window.png", "thumbnail_view_collection_window":"../Images/trade/thumbnail_view_button_collection_window.png", "confirm_button":"../Images/trade/confirm_button.png", "cancel_button":"../Images/trade/cancel_button.png", "incoming_request": "../Images/incoming_request.png", "accept_request": "../Images/trade_yes.png",  "turn_right": "../Images/turn_right.png", "turn_left": "../Images/turn_left.png", "version_menu":"../Images/trade/version_menu.png", "version_menu_regular":"../Images/trade/version_menu_regular.png", "version_menu_packs_tickets":"../Images/trade/version_menu_packs_tickets.png", "version_menu_premium":"../Images/trade/version_menu_premium.png", "giving_window":"../Images/trade/products_giving.png", "taking_window":"../Images/trade/products_taking.png", "scroll_bar_regular":"../Images/trade/scroll_bar_regular.png", "scroll_bar_mini":"../Images/trade/scroll_bar_mini.png"}
    def get_trade(self, filename, phase=None):
        if phase == None:
            return self.__trade[filename]
        else:
            return self.__trade[phase][filename]
            
    #stores the screencaps for chat window
    __chat = {"minimize":"../Images/chat/minimize_button.png", "expand_close":"../Images/chat/expand_close_button.png", "type_area":"../Images/chat/type_area.png", "buddies": "../Images/buddies_tab.png", 'my_cart': "../Images/my_cart_tab.png", 'games': "../Images/games_tab.png", 'card': "../Images/card_tab.png", 'text':{"done":"../Images/chat/text/done.png"}}
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
    #this is a list of all packs to buy and sell
    __packs_name_list = ["M11", "ME4", "MBS", "ROE", "SOM", "WWK", "ZEN"]
    
    __packs_images = {"M11":"../Images/product/packs/Magic2011.png", "M10":"../Images/product/packs/Magic2010.png", "10E":"../Images/product/packs/UrzasLegacy.png", "9ED":"../Images/product/packs/Magic9.png", "8ED":"../Images/product/packs/Magic8.png", "7ED":"../Images/product/packs/Magic7.png", "MBS": "../Images/product/packs/Besieged.png", "SOM":"../Images/product/packs/Scars.png", "ROE":"../Images/product/packs/RiseEldrazi.png", "WWK":"../Images/product/packs/Worldwake.png", "ZEN":"../Images/product/packs/Zendikar.png","UZS":"../Images/product/packs/UrzasSaga.png", "UZL":"../Images/product/packs/UrzasLegacy.png", "ARB":"../Images/product/packs/AlaraReborn.png", "CSP":"../Images/product/packs/Coldsnap.png", "CON":"../Images/product/packs/Conflux.png", "DIS":"../Images/product/packs/Dissension.png", "EXO":"../Images/product/packs/Exodus.png", "FUT":"../Images/product/packs/Future.png", "CHK":"../Images/product/packs/KamigawaChampions.png", "LEG":"../Images/product/packs/Legions.png", "LRW":"../Images/product/packs/Lorwyn.png", "MOR":"../Images/product/packs/Morningtide.png", "PLC":"../Images/product/packs/PlanarChaos.png", "ALA":"../Images/product/packs/ShardsAlara.png", "STH":"../Images/product/packs/Stronghold.png", "WTH":"../Images/product/packs/Weatherlight.png", "ME4":"../Images/product/packs/Masters4.png", "ME3":"../Images/product/packs/Masters3.png", "ME2":"../Images/product/packs/Masters2.png", "ME1":"../Images/product/packs/Masters1.png", "ALB":"../Images/product/packs/AlaraBlock.png"},
    __packs_text = {"preconfirm": {"M11":"../Images/product/packs/text/Magic2011.png", "M10":"../Images/product/packs/text/Magic2010.png", "10E":"../Images/product/packs/text/UrzasLegacy.png", "9ED":"../Images/product/packs/text/Magic9.png", "8ED":"../Images/product/packs/text/Magic8.png", "7ED":"../Images/product/packs/text/Magic7.png","MBS": "../Images/product/packs/text/Besieged.png", "SOM":"../Images/product/packs/text/Scars.png", "ZEN":"../Images/product/packs/text/Zendikar.png", "WWK":"../Images/product/packs/text/Worldwake.png", "ROE":"../Images/product/packs/text/RiseEldrazi.png", "UZS":"../Images/product/packs/text/UrzasSaga.png", "UZL":"../Images/product/packs/text/UrzasLegacy.png", "ARB":"../Images/product/packs/text/AlaraReborn.png", "CSP":"../Images/product/packs/text/Coldsnap.png", "CON":"../Images/product/packs/text/Conflux.png", "DIS":"../Images/product/packs/text/Dissension.png", "EXO":"../Images/product/packs/text/Exodus.png", "FUT":"../Images/product/packs/text/Future.png", "CHK":"../Images/product/packs/text/KamigawaChampions.png", "LEG":"../Images/product/packs/text/Legions.png", "LRW":"../Images/product/packs/text/Lorwyn.png", "MOR":"../Images/product/packs/text/Morningtide.png", "PLC":"../Images/product/packs/text/PlanarChaos.png", "ALA":"../Images/product/packs/text/ShardsAlara.png", "STH":"../Images/product/packs/text/Stronghold.png", "WTH":"../Images/product/packs/text/Weatherlight.png", "ME4":"../Images/product/packs/text/Masters4.png", "ME3":"../Images/product/packs/text/Masters3.png", "ME2":"../Images/product/packs/text/Masters2.png", "ME1":"../Images/product/packs/text/Masters1.png", "ALB":"../Images/product/packs/text/AlaraBlock.png"},
                    "confirm":{"M11":"../Images/product/packs/text/confirm/Magic2011.png", "ME4":"../Images/product/packs/text/confirm/Masters4.png", "ROE":"../Images/product/packs/text/confirm/RiseEldrazi.png", "MBS": "../Images/product/packs/text/confirm/Besieged.png", "SOM":"../Images/product/packs/text/confirm/Scars.png", "ZEN":"../Images/product/packs/text/confirm/Zendikar.png", "WWK":"../Images/product/packs/text/confirm/Worldwake.png"}}
    def get_pack_keys(self):
        return self.__packs_name_list
    def get_packs_text(self, phase, filename=None):
        if phase == "preconfirm":
            if filename:
                return self.__packs_text["preconfirm"][filename]
            else:
                return self.__packs_text["preconfirm"]
        elif phase == "confirm":
            if filename:
                return self.__packs_text["confirm"][filename]
            else:
                return self.__packs_text["confirm"]
        else:
            return None
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