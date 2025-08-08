from src.random_utils import RandomUtils

def test_is_palindrome():
    random_utils = RandomUtils()
    assert random_utils.is_palindrome("racecar")

def test_is_valid_email():
    random_utils = RandomUtils()
    assert random_utils.is_valid_email("racecar") is False
