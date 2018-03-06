from BinarySearch import BinarySearch
import pytest


class TestBinarySearch:

    def test_creates_instance(self):
        input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

        bin = BinarySearch(input)

        assert bin is not None

    def test_contains_an_integer(self):
        input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        bs = BinarySearch(input)
        result = bs.contains(5)

        assert result is True

    def test_doesnot_contain_an_integer(self):
        input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

        bs = BinarySearch(input)
        result = bs.contains(22)

        assert result is False
