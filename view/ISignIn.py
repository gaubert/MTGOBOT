path_to_bot = ""
import sys
sys.path.append(path_to_bot + "view")
import Interface
from sikuli.Sikuli import *

class ISignIn(Interface.Interface):
    #methods for interaction with login window

    def __init__(self):
        super(ISignIn, self).__init__()
        
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
