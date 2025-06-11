from lib.string_builder import *

def test_string_builder():
    string_builder = StringBuilder()
    string_builder.add("Hello")
    assert string_builder.size() == 5
    assert string_builder.output() == "Hello"