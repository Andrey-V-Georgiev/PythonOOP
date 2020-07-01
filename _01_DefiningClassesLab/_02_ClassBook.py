class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages

    def name(self):
        return self.name

    def author(self):
        return self.name

    def pages(self):
        return self.name


book = Book("My Book", "Me", 200)
print(book.name)
print(book.author)
print(book.pages)
