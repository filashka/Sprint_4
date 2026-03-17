import pytest


class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Тихий Дон')
        collector.add_new_book('Война и мир')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize(
        'name, is_correct',
        [
            ('Гордость и предубеждение', True),
            ('А', True),
            ('А' * 40, True),
            ('', False),
            ('А' * 41, False)
        ]
    )
    def test_add_new_book_check_name_length(self, collector, name, is_correct):
        collector.add_new_book(name)
        assert name in collector.get_books_genre() if is_correct else name not in collector.get_books_genre()


    def test_add_new_book_ignore_duplicate(self, collector):
        collector.add_new_book('Дюна')
        collector.add_new_book('Дюна')
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_valid_genre(self, collector):
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.get_book_genre('Дюна') == 'Фантастика'

    @pytest.mark.parametrize(
        'name, genre',
        [
            ('НесуществующаяКнига', 'Фантастика'),
            ('Дюна', 'Романтика'),
        ]
    )
    def test_set_book_genre_invalid_genre(self, collector, name, genre):
        collector.add_new_book('Дюна')
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre('Дюна') == ''

    def test_get_book_genre_nonexistent_returns_none(self, collector):
        assert collector.get_book_genre('Дюна') is None

    def test_get_books_with_specific_genre_get_books_with_fantasy_genre(self, books_genre):
        assert books_genre.get_books_with_specific_genre('Фантастика') == ['Дюна']

    def test_get_books_for_children_excludes_age_rated(self, books_genre):
        children_books = books_genre.get_books_for_children()
        assert 'Дюна' in children_books and 'Шрек' in children_books and 'Оно' not in children_books

    def test_add_book_in_favorites_and_get_list_add_one_book(self, collector):
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')
        assert 'Дюна' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_ignore_duplicate(self, collector):
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')
        collector.add_book_in_favorites('Дюна')
        assert collector.get_list_of_favorites_books().count('Дюна') == 1

    def test_delete_book_from_favorites_delete_one_book(self, collector):
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')
        collector.delete_book_from_favorites('Дюна')
        assert 'Дюна' not in collector.get_list_of_favorites_books()