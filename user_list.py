class UserWishList():
    def __init__(self):
        self.wishlist_items = []

    def add_item(self, item):
        self.wishlist_items.append(item)
        print(f"Added '{item}' to the wish list.")

    def remove_item(self, item):
        if item in self.wishlist_items:
            self.wishlist_items.remove(item)
            print(f"Remove {item} from the wish list.")
        else:
            print(f"Item {item} not fount in the wish list.")

    def view_list(self):
        if self.wishlist_items:
            print("Wish list Items: ")
            for item in self.wishlist_items:
                print(f" - {item}")
        else:
            print("Your wish list is empty.")

    def clear_list(self):
        self.wishlist_items = []
        print("Wish list cleared")

    def export_to_text(self, filename):
        with open(filename, 'w') as file:
            for item in self.wishlist_items:
                file.write(item + '\n')
        print(f"Wish list exported to {filename}.")
