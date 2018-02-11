# -*- coding: utf-8 -*-
"""
Tests the numberwang module.
"""
import pytest
import numberwang
import builtins
from unittest import mock


def test_is_that_numberwang_true():
    """
    Ensures True is returned if a sentence is Numberwang.
    """
    with mock.patch('numberwang.random.randint', return_value=0):
        assert numberwang.is_that_numberwang('1')


def test_is_that_numberwang_invalid_sentence():
    """
    A ValueError exception is thrown if the sentence is invalid.
    """
    with pytest.raises(ValueError):
        numberwang.is_that_numberwang('not a number')


def test_main():
    """
    Ensure the good case results in print("That's Numberwang!")
    """
    with mock.patch('sys.argv', ['a', 'b', 'c', ]), \
            mock.patch('numberwang.is_that_numberwang', return_value=True), \
            mock.patch.object(builtins, 'print') as mock_print:
        numberwang.main()
        mock_print.assert_called_once_with("That's Numberwang!")


def test_main_valueerror():
    """
    Output useful information in the case of invalid input.
    """
    with mock.patch('sys.argv', ['a', 'b', 'c', ]), \
            mock.patch('numberwang.is_that_numberwang',
                       side_effect=ValueError), \
            mock.patch.object(builtins, 'print') as mock_print:
        numberwang.main()
        mock_print.assert_called_once_with("Input must contain a number.")
