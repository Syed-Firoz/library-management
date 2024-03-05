from django.test import TestCase
from .models import Book
from django.db.utils import IntegrityError

class BookModelTestCase(TestCase):
    def setUp(self):
        # Create a book for testing
        self.book = Book.objects.create(
            book_name='Test Book',
            author='Test Author',
            pages=200,
            published_year=2022
        )

    def test_duplicate_book(self):
        # Attempt to create a duplicate book with the same name and author
        with self.assertRaises(IntegrityError):
            duplicate_book = Book(
                book_name='Test Book',
                author='Test Author',
                pages=300,
                published_year=2020
            )
            duplicate_book.save()

    def test_non_duplicate_book(self):
        # Attempt to create a non-duplicate book with a different name and author
        non_duplicate_book = Book(
            book_name='Another Book',
            author='Another Author',
            pages=300,
            published_year=2020
        )
        # No exception should be raised
        non_duplicate_book.save()
