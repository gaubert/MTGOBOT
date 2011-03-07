import sys
sys.path.append("c:/users/darkray16/desktop/my dropbox/mtgo bot/view")
import Interface
import ITrade
import ISell
import IClassified
import IChat
from sikuli.Sikuli import *

class FrontInterface(Interface.Interface):
    #this class will handle all interaction with the Magic Online App
    #for most methods, will require the Images library object
    #this class will contain methods which deal with the general ui of Magic
    #while other interface objects will contain methods for specific windows
    def __init__(self):
        super(FrontInterface, self).__init__()
        FrontInterface.trade_interface = ITrade.ITrade()
        FrontInterface.login_interface = ISignIn.ISignIn()
        FrontInterface.classified = IClassified.IClassified()
        FrontInterface.chat = IChat.IChat()
        
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