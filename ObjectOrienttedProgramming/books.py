class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    def str(self):
        print("Title: {}".format(self.title))
        print("Author: {}".format(self.author))
        print("Pages: {}".format(self.pages))
book = Book("Harry Potter","J.K. Rowling",500)
book.str()

# output: Title: Harry Potter
#         Author: J.K. Rowling
#         Pages: 500