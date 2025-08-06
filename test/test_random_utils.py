from src.random_utils import RandomUtils

def test_reverse_string():
    random_utils = RandomUtils()
    assert random_utils.reverse_string("Hello, World!") == "!dlroW ,olleH"