#shop_online = True

available_products = {
    "water": 4,
    "coc": 2,
    "toilet paper": 10,
    "bread": 2,
}


def order():

    product_to_order = input("Whats the product you want to order: ")
    if check_availability(product_to_order):
         if payment(product_to_order):
              address = input("Please choose your address: ")


def check_availability(product):
        
        global available_products

        if product in available_products:
            if available_products[product] > 0 :
                ordered_product_quantity = int(input(f"Please enter the quantity of {product}: "))
                if ordered_product_quantity <= available_products[product]:
                     available_products[product] -= ordered_product_quantity
                     return True
                else:
                     print(f"There is only {available_products[product]} of {product} available!")
                     check_availability(product)
            else:
                 print(f"sorry we ran out of {product}")
                 return False
        else:
             print(f"This item is not available")
             return False
        

def payment(product):
     
     payment_method = input("Please choose your payment method (Cash/Credit): ").lower()

     if payment_method == "cash":
          return True
     elif payment_method == "credit":
          print("redirecting to payment page")
          if check_transaction():
               print("Transaction completed!")
               return True
          else:
               continue_ordering = input("Transaction failed!, type yes if you want to order again: ")
               if continue_ordering == "yes":
                    order()
               else:
                    return False
     else:
          print("Please becareful with your input!")
          payment(product)


def check_transaction():
     
     transaction_results = input("Do you have money?(yes/no): ")
     if transaction_results == "yes":
          return True
     else:
          return False


order()
