from lib.check_codeword  import check_codeword

def test_check_codeword_horse():
    assert check_codeword("horse") == "Correct! Come in."

def test_check_codeword_close():
    assert check_codeword("house") == "Close, but nope."
    assert check_codeword("hose") == "Close, but nope."

def test_check_codeword_wrong():
    assert check_codeword("homes") == "WRONG!"