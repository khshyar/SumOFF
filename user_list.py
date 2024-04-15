class UserWishList():
    def __init__(self):
        self.wishlist_items = {}

    def add_item(self, item):
        self.wishlist_items[item] = 1
        print(f"Added '{item}' to the wish list.")

    # gui option
    def plus_quantity(self, item):
        self.wishlist_items[item] += 1

    # gui option
    def minus_quantity(self, item):
        if self.wishlist_items[item] == 1:
            self.remove_item(item)
        else:
            self.wishlist_items[item] -= 1

    # gui option
    def remove_item(self, item):
        if item in self.wishlist_items:
            del self.wishlist_items[item]
            print(f"Remove '{item}' from the wish list.")
        else:
            print(f"Item '{item}' not fount in the wish list.")

    def view_list(self):
        if self.wishlist_items:
            print("Wish list Items: ")
            for item in self.wishlist_items:
                print(f" - '{item}': {self.wishlist_items[item]}")
        else:
            print("Your wish list is empty.")

    def clear_list(self):
        self.wishlist_items = []
        print("Wish list cleared")

    def export_to_text(self, filename):
        with open(filename, 'w') as file:
            for item in self.wishlist_items:
                file.write(item + self.wishlist_items[item] + '\n')
        print(f"Wish list exported to {filename}.")
