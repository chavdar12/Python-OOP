class User:
    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        self.books = []

    def get_book(self, author: str, book_name: str, days_to_return: int, library):
        if book_name in library.books_available.get(author, []):
            library.books_available[author].remove(book_name)
            library.rented_books.setdefault(self.username, {})[book_name] = days_to_return
            self.books.append(book_name)
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        for rented in library.rented_books.values():
            if book_name in rented:
                return f'The book "{book_name}" is already rented and will be available in {rented[book_name]} days!'

    def return_book(self, author: str, book_name: str, library):
        if book_name not in self.books:
            return f"{self.username} doesn't have this book in his/her records!"
        self.books.remove(book_name)
        library.books_available.setdefault(author, []).append(book_name)
        del library.rented_books[self.username][book_name]

    def info(self):
        return ", ".join(sorted(self.books))

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"
