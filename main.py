from user_list import UserWishList

print("Welcome to SumOff")

user_input = input("Do you want to create your wishlist? (Y/N)").lower()

if user_input == "y":
    wishlist = UserWishList()

    add_item = True
    counter = 0
    while add_item:
        user_item = input(
            "What kind of product would you like to add to your list? Write 'STOP' to cancel adding. ").lower()

        if user_item == "stop":
            break
        wishlist.add_item(user_item)

    wishlist.view_list()

    export_format = input(
        "Do you want to export the list? Enter 'yes' for text file or 'no' to skip: ").lower()
    if export_format == 'yes':
        wishlist.export_to_text('wishlist.txt')
    else:
        print("No export performed.")
else:
    print("Wish list creation was cancelled.")
