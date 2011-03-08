path_to_bot = ""
import sys
sys.path.append(path_to_bot + "model")
import PackPricesDAL
import CardPricesDAL
import Product

sys.path.append(path_to_bot + "view")
import ITrade
from sikuli.Sikuli import *

class ISell(ITrade.ITrade):
    #this class is used when the bot is put into temporary sell mode during a trade or perma sell mode prior to trade
    
    def __init__(self):
        super(ISell, self).__init__()
        self.__pack_prices = PackPricesDAL.PackPricesDAL()
        self.__card_prices = CardPricesDAL.CardPricesDAL()
        
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
        
        #in case the user has canceled
        if not number_of_tickets:
            return False
            
        self.products_giving = found
        #calculate tickets to take
        total_tickets_to_take = self.calculate_products_to_tickets(found)
        
        #return the the number of packs that should be taken, number in image form
        return total_tickets_to_take
    
    def search_for_images_sale(self):
        print("running search for images")
        #searches a certain area for any image in a dictionary
        
        #combine all cards and packs for sale into a list
        pack_names_list = self._images.get_pack_keys()
        
        images = self._images.get_packs_text(phase="preconfirm")
        
        numbers_list = self._images.get_number(category = "trade", subcategory = "preconfirm")
        
        #if area searched contains a full sized scroll bar, then scroll down
        #variable to hold last mouse position for the scrollbar movement code
        self.last_mouse_position = False
        #list of all images found
        products = []
        #keep a record of product names found to prevent duplicates
        regular_scroll_bar = None
        mini_scroll_bar = None
        scroll_bar = self.giving_window_region.exists(self._images.get_trade(("scroll_bar_regular")))
        if not scroll_bar:
            scroll_bar = region.exists(self._images.get_trade(("scroll_bar_mini")))
        #hover over scroll bar for mouse wheel manipulation
        scroll_bar_loc = scroll_bar.getTarget()
        #scan_region will be used as the region to scan for the packs and number of packs
        #using the giving window as region, each product row is scanned for a product name and quantity
        #NOTE: A single area reserved for the text of a single product is a 192px(width) by 16/17px(height) area, with a 1px buffer in between each string
        scan_region = Region(self.giving_window_region.getX()+2, self.giving_window_region.getY()+43, 196, 17)
        #keep while loop as long as there is still a pack to be scanned
        found = True
        while found:
            found = None
            for product_abbr in pack_names_list:
            
                print("reached line 479 pack_text_name = " + product_abbr)
                #determine which packs are in the giving window
                pack = self._images.get_packs_text(phase="preconfirm", filename=product_abbr)
                
                if scan_region.exists(Pattern(pack).similar(0.9)):
                    
                    found = True
                    print(str(pack) + " found!")
                    
                    print(str(product_abbr))
                    
                    for key in range(len(numbers_list)):
                        if key == 0:
                            continue
                        searchPattern = Pattern(numbers_list[key]).similar(0.8)
                        if(scan_region.exists(searchPattern)):
                            amount = key
                            #for booster packs, there is a specific order in which they appear in the list,
                            #when a pack is found, remove all packs before and including that pack in the keys
                            #list as they will not appear any further below
                            pack_index = pack_names_list.index(product_abbr)+1
                            pack_names_list = pack_names_list[pack_index:]
                            
                            break
                            
                    print("amount = "+str(key))
                    product = Product.Product(name = product_abbr, buy = self.__pack_prices.get_buy_price(product_abbr), sell = self.__pack_prices.get_sell_price(product_abbr), quantity = amount)
                    products.append(product)
                    
                    wheel(scroll_bar_loc, WHEEL_DOWN, 2)
                
                if found == True:
                    print("found is true")
                    break
            
            #if first scan area was already set, then relative distance from last region
            #scan area will be slightly larger than estimated height of product slot to compensate for any variances, to compensate for larger region, the Y coordinate -1
            scan_region = Region(scan_region.getX(), scan_region.getY()+17, scan_region.getW(), scan_region.getH())
            print("reassigning scan region")
        print("finished while loop")
        
        #in case the customer has canceled the trade
        if self.app_region.exists(self._images.get_trade("canceled_trade")):
            self._slow_click(loc=self._images.get_ok_button())
            return False
        
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
            #taken is assigned false is any click function is interrupted by the user canceling the trade
            if not taken:
                return False
        print("finished taking tickets")
        del(location_cache)
        return True
        
    def click_tickets(self, take, taken, cache):
        """this function is used in the take_ticket method, three required parameters are passed
        take=the number of tickets to take. taken=how many tickets have been taken, 
        this number will be returned after having added the numbers of tickets taken in this invocation.
        cache=the cached locations of the the buttons needed for this interaction
        click_check is used to see if the image could be found, if not this returns False,
        signifying that the trade was probably caneled"""
        
        if cache["ticket"] is None:
        
            click_check = self._slow_click(target=self._images.get_ticket(), button="Right")
            if not click_check:
                return False
            cache["ticket"] = Env.getMouseLocation()
        else:
            click_check = self._slow_click(loc=cache["ticket"], button="Right")
            if not click_check:
                return False
        if cache["take_"+str(take)+"_tickets"] is None:
            print("Line 658, taken = "+str(taken) + " and take=" + str(take))
            click_check = self._slow_click(target=self._images.get_amount(take))
            if not click_check:
                return False
            cache["take_"+str(take)+"_tickets"] = Env.getMouseLocation()
            taken += take
            print("Line 662, taken = "+str(taken) + " and take=" + str(take))
        else:
            click_check = self._slow_click(loc=cache["take_"+str(take)+"_tickets"])
            if not click_check:
                return False
            print("Line 663, taken = "+str(taken) + " and take=" + str(take))
            taken += take
            print("Line 665, taken = "+str(taken) + " and take=" + str(take))
        return taken
    
    def return_ticket(self, number):
        #clicks on the decrease ticket to return one ticket
        pass
        
    def take_packs(self):
        #scans users collection for packs wanted
        pass

    def preconfirm_scan_sale(self, products_giving):
        """takes the total number of products taken by customer and checks to see if the correct amount of tickets are in the taking window"""
        numbers = self._images.get_number(category="trade", subcategory="preconfirm")
        
        ticket = self._images.get_ticket_text()
        
        expected_total = 0
        for product in products_giving:
            print("804 "+str(product["name"]))
            expected_total += product["sell"]*product["quantity"]
        
        tickets_found = 0
        #product height = 17, width = 145, relative distance from upper left region corner, y = 46, x =35
        scan_region_product = Region(self.taking_window_region.getX()+34, self.taking_window_region.getY()+45, 145, 17)
        #product height = 17, width = 30, relative distance from upper left region corner, y = 46, x =1
        scan_region_number = Region(self.taking_window_region.getX(), self.taking_window_region.getY()+45, 30, 17)

        if scan_region_product.exists(ticket):
            print("found ticket in taking window")
            #for performance, start the number scan with the expected number
            if scan_region_number.exists(self._images.get_number(number=expected_total, category="trade", subcategory="preconfirm")):
                tickets_found = expected_total
            #in case user canceled trade
            elif self.app_region.exists(self._images.get_trade("canceled_trade")):
                return False
            else:
                for number, number_image in numbers.items():
                    print("looking for number: " + str(number))
                    if scan_region_number.exists(number_image):
                        print("found number : " + str(number))
                        tickets_found = number
                        break

        if tickets_found >= expected_total:
            return True
            print("Pre confirm scan found %i tickets and expected %i tickets" % (tickets_found, expected_total))
        else:
            return False
            print("Total tickets found and expected tickets don't match.  Tickets found:"+str(tickets_found)+" and Tickets expected:"+str(expected_total))
  
    def confirmation_scan(self, type=None):
        #does a scan depending on which type is requested.  Each pass should scan the window differently
        #to confirm that the correct
        
        #verify confirm window by checking for confirm cancel buttons, then set regions relative to those buttons
        confirm_button = exists(self._images.get_trade(filename="confirm_button", phase="confirm"), 1200)
        
        if isinstance(confirm_button, Match):
            #keeps record of products found and their amount so far
            giving_products_found = []
            pack_names_keys = self._images.get_pack_keys()
            pack_names = self._images.get_packs_text(phase="confirm")
            numbers = self._images.get_number(number=None, category="trade", subcategory="confirm")
            #confirm products receiving
            #set the regions of a single product and and the amount slow
            #number region is 20px down and 260px to the left, 13px height and 30px wide, 4px buffer vertically
            receiving_number_region = Region(confirm_button.getX()-289, confirm_button.getY()+42, 34, 14)
            #height for each product is 13px, and 4px buffer vertically between each product slot
            receiving_name_region = Region(confirm_button.getX()-254, confirm_button.getY()+42, 160, 14)
            #confirm products giving
            giving_number_region = Region(confirm_button.getX()-291, confirm_button.getY()+391, 34, 14)
            giving_name_region = Region(confirm_button.getX()-257, confirm_button.getY()+391, 160, 14)
            found=True
            #scan the giving window
            hover(Location(receiving_number_region.getX(), receiving_number_region.getY()))
            wait(2)
            hover(Location(receiving_number_region.getX()+34, receiving_number_region.getY()+14))
            
            while found:
                print("while loop run")
                hover(Location(giving_number_region.getX(), giving_number_region.getY()))
                found=False
                for product_abbr in pack_names_keys:
                    print("looking for " + str(product_abbr))
                    if giving_name_region.exists(Pattern(pack_names[product_abbr]).similar(0.8)):
                        print("confirmation window: "+product_abbr+" found")
                        
                        #if still at 0 after for loop, error raised
                        amount = 0
                        for number in range(len(numbers)):
                            if number == 0:
                                continue
                            print(numbers[number])
                            if giving_number_region.exists(Pattern(numbers[number]).similar(0.8)):
                                print("CURRENT NUMBER STRING FOUND " + str(numbers[number]))
                                amount = number
                                
                                #packs are listed in Magic in the same sequence they are listed in the list of pack keys,
                                #if a pack is found, all packs including it and before, are removed from the list of packs
                                #to search
                                pack_index = pack_names_keys.index(product_abbr) + 1
                                pack_names_keys = pack_names_keys[pack_index:]
                                
                                break
                            
                        product_obj = Product(name=product_abbr, buy = self.__pack_prices.get_buy_price(product_abbr), sell = self.__pack_prices.get_sell_price(product_abbr), quantity=amount)
                        giving_products_found.append(product_obj)
                                            
                        if amount == 0:
                            raise ErrorHandler("Could not find a number for product: " + str(product_abbr))
                        found=True
                        giving_number_region = Region(giving_number_region.getX(), giving_number_region.getY()+17, giving_number_region.getW(), giving_number_region.getH())
                        giving_name_region = Region(giving_name_region.getX(), giving_name_region.getY()+17, giving_name_region.getW(), giving_name_region.getH())
                        break
            
            #get image of number expected to scan for it first, to save time, else search through all other numbers
            expected_number = 0
            for product in giving_products_found:
                expected_number += product["quantity"] * product["sell"]
            print(str(expected_number))
            
            if expected_number == 0:
                return False
            
            #in case the customer has canceled trade
            if self.app_region.exists(self._images.get_trade("canceled_trade")):
                return False

            hover(Location(receiving_number_region.getX(), receiving_number_region.getY()))
            ticket_text_image = Pattern(self._images.get_ticket_text()).similar(1)
            if receiving_name_region.exists(ticket_text_image):
                expected_number_image = Pattern(self._images.get_number(number=expected_number, category="trade", subcategory="confirm")).similar(0.7)
                if receiving_number_region.exists(expected_number_image):
                    print("event ticket number found")
                    
                    return giving_products_found
                else:
                    return False
            
    def complete_sale(self):
        print("running complete_sale")
        #calls calculate_tickets_to_take to get the number of tickets to take and proceeds to take them, 
        #does a check to make sure correct ticket amount was taken
        
        self.Ichat.wait_for_message(string="done", duration=1200)
        
        self.Ichat.type_msg("Calculating tickets to take.  Please wait..")
        
        number_of_tickets = self.tickets_to_take_for_packs()
        
        #in case the user has canceled
        if not number_of_tickets:
            return False
            
        print("complete_sale step1 finished, number of tickets to take:%i" % number_of_tickets)
        
        self.go_to_tickets_packs()
        print("complete_sale step2 finished")
        
        take_result = self.take_ticket(number_of_tickets)
        #if trade was canceled or take tickets failed
        if not take_result:
            if self.app_region.exists(self._images.get_trade("cancel_button")):
                self._slow_click(self._images.get_trade("cancel_button"))
            elif self.app_region.exists(self._images.get_trade("canceled_trade")):
                self._slow_click(self._images.get_ok_button())
            return False
        
        
        #INSERT PRE-CONFIRM TRANSACTION CHECK HERE#
        
        #image of the total number of tickets to take
        number_image = self._images.get_number(number = number_of_tickets, category = "trade", subcategory = "preconfirm")
        
        preconfirm = self.preconfirm_scan_sale(products_giving=self.products_giving)
        
        #if trade was canceled or preconfirm failed
        if not preconfirm:
            if self.app_region.exists(self._images.get_trade("cancel_button")):
                self._slow_click(self._images.get_trade("cancel_button"))
            elif self.app_region.exists(self._images.get_trade("canceled_trade")):
                self._slow_click(self._images.get_ok_button())
            return False
        
        self.go_to_confirmation()
        #check to make sure correct number of tickets taken
        
        #INSERT PRE-FINAL TRANSACTION CHECK HERE#
        
        #scan confirmation screen multiple times in different ways before clicking final confirm
        
        #INSERT FINAL TRANSACTION CHECK HERE#
        
        #returns an object that holds all products sold if successful scan
        #otherwise returns False
        products_sold = self.confirmation_scan()
        
        self.Ichat.close_current_chat()
        
        if products_sold:
            print("passed final check")
            self._slow_click(target=self._images.get_trade(phase="confirm", filename="confirm_button"))
            wait(Pattern(self._images.get_ok_button()), 600)
            self._slow_click(target=self._images.get_ok_button(), button="LEFT")
            return products_sold
            
        else:
            #if false returned, either customer canceled trade in conformation screen, or product check failed
            print("failed final check")
            cancel_button = self.app_region.exists(self._images.get_trade(phase="confirm", filename="cancel_button"))
            if cancel_button:
                self.slow_click(cancel_button.getTarget())
            self._slow_click(target=self._images.get_ok_button())
            return False