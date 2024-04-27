class User:
    def __init__(self,username,email,password) -> None:

        self.username=username
        self.email=email
        self.password=password
        self.item_list=[]
        




class Seller(User):
    def __init__(self, username, email, password) -> None:
        super().__init__(username, email, password)

        self.seller_list=[]
        

    def seller_sign_up(self):
        self.seller_list.append(self)
        
    
    def seller_login(self, em, pas):
        flag = False
        for seller in self.seller_list:
            if em == seller.email and pas == seller.password:
                print("Welcome", seller.username)
                flag = True
                break
        
        if flag==False:
            print("Account not found, please try again")

    
    def seller_add_item(self,item):
        self.item_list.append(item)

    

    def seller_show_item(self):
        
        print(f"item\tprice\tquantity")
        
        for i in self.item_list:
            print(f"{i.name}\t{i.price}\t{i.quantity}")
    


class customer(User):
    def __init__(self, username, email, password) -> None:
        super().__init__(username, email, password)

    
        self.customer_list=[]
        self.cart_list=[]


    
    
    
    def add_customer(self,custom):
        self.customer_list.append(custom)

    # def check_item_quantity(self,food,quantity):
    #     flg=False
    #     for i in self.item_list:
    #         print (i.quantity)
    #         if(i.name.lower()==food.lower()):
    #             flg=True
    #             if(flg==True): 
    #              if(quantity>i.quantity):
    #                 print("Your number of order exceeded")
    #              else:
    #                 return food
        
    #     print("Your item isnot available right now")

    def check_item_quantity(self, food, quantity):
     print(self.item_list)
     for item in self.item_list:
        
        
        print('check',item)
        if item.name.lower() == food.lower():
            if quantity <= item.quantity:
                return item  # Return the item object if available
            else:
                print("Your number of orders exceeded")
                return None  # Return None if quantity exceeds available quantity
    
     print("Your item is not available right now")
     return None 



    def add_to_cart(self,item,quantity):
        item=self.check_item_quantity(item,quantity)
        print ('from add_to_cart',item )

        if item:
            item.quantity=quantity
            self.cart_list.append(item)
            print("item added")


     
    def view_cart(self):
        print("_____Here is your Cart_____")
        print("Name\tPrice\tQuantity")
        for item,quantity in self.cart_list:
            print(f"{item.name}\t{item.price}\t{quantity}")
        
     
     
          
             

class Admin(User):
    def __init__(self, username, email, password) -> None:
        super().__init__(username, email, password)
        

    
    def add_item(self,shop):
        self.item_list.append(shop)


    def show_item(self):
        for i in self.item_list:
            print(i)
    
                                    





  


