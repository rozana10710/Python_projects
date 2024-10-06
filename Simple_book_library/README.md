For the following topics in python: Variables, built in functions, operators, strings, lists, tuples, dictionaries and sets
Project: Personal Library Management System
Objective: Create a simple library management system where users can add, search, update, and delete books from their personal library.

Features:
Add Books:

Prompt the user to enter details for a new book (title, author, year, genre).
Store this information in a dictionary with the title as the key.
View Books:

Display all books in the library.
Use lists to store the book details and print them in a user-friendly format.
Search for a Book:

Allow users to search for a book by title or author.
Return the book details if found, otherwise inform the user that the book is not in the library.
Update Book Information:

Let users update details of an existing book.
Use tuples to store the original details temporarily during the update process.
Delete a Book:

Provide an option to remove a book from the library.
Confirm the deletion with the user before proceeding.
User Interface:

Implement a simple text-based menu for the user to choose options.
Use loops to allow users to perform multiple actions without restarting the program.
Implementation Steps:
Setup: Create a new Python file (e.g., library_management.py).
Create Functions: Write functions for each feature (add, view, search, update, delete).
Use Data Structures:
Use a dictionary to store books.
Use lists to display book details.
User Input: Use input functions to gather user input and display options.
Loop and Control Flow: Implement a loop to keep the menu running until the user decides to exit.
Bonus Features:
Save the library data to a file (JSON or CSV) and load it when the program starts.
Add the ability to filter books by genre.

################THE CODE SHOULD PROMPT SOMETHING LIKE THAT################

Welcome to the Personal Library Management System
1. Add a Book
2. View Books
3. Search for a Book
4. Update a Book
5. Delete a Book
6. Exit

Choose an option: 1
Enter book title: The Alchemist
Enter author: Paulo Coelho
Enter year: 1988
Enter genre: Fiction
Book added!

Choose an option: 2
Your library:
- The Alchemist by Paulo Coelho (1988) [Fiction]


##############################END OF PROMPT##############################

For the colored version of the code in "simple_lib_colors.py", make sure to install the chroma module as in: pip install colorama


