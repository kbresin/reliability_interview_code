from src.random_utils import RandomUtils

def test_is_palindrome():
    random_utils = RandomUtils()
    assert random_utils.is_palindrome("racecar")
