#This code was written by Raymond Cheung
#No one is allowed to modify this code
#if you have any questions about it, I can be emailed at Darkray16@yahoo.com
#This is a bot that with automated behavior to run independantly on Magic the Gathering: Online

#DEPENDENCIES
#used in controller to set time of transaction for recording
from datetime import datetime
import sys
sys.path.append("c:/users/darkray16/desktop/my dropbox/mtgo bot")
import model
import view
import controller

exec(open("c:/users/darkray16/desktop/my dropbox/mtgo bot/ini.py", "rb").read())
 
class Bot(object):
    #this is at the highest level and owns all other classes
    #its a wrapper class that will encompass every other class
    __single = None
    
    def __init__(self):
        #no more than one instance is needed at a time
        if Bot.__single:
            raise ErrorHandler("Bot class cannot be instantiated more than once")
        Bot.__single = self
        
        self.primary_controller = controller.MainController()
        
    def main(self):
        #run when script starts
        self.primary_controller.startup()
        
    def do_function(self):
        self.primary_controller.trade_mode()

        

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
        


#run the bot
Bot_App = Bot()
Bot_App.do_function()