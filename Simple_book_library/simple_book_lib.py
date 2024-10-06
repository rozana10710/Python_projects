# Initialize a dictionary to store books
books = {}

def add_book():
    # Prompt user for book details
    title = input("Enter book title: ")
    author = input("Enter author: ")
    year = input("Enter year: ")
    genre = input("Enter genre: ")
    
    # Create a list for the new book
    book_details = [author, year, genre]
    
    # Store the list in the books dictionary with the title as the key
    books[title] = book_details
    
    print(f'Book "{title}" added to the library!')

def view_books():
    if not books:
        print("No books in the library.")
        return
    
    print("Your library:")
    for title, details in books.items():
        author, year, genre = details
        print(f'- {title} by {author} ({year}) [{genre}]')

def search_book():
    title = input("Enter the book title you want to search for: ")
    
    # Use the get method to find the book
    details = books.get(title)
    
    if details:
        author, year, genre = details
        print(f'Found: {title} by {author} ({year}) [{genre}]')
    else:
        print(f'Book "{title}" not found in the library.')

def update_book():
    title = input("Enter the book title you want to update: ")
    
    # Use the get method to find the book
    details = books.get(title)

def delete_book():
    title = input("Enter the book title you want to delete: ")
    
    # Check if the book exists in the dictionary
    if title in books:
        del books[title]  # Delete the book from the dictionary
        print(f'Book "{title}" has been deleted from the library.')
    else:
        print(f'Book "{title}" not found in the library.')
    
    if details:
        author, year, genre = details
        print(f'Current details for "{title}":')
        print(f'Author: {author}')
        print(f'Year: {year}')
        print(f'Genre: {genre}')
        
        # Prompt user for new values, or keep existing ones
        new_author = input(f"Enter new author (or press Enter to keep '{author}'): ") or author
        new_year = input(f"Enter new year (or press Enter to keep '{year}'): ") or year
        new_genre = input(f"Enter new genre (or press Enter to keep '{genre}'): ") or genre
        
        # Update the book details
        books[title] = [new_author, new_year, new_genre]
        print(f'Book "{title}" updated successfully!')
    else:
        print(f'Book "{title}" not found in the library.')

def main_menu():
    while True:
        print("\nWelcome to the Personal Library Management System")
        print("1. Add a Book")
        print("2. View Books")
        print("3. Search for a Book")
        print("4. Update a Book")
        print("5. Delete a Book")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")
        
        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            search_book()
        elif choice == '4':
            update_book()
        elif choice == '5':
            delete_book()
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

# Call the main menu to start the program
if __name__ == "__main__":
    main_menu()
