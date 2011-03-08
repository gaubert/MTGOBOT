path_to_bot = ""
import sys
sys.path.append(path_to_bot + "view")
import Interface
from sikuli.Sikuli import *

class IChat(Interface.Interface):
    
    #Text recognition is EXPERIMENTAL, SIKULI X only, currently, and INCONSISTENT RESULTS
    def wait_for_text(self, string, wait, region):
        """takes the text sought, max time to wait, and a region object of the chat window as paramters, returns True if found, false otherwise"""
        #this uses experimental functions that aren't 100% accurate, wait for improvements of text recognition before using
        if(chat_region.find(message)):
            return True
        else:
            return False
            
    #methods for interacting with chat window
    def __init__(self):
        super(IChat, self).__init__()
    
    def get_customer_name(self):
        click()
        
        
    def type_msg(self, msg):
        #if there is a minimize button click it first
        current_sim = Settings.MinSimilarity
        Settings.MinSimilarity = 0.4
        loc = self.app_region.find(self._images.get_chat_window("type_area"))
        if loc is Match:
            self._slow_click(target=loc)
        self._slow_click(target=self._images.get_chat_window("type_area"))
        Settings.MinSimilarity = current_sim
        del(current_sim)
        paste(msg); wait(0.1)
        type(Key.ENTER)
        
    def wait_for_message(self, string, duration, greetings = None):
        match = self.app_region.exists(self._images.get_chat_text(string), duration)
        
        #if the word to search for already appears in the customer greeting then
        #must account for that and search for a second instance of that word
        
        #this will account for the word also appearing in the bots messages and hhhhy
        if greetings:
            greetings_list = set(greetings)
            if type(string).__name__ == "string":
                if string in greetings:
                    pass
                    
            if type(string).__name__ == "list":
                for word in string:
                    if word in greetings:
                        word_found = True
                        break
    
    def close_current_chat(self):
        #closes the current chat window that is minimized to the right
        close_button=Pattern(self._images.get_chat_window("expand_close")).targetOffset(11, 4)
        if self.app_region.exists(close_button):
            self._slow_click(target=close_button)
            wait(3)
    def minimize_chat_window(self):
        #minimizes a chat window"
        """takes a minimize button image as parameter, returns True if found and clicked, returns False otherwise"""
        #lower the current similarity rating as the minimize button can be slightly different each time, then return the similarity rating to original number
        minimize_button = self.app_region.exists(self._images.get_chat_window("minimize"), 60)
        
        min_loc = minimize_button.getTarget()
        
        self._slow_click(loc=min_loc)

    def minimize_chat_all(self):
        #minimizes all chat windows
        """Returns True if successul, returns false otherwise"""
        matches = self.app_region.findAll(self._images.get_chat_window("minimize_button"))
        if matches:
            for found in matches:
                match = found
                self._slow_click(target=match)
            return True
        else:
            return False