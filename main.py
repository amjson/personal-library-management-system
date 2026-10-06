"""
start by creating an empty list, this will act as our temporary storage of anything that is added by the user.
we shall be using dictionaries to store, transport details of the book to/from the storage list
"""
books = []

# ======================================================================
# ======= Creating functions that will manipulate the book list ========
# ======================================================================

# ---------- adding a new book
def add_book():
    # getting user inputs
    book_id = input("Enter book ID: ")
    title = input("Enter title: ")
    author = input("Enter author: ")
    year = input("Enter year: ")

    # Create a flag
    duplicate = False

    # loop through the list to check for a duplicate ID
    for check_book in books:
        if check_book["id"] == book_id:
            print("\nA book with this ID already exists.")

            # flag variable to show we found a duplicate
            duplicate = True
            break

    # when no duplicate was found proceed
    if duplicate == False:
        # create a dictionary and save the inputs inside it (key => value)
        book = {
            "id": book_id,
            "title": title,
            "author": author,
            "year": year
        }

        # add the dictionary to the list
        books.append(book)

        # print a successful message
        print("\nBook Added successfully.")


# ---------- viewing books from the list
def view_books():
    # loop through the list
    for book in books:
        print(book["id"], "|", book["title"], "|", book["author"], "|", book["year"])


# ---------- searching books inside the list
def search_book():
    # getting book title from the user
    search_by_title = input("Enter book Title: ")

    # a flag variable to show we haven't found our match
    found = False

    # Loop through the list to search
    for book in books:
        # check users title matches the title inside the dictionary & display the book
        if book["title"] == search_by_title:
            print(book["id"], "|", book["title"], "|", book["author"], "|", book["year"])

            # a flag variable to show we found our match
            found = True
            break

    if found == False:
        # if not found
        print("\nbook not found")


# ---------- updating book info in the list
def update_book():
    # get book id from the user
    search_by_id = input("Enter book ID: ")

    # a flag variable to show we haven't found our match
    found = False

    # loop through the list
    for book in books:
        # check if the id matches the one we have inside the list
        if book["id"] == search_by_id:
            # ask user for new input
            new_title = input("Enter new title: ")
            new_author = input("Enter new author: ")
            new_year = input("Enter new year: ")

            # replace the old one with the newly entered info
            book["title"] = new_title
            book["author"] = new_author
            book["year"] = new_year

            # print a successful message
            print("\nBook updated successfully.")

            # a flag variable to show we found our match
            found = True
            break

    if found == False:
        # if not found
        print("\nbook not found")


# ---------- deleting/removing a book from the list
def delete_book():
    # get book id from the user
    search_by_id = input("Enter book ID: ")

    # a flag variable to show we haven't found our match
    found = False

    # loop through the list
    for book in books:
        # check if the id matches the one we have inside the list
        if book["id"] == search_by_id:

            books.remove(book)

            # print a successful message
            print("\nBook deleted successfully.")

            # a flag variable to show we found our match
            found = True
            break

    if found == False:
        # if not found
        print("\nbook not found")


while True:
    print("\n========================================")
    print("WELCOME TO MY PERSONAL LIBRARY")
    print("========================================")

    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Update Book")
    print("5. Delete Book")
    print("6. Exit")

    choice = input("\nEnter your choice: ")
    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        update_book()

    elif choice == "5":
        delete_book()

    elif choice == "6":
        break

    else:
        print("please enter a valid choice")