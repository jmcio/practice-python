#  test_hashtable.py

# def test_should_always_pass():
#     assert 2 + 2 == 4, "This is just a dummy test"

from hashtable import HashTable


def test_should_create_hashtable():
    assert HashTable() is not None
