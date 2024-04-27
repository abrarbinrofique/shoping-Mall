from user import Seller, Admin,customer
from product import food_item

seler=Seller("abrar","ab","qw")
seler.seller_sign_up ()
e=input("Input your email: ")
p=input("Input your Password:  ")
seler.seller_login(e,p)

burger=food_item("burger",34,32)
seler.seller_add_item(burger)
pizza=food_item("pizza",12,20)
seler.seller_add_item(pizza)
seler.seller_show_item()
cus=customer('asdf','trgwea',546)
cus.add_to_cart('burger',1)
cus.view_cart()

