from lib.counter import *

def test_counter_accuracy():
    counter = Counter()
    counter.add(5)
    assert counter.report() == "Counted to 5 so far."

 