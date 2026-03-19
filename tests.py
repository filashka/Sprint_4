import pytest
from test_data import *


class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book(BOOK_DUNE)
        collector.add_new_book(BOOK_SHREK)
        assert len(collector.get_books_genre()) == 2

    def test_get_books_genre_returns_dict_with_books(self, books_genre):
        result = books_genre.get_books_genre()
        assert result == BOOKS_WITH_GENRES

    @pytest.mark.parametrize(
        'name',
        [
            'Гордость и предубеждение',
            'А',
            'А' * 40
        ]
    )
    def test_add_new_book_valid_name_length_added(self, collector, name):
        collector.add_new_book(name)
        assert name in collector.get_books_genre()

    @pytest.mark.parametrize(
        'name',
        [
            '',
            'А' * 41
        ]
    )
    def test_add_new_book_invalid_name_length_not_added(self, collector, name):
        collector.add_new_book(name)
        assert name not in collector.get_books_genre()

    def test_add_new_book_ignore_duplicate(self, collector):
        collector.add_new_book(BOOK_DUNE)
        collector.add_new_book(BOOK_DUNE)
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_valid_genre(self, collector):
        collector.add_new_book(BOOK_DUNE)
        collector.set_book_genre(BOOK_DUNE, GENRE_FANTASY)
        assert collector.get_book_genre(BOOK_DUNE) == GENRE_FANTASY

    def test_set_book_genre_nonexistent_book(self, collector):
        collector.add_new_book(BOOK_DUNE)
        assert collector.get_book_genre(BOOK_DUNE) == ''

    def test_get_book_genre_nonexistent_returns_none(self, collector):
        assert collector.get_book_genre(BOOK_DUNE) is None

    def test_get_books_with_specific_genre_get_books_with_fantasy_genre(self, books_genre):
        assert books_genre.get_books_with_specific_genre(GENRE_FANTASY) == [BOOK_DUNE]

    def test_get_books_for_children_excludes_age_rated(self, books_genre):
        children_books = books_genre.get_books_for_children()
        assert BOOK_DUNE in children_books and BOOK_SHREK in children_books and BOOK_IT not in children_books

    def test_add_book_in_favorites_add_one_book(self, books_genre):
        books_genre.add_book_in_favorites(BOOK_DUNE)
        assert BOOK_DUNE in books_genre.favorites
    
    def test_get_list_of_favorites_books_returns_list(self, books_genre):
        for name in BOOKS_WITH_GENRES:
            books_genre.add_book_in_favorites(name)
        result = books_genre.get_list_of_favorites_books()
        assert type(result) == list

    def test_add_book_in_favorites_ignore_duplicate(self, books_genre):
        books_genre.add_book_in_favorites(BOOK_DUNE)
        books_genre.add_book_in_favorites(BOOK_DUNE)
        assert books_genre.get_list_of_favorites_books().count(BOOK_DUNE) == 1

    def test_delete_book_from_favorites_delete_one_book(self, collector):
        collector.add_new_book(BOOK_DUNE)
        collector.add_book_in_favorites(BOOK_DUNE)
        collector.delete_book_from_favorites(BOOK_DUNE)
        assert BOOK_DUNE not in collector.get_list_of_favorites_books()
