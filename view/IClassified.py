path_to_bot = ""
import sys
sys.path.append(path_to_bot + "view")
import Interface
from sikuli.Sikuli import *

class IClassified(Interface.Interface):
    #methods for interacting with classified
    #in final version, should contain methods to post ads, search classified, remove ads
    
    def __init__(self):
        super(IClassified, self).__init__()
        
    def go_to_classified(self):
        if not self.app_region.exists(self._images.get_classified("search_posts")):   
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
        if self.app_region.exists(self._images.get_classified("edit_posting")):
            self._slow_click(target=self._images.get_classified("edit_posting"))
        if self.app_region.exists(self._images.get_classified("posting")):
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
        if self.app_region.exists(self._images.get_classified("remove_posting")):
            self._slow_click(target=self._images.get_classified("remove_posting"))
            return True
        else:
            raise ErrorHandler("No posting found, cannot remove")
            return False