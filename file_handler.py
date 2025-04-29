# file_handler.py
import csv
import os
from book import Book, EBook

def save_library_to_csv(library):  # Accept library as parameter
    with open("library.csv", 'w', newline="") as file:
        fieldnames = ["title", 'author', 'year', 'genre', 'file_size', 'book_type']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()  # Don't forget to write headers
        
        for book in library:
            if isinstance(book, EBook):  # Fixed this line
                writer.writerow({
                    "title": book.title,
                    "author": book.author,
                    "year": book.year,
                    "genre": book.genre,
                    "file_size": book.file_size,
                    "book_type": "ebook"
                })
            else:  # It's a normal Book
                writer.writerow({
                    "title": book.title,
                    "author": book.author,
                    "year": book.year,
                    "genre": book.genre,
                    "file_size": "",
                    "book_type": "book"
                })

def load_library_from_csv():
    library = []  # Create new list to return
    if not os.path.exists("library.csv"):
        print("No existing library found. Starting fresh.")
        return library
    
    with open('library.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["book_type"] == 'ebook':
                ebook = EBook(
                    row["title"],
                    row["author"],
                    row["year"],
                    row["genre"],
                    row["file_size"]
                )
                library.append(ebook)
            else:
                book = Book(
                    row["title"],
                    row["author"],
                    row["year"],
                    row["genre"]
                )
                library.append(book)
    return library