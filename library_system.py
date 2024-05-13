def add_book(library, title, author):
    new_book = (title, author)
    if new_book in library:
        print(f"The book '{title}' by {author} already exists in the library.")
    else:
        library.append(new_book)
        print(f"The book '{title}' by {author} has been successfully added to the library.")

# Existing Library Data
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]


add_book(library, "1984", "George Orwell")  # Output: The book '1984' by George Orwell already exists in the library.
add_book(library, "To Kill a Mockingbird", "Harper Lee")  # Output: The book 'To Kill a Mockingbird' by Harper Lee has been successfully added to the library.

# Print updated library
print(library)
