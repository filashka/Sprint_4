import pytest
from main import BooksCollector
from test_data import BOOKS_WITH_GENRES

@pytest.fixture()
def collector():
    collector = BooksCollector()
    return collector

@pytest.fixture()
def books_genre(collector):
    for name, genre in BOOKS_WITH_GENRES.items():
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
    return collector
