class book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        print("title:", self.title)
        print("author:", self.author)
        print("year:", self.year)
        #def info(self):
        # print(f"Title: {self.title}")
        # print(f"Author: {self.author}")
        # print(f"Year: {self.year}")

title = input ("pls enter the title of ur book:")
author = input("pls enter the name of author:")
year = input("pls enter the year that the book released on :")

ur_book = book(title, author, year)
ur_book.display_info()