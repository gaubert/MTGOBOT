path_to_bot = ""
import sys
sys.path.append(path_to_bot + "model")
import ImagesModel
from sikuli.Sikuli import *

class Interface(object):
    #parent class for all Interface classes
    
    def __init__(self):
        self._images = ImagesModel.ImagesModel()
        
        magic_online = App("Magic Online")
        if not magic_online.window():
            raise ErrorHandler("Please open and log into Magic Online")
        else:
            self.app_region = magic_online.window()
            
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
            target_match = self.app_region.exists(target)
            
            #if click was called in middle of trade, check if it was cancelled
            if not target_match:
                if self.app_region.exists(self._images.get_trade("canceled_trade")):
                    return False
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
        return True