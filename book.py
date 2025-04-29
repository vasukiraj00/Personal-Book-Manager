class Book:
    def __init__(self,title,author,year,genre):
        self.title= title
        self.author=author
        self.year=year
        self.genre= genre
        
    def __str__(self):
        return f"Title: {self.title}\n Author: {self.author}\n Year: {self.year}\n Genre: {self.genre}"
        
class EBook(Book):
    def __init__(self, title, author, year, genre,file_size):
        super().__init__(title, author, year, genre)
        self.file_size=file_size
        
    def __str__(self):
        return f"Title: {self.title}\n Author: {self.author}\n Year: {self.year}\n Genre: {self.genre}\n File Size: {self.file_size}"
        