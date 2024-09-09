class Book:
    """Class to represent a book in the library."""

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"


class Member:
    """Class to represent a library member."""

    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.checked_out_books = []

    def check_out_book(self, book):
        self.checked_out_books.append(book)
        print(f"{self.name} checked out {book}.")

    def return_book(self, book_title):
        book = next(
            (book for book in self.checked_out_books if book.title == book_title), None)
        if book:
            self.checked_out_books.remove(book)
            print(f"{self.name} returned {book}.")
            return book
        else:
            print(f"{book_title} not found in {
                  self.name}'s checked out books.")
            return None

    def __str__(self):
        return f"{self.name} (ID: {self.member_id})"


class Library:
    """Class to represent the library system."""
    
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added book: {book}")

    def remove_book(self, title):
        book = next((book for book in self.books if book.title == title), None)
        if book:
            self.books.remove(book)
            print(f"Removed book: {book}")
        else:
            print(f"Book {title} not found in the library.")

    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)

    def add_member(self, member):
        self.members.append(member)
        print(f"Added member: {member}")

    def remove_member(self, member_id):
        member = next(
            (member for member in self.members if member.member_id == member_id), None)
        if member:
            self.members.remove(member)
            print(f"Removed member: {member}")
        else:
            print(f"Member with ID {member_id} not found.")

    def list_members(self):
        if not self.members:
            print("No members in the library.")
        else:
            for member in self.members:
                print(member)

    def check_out_book(self, member_id, book_title):
        member = next(
            (member for member in self.members if member.member_id == member_id), None)
        if not member:
            print(f"Member with ID {member_id} not found.")
            return

        book = next(
            (book for book in self.books if book.title == book_title), None)
        if book:
            self.books.remove(book)
            member.check_out_book(book)
        else:
            print(f"Book {book_title} not found in the library.")

    def return_book(self, member_id, book_title):
        member = next(
            (member for member in self.members if member.member_id == member_id), None)
        if not member:
            print(f"Member with ID {member_id} not found.")
            return

        book = member.return_book(book_title)
        if book:
            self.books.append(book)

# Main function
def main():
    """Main function to run the library system."""
    library = Library()

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
            book = Book(title, author, year)
            library.add_book(book)
        elif choice == '2':
            title = input("Enter the title of the book to remove: ")
            library.remove_book(title)
        elif choice == '3':
            library.list_books()
        elif choice == '4':
            name = input("Enter member name: ")
            member_id = input("Enter member ID: ")
            member = Member(name, member_id)
            library.add_member(member)
        elif choice == '5':
            member_id = input("Enter member ID to remove: ")
            library.remove_member(member_id)
        elif choice == '6':
            library.list_members()
        elif choice == '7':
            member_id = input("Enter member ID: ")
            book_title = input("Enter the title of the book to check out: ")
            library.check_out_book(member_id, book_title)
        elif choice == '8':
            member_id = input("Enter member ID: ")
            book_title = input("Enter the title of the book to return: ")
            library.return_book(member_id, book_title)
        elif choice == '9':
            print("Exiting the library system.")
            break
        else:
            print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    main()
