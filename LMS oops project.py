#parent class
class LibraryItem:
    def __init__(self,item_name,item_title):
        self.item_name = item_name
        self.item_title = item_title
    def borrowing_charges(self,borrow_days):
        pass
#child class of book
class Book(LibraryItem):
    def borrowing_charges(self, borrow_days):
        return borrow_days*10
#child class of magazine
class Magazine(LibraryItem):
    def borrowing_charges(self, borrow_days):
        return borrow_days*10
    
class LibraryApp:
    def __init__(self):
        self.item = None
    def create_item(self,item_name,item_title,item_type):
        if item_type == "Book":
            self.item = Book(item_name,item_title)
            return "Item type: Book"
        elif item_type == "Magazine":
            self.item = Magazine(item_name,item_title)
            return "Item type: Magazine"
        else:
            self.item = None
    def borrowing_charges(self,borrow_days):
        charges = self.item.borrowing_charges(borrow_days)
        return charges
    
app = LibraryApp()

print(app.create_item(1,"Programming in Python","Book"))
charges = app.borrowing_charges(5)
print("Borrow Days: 5")
print("Borrowing charges:",charges)

print(app.create_item(2,"Weekly Magazine","Magazine"))
charges = app.borrowing_charges(3)
print("Borrow Days: 3")
print("Borrowing charges:",charges)