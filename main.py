from book import Book, EBook
from file_handler import load_library_from_csv, save_library_to_csv

def add_book(library):  # Accept library as parameter
    book_type = input("Do you want to add a Book 📚 or an EBook 📱? (Type 'book' or 'ebook'): ").strip().lower()
    
    if book_type not in ['book', 'ebook']:
        print("Invalid input! Please type 'book' or 'ebook'.")
        return

    title = input("Enter the Title of the Book: ")
    author = input("Enter the Author of the Book: ")
    year = input("Enter the Year Book was Released: ")
    genre = input("Enter the type of Genre: ")

    if book_type == 'book':
        book = Book(title, author, year, genre)
        library.append(book)
        print(f"Book '{title}' added successfully!")
    elif book_type == 'ebook':
        file_size = input("Enter the File Size (in MB): ")
        ebook = EBook(title, author, year, genre, file_size)
        library.append(ebook)
        print(f"EBook '{title}' added successfully!")

def list_books(library):  # Accept library as parameter
    if not library: 
        print("No books available in the library.")
        return

    print("\nLibrary Catalog:")
    print("-" * 40)
    for index, book in enumerate(library, start=1):
        print(f"{index}. {book}")
    print("-" * 40)
    print(f"Total books: {len(library)}\n")

def search_books_by_title(library):  # Accept library as parameter
    search_term = input("Enter the title or part of the title to search for: ").strip()
    
    if not search_term:
        print("Search term cannot be empty.")
        return

    search_term = search_term.lower()
    matches = [book for book in library if search_term in book.title.strip().lower()]
    
    if matches:
        print(f"\nFound {len(matches)} matching book(s):")
        for i, book in enumerate(matches, 1):
            print(f"{i}. {book}")
    else:
        print("\nNo books matched your search.")

def main():
    library = load_library_from_csv()  # Initialize library
    
    while True:
        print("\n--------Welcome to Book Manager App---------")
        print("1. Add Book")
        print("2. List All Books")
        print("3. Search Book by Title")
        print("4. Exit") 
        
        choice = input("Enter your choice (1/2/3/4): ")
          
        if choice == '1':
            add_book(library)  # Pass library
        elif choice == '2':
            list_books(library)  # Pass library
        elif choice == '3':
            search_books_by_title(library)  # Pass library
        elif choice == '4':
            save_library_to_csv(library)  # Pass library
            print("Library saved. Exiting the Program.")
            break
        else:
            print("Invalid choice, please select 1, 2, 3 or 4.")

if __name__ == "__main__":
    main()