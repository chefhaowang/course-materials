# Global variables for books and members
library_books = []
library_members = []
checked_out_books = {}


def add_book(title, author, year):
    """Add a book to the library."""
    book = {
        'title': title,
        'author': author,
        'year': year
    }
    library_books.append(book)
    print(f"Added book: {title} by {author} ({year})")


def remove_book(title):
    """Remove a book from the library."""
    global library_books
    library_books = [book for book in library_books if book['title'] != title]
    print(f"Removed book: {title}")


def list_books():
    """List all books in the library."""
    if not library_books:
        print("No books in the library.")
        return
    for book in library_books:
        print(f"{book['title']} by {book['author']} ({book['year']})")


def add_member(name, member_id):
    """Add a member to the library."""
    member = {
        'name': name,
        'member_id': member_id
    }
    library_members.append(member)
    print(f"Added member: {name} with ID {member_id}")


def remove_member(member_id):
    """Remove a member from the library."""
    global library_members
    library_members = [
        member for member in library_members if member['member_id'] != member_id]
    print(f"Removed member with ID {member_id}")


def list_members():
    """List all members of the library."""
    if not library_members:
        print("No members in the library.")
        return
    for member in library_members:
        print(f"{member['name']} (ID: {member['member_id']})")


def check_out_book(member_id, book_title):
    """Check out a book to a member."""
    global checked_out_books
    book = next(
        (book for book in library_books if book['title'] == book_title), None)
    if book:
        if member_id not in checked_out_books:
            checked_out_books[member_id] = []
        checked_out_books[member_id].append(book)
        library_books.remove(book)
        print(f"{book_title} has been checked out to member ID {member_id}.")
    else:
        print(f"Book {book_title} not found in the library.")


def return_book(member_id, book_title):
    """Return a checked out book."""
    if member_id in checked_out_books:
        book = next(
            (book for book in checked_out_books[member_id] if book['title'] == book_title), None)
        if book:
            checked_out_books[member_id].remove(book)
            library_books.append(book)
            print(f"{book_title} has been returned by member ID {member_id}.")
        else:
            print(f"{book_title} was not checked out by member ID {member_id}.")
    else:
        print(f"Member ID {member_id} has no checked out books.")


def main():
    """Main function to run the library system."""
    while True:
        print("\nLibrary Menu:")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Add Member")
        print("5. Remove Member")
        print("6. List Members")
        print("7. Check Out Book")
        print("8. Return Book")
        print("9. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            year = input("Enter year of publication: ")
            add_book(title, author, year)
        elif choice == '2':
            title = input("Enter the title of the book to remove: ")
            remove_book(title)
        elif choice == '3':
            list_books()
        elif choice == '4':
            name = input("Enter member name: ")
            member_id = input("Enter member ID: ")
            add_member(name, member_id)
        elif choice == '5':
            member_id = input("Enter member ID to remove: ")
            remove_member(member_id)
        elif choice == '6':
            list_members()
        elif choice == '7':
            member_id = input("Enter member ID: ")
            book_title = input("Enter the title of the book to check out: ")
            check_out_book(member_id, book_title)
        elif choice == '8':
            member_id = input("Enter member ID: ")
            book_title = input("Enter the title of the book to return: ")
            return_book(member_id, book_title)
        elif choice == '9':
            print("Exiting the library system.")
            break
        else:
            print("Invalid choice. Please choose again.")


# Run the main function
if __name__ == "__main__":
    main()
