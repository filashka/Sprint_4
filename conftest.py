import pytest
from main import BooksCollector

@pytest.fixture()
def collector():
    collector = BooksCollector()
    return collector
    
@pytest.fixture()
def books_genre(collector):
    collector.add_new_book('Дюна')
    collector.add_new_book('Оно')
    collector.add_new_book('Шрек')
    collector.set_book_genre('Дюна', 'Фантастика')
    collector.set_book_genre('Оно', 'Ужасы')
    collector.set_book_genre('Шрек', 'Мультфильмы')
    return collector