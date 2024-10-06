from colorama import Fore, Style, init

# Initialize colorama
init()

# Initialize a dictionary to store books
books = {}

def add_book():
    title = input(Fore.CYAN + "Enter book title: " + Style.RESET_ALL)
    author = input(Fore.CYAN + "Enter author: " + Style.RESET_ALL)
    year = input(Fore.CYAN + "Enter year: " + Style.RESET_ALL)
    genre = input(Fore.CYAN + "Enter genre: " + Style.RESET_ALL)
    
    book_details = [author, year, genre]
    books[title] = book_details
    
    print(Fore.GREEN + f'Book "{title}" added to the library!' + Style.RESET_ALL)

def view_books():
    if not books:
        print(Fore.YELLOW + "No books in the library." + Style.RESET_ALL)
        return
    
    print(Fore.BLUE + "Your library:" + Style.RESET_ALL)
    for title, details in books.items():
        author, year, genre = details
        print(Fore.MAGENTA + f'- {title} by {author} ({year}) [{genre}]' + Style.RESET_ALL)

def search_book():
    title = input(Fore.CYAN + "Enter the book title you want to search for: " + Style.RESET_ALL)
    details = books.get(title)
    
    if details:
        author, year, genre = details
        print(Fore.GREEN + f'Found: {title} by {author} ({year}) [{genre}]' + Style.RESET_ALL)
    else:
        print(Fore.RED + f'Book "{title}" not found in the library.' + Style.RESET_ALL)

def update_book():
    title = input(Fore.CYAN + "Enter the book title you want to update: " + Style.RESET_ALL)
    details = books.get(title)
    
    if details:
        author, year, genre = details
        print(Fore.BLUE + f'Current details for "{title}":' + Style.RESET_ALL)
        print(Fore.YELLOW + f'Author: {author}' + Style.RESET_ALL)
        print(Fore.YELLOW + f'Year: {year}' + Style.RESET_ALL)
        print(Fore.YELLOW + f'Genre: {genre}' + Style.RESET_ALL)
        
        new_author = input(Fore.CYAN + f"Enter new author (or press Enter to keep '{author}'): " + Style.RESET_ALL) or author
        new_year = input(Fore.CYAN + f"Enter new year (or press Enter to keep '{year}'): " + Style.RESET_ALL) or year
        new_genre = input(Fore.CYAN + f"Enter new genre (or press Enter to keep '{genre}'): " + Style.RESET_ALL) or genre
        
        books[title] = [new_author, new_year, new_genre]
        print(Fore.GREEN + f'Book "{title}" updated successfully!' + Style.RESET_ALL)
    else:
        print(Fore.RED + f'Book "{title}" not found in the library.' + Style.RESET_ALL)

def delete_book():
    title = input(Fore.CYAN + "Enter the book title you want to delete: " + Style.RESET_ALL)
    
    if title in books:
        del books[title]
        print(Fore.GREEN + f'Book "{title}" has been deleted from the library.' + Style.RESET_ALL)
    else:
        print(Fore.RED + f'Book "{title}" not found in the library.' + Style.RESET_ALL)

def main_menu():
    while True:
        print(Fore.YELLOW + "\nWelcome to the Personal Library Management System" + Style.RESET_ALL)
        print(Fore.CYAN + "1. Add a Book" + Style.RESET_ALL)
        print(Fore.CYAN + "2. View Books" + Style.RESET_ALL)
        print(Fore.CYAN + "3. Search for a Book" + Style.RESET_ALL)
        print(Fore.CYAN + "4. Update a Book" + Style.RESET_ALL)
        print(Fore.CYAN + "5. Delete a Book" + Style.RESET_ALL)
        print(Fore.CYAN + "6. Exit" + Style.RESET_ALL)
        
        choice = input(Fore.CYAN + "Choose an option (1-6): " + Style.RESET_ALL)
        
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
            print(Fore.GREEN + "Exiting the program." + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Invalid choice. Please enter a number between 1 and 6." + Style.RESET_ALL)

# Call the main menu to start the program
if __name__ == "__main__":
    main_menu()
