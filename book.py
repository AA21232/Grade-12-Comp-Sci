class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.isAvailable = True

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.ISBN}) - {'Available' if self.isAvailable else 'Borrowed'}"


class LibraryManager:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, ISBN):
        if any(book.ISBN == ISBN for book in self.books):
            print(f"Book with ISBN {ISBN} already exists.")
            return
        new_book = Book(title, author, ISBN)
        self.books.append(new_book)
        print(f"Book '{title}' added.")

    def remove_book(self, ISBN):
        for book in self.books:
            if book.ISBN == ISBN:
                self.books.remove(book)
                print(f"Book with ISBN {ISBN} removed.")
                return
        print(f"No book found with ISBN {ISBN}.")

    def view_books(self):
        if not self.books:
            print("The library is empty.")
            return
        print("\nLibrary Collection:")
        for book in self.books:
            print(f"- {book}")


def main():
    library = LibraryManager()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. View Books")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()
            ISBN = input("Enter book ISBN: ").strip()
            library.add_book(title, author, ISBN)

        elif choice == "2":
            ISBN = input("Enter the ISBN of the book to remove: ").strip()
            library.remove_book(ISBN)

        elif choice == "3":
            library.view_books()

        elif choice == "4":
            print("Exiting the Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
