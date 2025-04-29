Project Structure
book_manager/
│
├── main.py         # Main application
├── book.py         # Book and EBook classes
├── file_handler.py # Saving and loading books
├── test_app.py     # Pytest tests
└── books.csv       # Your book database


Personal Book Manager
│
├── Core Classes
│    ├── Book
│    └── EBook (inherits Book)
│
├── Basic Functionalities
│    ├── add_book()
│    ├── remove_book()
│    ├── list_books()
│    ├── search_books_by_title()
│    ├── save_books_to_csv()
│    └── load_books_from_csv()
│
├── File Handling
│    ├── Save books to CSV
│    └── Load books from CSV
│
├── Exception Handling
│    ├── Handle missing file (books.csv)
│    └── Handle wrong user input
│
└── Bonus: Pytest
     ├── test_add_book()
     ├── test_save_books_to_csv()
     └── test_search_books_by_title()
