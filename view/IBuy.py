path_to_bot = ""
import sys
sys.path.append(path_to_bot + "view")
import PackPricesDAL
import CardPricesDAL
import Product

sys.path.append(path_to_bot + "view")
import ITrade
from sikuli.Sikuli import *

class IBuy(ITrade.ITrade):
    #this class is used when the bot is put into buy mode during a trade
    
    def __init__(self):
        super(IBuy, self).__init__()
        self.__pack_prices = PackPricesDAL.PackPricesDAL()
        self.__card_prices = CardPricesDAL.CardPricesDAL()
    
    def take_all_copies_of_product(self):
        #this will keep taking the product until there are no more of that product
        pass

    def take_single_pack(self, product_loc, quantity):
        #this will take all the packs from the given location
        #right click on the product to open context menu
        self._slow_click(loc=product_loc, button="Right")
        #take 32 at a time, until there are no more, Magic Online UI will give all if there are less than 32 left
        while quantity > 0:
            self._slow_click(self._images.get_amount(32))
            quantity -= 32

    def take_packs(self):
        #will take all packs found in the customers collection and in buy list
        self.go_to_tickets_packs()
        
        #declare variable to hold amount of tickets the customer should take
        tickets_to_give = 0
        #holds the prices for all the packs
        prices = PackPricesDAL.PackPricesDAL()
        
        #a dict that holds images of the names of all packs
        pack_names_keys = self._images.get_pack_keys()
        pack_names_images = self._images.get_packs_text(phase="preconfirm")
        #this will hold all the product objects that have been taken
        packs_taken = []
        number_list = self._images.get_number(number=None, category="trade", subcategory="preconfirm")
        
        #this variable is used as an indicator whether the while loop should keep iterating
        found = True
        
        while found:
            found = False
            for pack_abbr in pack_names_keys:
                print("searching for " + str(pack_names_images[pack_abbr]))
                if self.topmost_product_name_area.exists(Pattern(pack_names_images[pack_abbr]).similar(0.8)):
                    print("found " + str(pack_abbr) + "!")
                    found = True
                    amount = 0
                    for num in range(len(number_list)):
                        if num == 0:
                            continue
                        print("searching for number: " + str(number_list[num]))
                        if self.topmost_product_quantity_area.exists(Pattern(number_list[num]).similar(0.9)):
                            amount = num
                            self.take_single_pack(product_loc=self.topmost_product_name_area.getCenter(), quantity=amount)
                            break

                    pack_abbr_index = pack_names_keys.index(pack_abbr)+1
                    pack_names_keys = pack_names_keys[pack_abbr_index:]
                    
                    if amount == 0:
                        raise ErrorHandler("Found 0 of " + str(pack_abbr))
                    
                    pack_obj = Product.Product(name=pack_abbr, buy = self.__pack_prices.get_buy_price(pack_abbr), sell = self.__pack_prices.get_sell_price(pack_abbr), quantity=amount)
                    packs_taken.append(pack_obj)
                    break
        
        for pack in packs_taken:
            tickets_to_give += pack["quantity"] * pack["buy"]
        
        if self.app_region.exists(self._images.get_trade("canceled_trade")):
            return False
        return tickets_to_give
    
    def take_cards(self):
        pass
        
        return 0
    
    def take_products(self):
        #confirm button will be used for relative positioning the regions for products scanning
        confirm_button = self.app_region.exists(self._images.get_trade(filename="confirm_button"), 30)
        #find the position in the window where the topmost product would be located
        
        self.topmost_product_name_area = Region(confirm_button.getX()-271, confirm_button.getY()+47, 159, 13)
        self.topmost_product_quantity_area = Region(confirm_button.getX()-113, confirm_button.getY()+47, 40, 13)
        
        name_sort_button_location = Location(confirm_button.getX()-231, confirm_button.getY()+23)
        self._slow_click(loc=name_sort_button_location)
        
        #we don't want to take tickets, just products
        if self.topmost_product_name_area.exists(self._images.get_ticket_text()):
            print("event ticket found, moving down")
            self.topmost_product_name_area = Region(self.topmost_product_area.getX(), self.topmost_product_area.getY()+18, 159, 13)
            self.topmost_product_quantity_area = Region(self.topmost_product_quantity_area.getX(), self.topmost_product_quantity_area.getY()+18, 40, 9)
        print("LOC IS : X =" + str(self.topmost_product_name_area.getX()) + " AND Y = " + str(self.topmost_product_name_area.getY()))
        
        tickets_to_give = 0
        tickets_for_packs = self.take_packs()
        print("Reached 109 and tickets = " + str(tickets_for_packs))
        #if customer cancels trade
        if tickets_for_packs is False:
            return False
        else:
            tickets_to_give += tickets_for_packs
        tickets_for_cards = self.take_cards()
        #if customer cancels trade
        if tickets_for_cards is False:
            return False
        else:
            tickets_to_give += tickets_for_cards
        print("Reached 120")
        print(str(tickets_to_give))
        return tickets_to_give
        
    def preconfirm_scan_purchase(self):
        #will scan the giving and receiving window to see if items match
        taking_name_region = Region(self.taking_window_region.getX()+34, self.taking_window_region.getY()+45, 145, 17)
        taking_number_region = Region(self.taking_window_region.getX(), self.taking_window_region.getY()+45, 30, 17)
        
        giving_name_region = Region(self.giving_window_region.getX()+35, self.giving_window_region.getY()+43, 197, 17)
        giving_number_region = Region(self.giving_window_region.getX()+3, self.giving_window_region.getY()+43, 30, 17)
        
        pack_images = self._images.get_packs_text(phase="preconfirm")
        pack_image_keys = self._images.get_pack_keys()
        
        numbers_list = self._images.get_number(category = "trade", subcategory = "preconfirm")
        
        #will hold the name of all products found
        products_found = []
        
        #will hold all the Product objects of items found
        products_obj_found = []
        
        scroll_bar_loc = Location(self.giving_window_region.getX()+388, self.giving_window_region.getY()+80)
        found = True
        while True:
            found = False
            
            for pack_abbr in pack_image_keys:
            
                if taking_name_region.exists(Pattern(pack_images[pack_abbr]).similar(0.9)):
                    found = True
                    products_found.append(pack_abbr)
                    
                    
                    for number, number_img in range(len(Pattern(numbers_list).similar(0.8))):
                    
                        if taking_number_region.exists(number_img):
                            pack_obj = Product(name = pack_abbr, buy = self.__pack_prices.get_buy_price(pack_abbr), sell = self.__pack_prices.get_sell_price(pack_abbr), quantity = number)
                            products_obj_found.append(pack_obj)
                            break
                    break
            
            wheel(scroll_bar_loc, WHEEL_DOWN, 2)
        total_expected_tickets = 0
        for product in product_obj_found:
            total_expected_tickets += product["buy"] * product["quantity"]
        
        #wait 2 minutes for the customer to find event ticket, then 2 minutes to take the correct amount
        if giving_name_region.wait(Pattern(self._images.get_ticket_text()).similar(0.9), 120):
            giving_name_region.wait(Pattern(numbers_list[total_expected_tickets]).similar(0.9), 120)
            return True
        #if he still hasn't taken a ticket, then close the trade
        else:
            return False
        
    def confirmation_scan(self):
        """will return number of tickets taken for transaction recording"""
        #verify confirm window by checking for confirm cancel buttons, then set regions relative to those buttons
        confirm_button = exists(self._images.get_trade(filename="confirm_button", phase="confirm"), 1200)
        
        if not confirm_button:
            self._slow_click(loc=Pattern(self._images.get_trade["cancel_button"]))
        
        if isinstance(confirm_button, Match):
            #keeps record of products found and their amount so far
            receiving_products_found = []
            pack_names_keys = self._images.get_pack_keys()
            pack_names = self._images.get_packs_text(phase="confirm")
            numbers = self._images.get_number(number=None, category="trade", subcategory="confirm")
            #confirm products receiving
            #set the regions of a single product and and the amount slow
            #number region is 20px down and 260px to the left, 13px height and 30px wide, 4px buffer vertically
            receiving_number_region = Region(confirm_button.getX()-289, confirm_button.getY()+41, 34, 14)
            #height for each product is 13px, and 4px buffer vertically between each product slot
            receiving_name_region = Region(confirm_button.getX()-254, confirm_button.getY()+41, 160, 14)
            #confirm products giving
            giving_number_region = Region(confirm_button.getX()-291, confirm_button.getY()+391, 34, 14)
            giving_name_region = Region(confirm_button.getX()-257, confirm_button.getY()+391, 160, 14)
            #this is a variable that will hold the number of pixels to move down after scanning each area
            how_many_pixels_to_move_down = 0
            
            found=True
            while found:
                print("while loop run")
                hover(Location(receiving_number_region.getX(), receiving_number_region.getY()))
                found=False
                for product_abbr in pack_names_keys:
                    print("looking for " + str(product_abbr))
                    if receiving_name_region.exists(Pattern(pack_names[product_abbr]).similar(0.8)):
                        print("confirmation window: "+product_abbr+" found")
                        
                        #if still at 0 after for loop, error raised
                        amount = 0
                        for number in range(len(numbers)):
                            if number == 0:
                                continue
                            print(numbers[number])
                            if receiving_number_region.exists(Pattern(numbers[number]).similar(0.8)):
                                print("CURRENT NUMBER STRING FOUND " + str(numbers[number]))
                                amount = number
                                
                                #packs are listed in Magic in the same sequence they are listed in the list of pack keys,
                                #if a pack is found, all packs including it and before, are removed from the list of packs
                                #to search
                                pack_index = pack_names_keys.index(product_abbr) + 1
                                pack_names_keys = pack_names_keys[pack_index:]
                                
                                break
                            
                        product_obj = Product(name=product_abbr, buy = self.__pack_prices.get_buy_price(product_abbr), sell = self.__pack_prices.get_sell_price(product_abbr), quantity=amount)
                        receiving_products_found.append(product_obj)
                                            
                        if amount == 0:
                            raise ErrorHandler("Could not find a number for product: " + str(product_abbr))
                        found=True
                        
                        if how_many_pixels_to_move_down != 17:
                            how_many_pixels_to_move_down = 17
                        else:
                            how_many_pixels_to_move_down =  18
                        receiving_number_region = Region(receiving_number_region.getX(), receiving_number_region.getY()+how_many_pixels_to_move_down, receiving_number_region.getW(), receiving_number_region.getH())
                        receiving_name_region = Region(receiving_name_region.getX(), receiving_name_region.getY()+how_many_pixels_to_move_down, receiving_name_region.getW(), receiving_name_region.getH())
                        break
            
            #get image of number expected to scan for it first, to save time, else search through all other numbers
            expected_number = 0
            for product in receiving_products_found:
                expected_number += product["quantity"] * product["buy"]
            print(str(expected_number))
            
            if expected_number == 0:
                return False
                
            hover(Location(giving_number_region.getX(), giving_number_region.getY()))
            ticket_text_image = Pattern(self._images.get_ticket_text()).similar(1)
            if giving_name_region.exists(ticket_text_image):
                expected_number_image = Pattern(self._images.get_number(number=expected_number, category="trade", subcategory="confirm")).similar(0.7)
                if giving_number_region.exists(expected_number_image):
                    print("event ticket number found")
                    
                    return receiving_products_found
                else:
                    return False
            
    def complete_purchase(self, method="A"):
        """Will return the transactions details to be recorded if successul
        else will return False"""
        
        if method == "A":
            #take the products first, then tell customer how many tickets to take
            #requires IChat interface to be passed to tell customers how many tickets to take
            
            #switch to list view in the collection window
            self._slow_click(target=self._images.get_trade(filename="list_view_collection_window"))
            
            running_total = self.take_products()
            
            if running_total == 0 or not running_total:
                cancel_button = self.app_region.exists(self._images.get_trade(filename="cancel_button"))
                if cancel_button:
                    self.slow_click(loc=cancel_button.getTarget())
                self._slow_click(target=self._images.get_ok_button())
                return False
            
            total_tickets_notice = 'Please take %i tickets.' % running_total
            self.Ichat.type_msg(total_tickets_notice)
            
            #scan the giving region area, if customer doesn't take ticket in time or scan files, cancel trade
            #if not self.preconfirm_scan_purchase(): 
            #    self._slow_click(loc=Pattern(self._images.get_trade["cancel_button"]))
            
            self.go_to_confirmation()
            
            #run a final confirmation scan to check the products and tickets taken
            products_bought = self.confirmation_scan()
            
            self.Ichat.close_current_chat()
        
            if products_bought:
                print("passed final check")
                
                self._slow_click(target=self._images.get_trade(phase="confirm", filename="confirm_button"))
                wait(Pattern(self._images.get_ok_button()), 600)
                self._slow_click(target=self._images.get_ok_button())
            
                return products_bought
                
            else:
                print("failed final check")
                cancel_button = self.app_region.exists(self._images.get_trade(phase="confirm", filename="cancel_button"))
                if cancel_button:
                    self.slow_click(loc=cancel_button.getTarget())
                self._slow_click(target=self._images.get_ok_button())
                return False
            
        elif method == "B":
            #let customer take tickets first, then take products totalling up to products taken
            #prompt users with IChat whether they want to sell cards, packs, or both
        
            #read the number of tickets taken
            number_of_tickets_taken = self.tickets_taken()
            
            self.Ichat.type_msg("Type \"packs\" to sell boosters, \"cards\" to sell singles")
            
            prompts = ["packs", "cards", "both"]
            
            response = self.Ichat.wait_for_message(prompts)
            
            if response == "packs":
                self.take_packs(number_of_tickets)
            elif response == "cards":
                self.take_cards(number_of_tickets)