def reverse_string(string):
    return string[::-1]

# Unit test
def test_reverse_string():
    assert reverse_string("Hello") == "olleH"
    assert reverse_string("GitHub Copilot") == "topiloC buHtiG"
    assert reverse_string("12345") == "54321"
    assert reverse_string("") == ""

test_reverse_string()
