BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id_, name, pages):
        """
        Конструктор класса Book.

        Args:
            id_ (int): Идентификатор книги.
            name (str): Название книги.
            pages (int): Количество страниц.
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __repr__(self):
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"

# TODO написать класс Library
class Library:
    def __init__(self, books=None):
        """
        Конструктор класса Library.

        Args:
            books (list, optional): Список книг. По умолчанию — пустой список.
        """
        if books is None:
            self.books = []
        else:
            self.books = books

    def get_next_book_id(self):
        """
        Возвращает идентификатор для добавления новой книги в библиотеку.

        Returns:
            int: Идентификатор для новой книги.
        """
        if not self.books:
            return 1
        last_book = self.books[-1]
        return last_book.id + 1

    def get_index_by_book_id(self, book_id):
        """
        Возвращает индекс книги в списке по её идентификатору.

        Args:
            book_id (int): Идентификатор книги.

        Returns:
            int: Индекс книги в списке.

        Raises:
            ValueError: Если книги с указанным id не существует.
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")

if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
