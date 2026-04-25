class Book:
    def __init__(self,title,aurthor,price):
      self.title=title
      self.aurthor=aurthor
      self.price=price
      self.available=True
    
    def checkout(self):
       if self.available:
          self.available=False
          print("Book is given")
       else:
          print("Book is checkedout")

    def return_book(self):
       self.available=="true"
    def display(self):
       print(f"title: {self.title} ,aurthor: {self.aurthor} cost is: {self.price} ,is {self.available}")

b=Book("python","nikhil",1009)   
b2=Book("java","rajesh",1290)
b.display()
b.checkout()
b.checkout()
b.return_book()
