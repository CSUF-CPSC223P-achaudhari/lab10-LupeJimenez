# Lupita Jimenez 
# 11/ 15/ 23 

#  This program peforms a bot  that  fill up a shopping cart with items
#  and then  check out.  The bot  will  be  able to  add  items  to  the
#  shopping cart,  remove  items  from  the  shopping cart,  and  check
#  out.  The bot  will  also  be  able  to  check  the  contents  of  the shopping cart.

import threading
import time


# This function will  add  items  to  the  shopping cart,  remove  items  from  the  shopping cart,  and  check  out.  The bot  will  also  be  able  to  check  the  contents  of  the shopping cart.
def bot_clerk(items_num):
    shopping_cart = []
    lock = threading.Lock()
    
    def bot_fetcher(list, shopping_cart, lock, inventory):
        for item_num in list:
            time.sleep(inventory[item_num][1])
            with lock:
                shopping_cart.append([item_num,inventory[item_num][0]])
                
    fetcher = {1: [], 2: [], 3: []}
    for i, item_num in enumerate(items_num, start = 1):
        fetcher[i % 3 + 1].append(item_num)
    
        
    inventory = {
        "101": ["Notebook Paper", 2],
        "102": ["Pencils", 2],
        "103": ["Pens", 6],
        "104": ["Graph Paper", 1],
        "105": ["Paper Clips", 1],
        "106": ["Staples", 4],
        "107": ["Stapler", 7],
        "108": ["3 Ring Binder", 1],
        "109": ["Printer Paper", 1],
        "110": ["Notepad", 1]
    }   
        
    threads = []
    for i in range(1, 4):
        t= threading.Thread(target = bot_fetcher, args=(fetcher[i], shopping_cart, lock, inventory))
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()
        
    return shopping_cart


# The main to test bot function: 

if __name__ == "__MAIN__":
    items_list = ['101', '102', '103', '104', '105', '106', '107', '108', '109', '110'] 
    result = bot_clerk(items_list)
    print("Final Cart:", result)  
        
    
            
        

