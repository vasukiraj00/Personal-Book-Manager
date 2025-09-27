# file_handler.py
import csv
import os
import shutil
from book import Book, EBook

#1.path handling function
def get_library_path():
    # Get the current directory of the script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Ensure the file is created directly under Personal_Book_Manager
    library_path = os.path.join(current_dir, "library.csv")
    
    return library_path

#2. duplicate removal function
def create_backup(original_path):
    if os.path.exists(original_path):
        backup_path = original_path.replace('.csv', '_backup.csv')
        shutil.copyfile(original_path, backup_path)
        print(f"Backup created at {backup_path}")
    
#3. duplicate prvention idea   
def remove_duplicate_books(library):
    seen =set()
    unique_books = []
    for book in library:
        book_id = (book.title.strip().lower(), book.author.strip().lower())
        #so here we use strip() to remove traialing spaces
        if book_id not in seen:
            seen.add(book_id)
            unique_books.append(book)
        else:
            print(f"Duplicate found and removed: {book.title} by {book.author}")
    return unique_books

#save function
def save_library_to_csv(library):  # Accept library as parameter
    file_path = get_library_path()
    print(f"Saving library to {file_path}")
    create_backup(file_path)  # Create backup before saving
    library = remove_duplicate_books(library)  # Remove duplicates before saving
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

# def save_library_to_csv(library):  
#     with open("library.csv", 'w', newline="") as file:
#         fieldnames = ["title", 'author', 'year', 'genre', 'file_size', 'book_type']
#         writer = csv.DictWriter(file, fieldnames=fieldnames)
#         writer.writeheader()
        
#         print("=== DEBUGGING ===")  # ← ADD THIS
#         for i, book in enumerate(library):
#             print(f"Book {i}: Type = {type(book)}")
#             print(f"Book {i}: Attributes = {dir(book)}")
#             print(f"Book {i}: Has file_size? = {hasattr(book, 'file_size')}")
#             print("---")
            
#             writer.writerow({
#                 "title": book.title,
#                 "author": book.author,
#                 "year": book.year,
#                 "genre": book.genre,
#                 "file_size": book.file_size,  # This should crash!
#                 "book_type": "ebook"
#             })

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