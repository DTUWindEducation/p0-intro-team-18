"""Test your functions from Week 2 assignment.
"""
import preclass_assignment.functions as fxn


def test_greet(capsys):
    """Check that the greet function prints as expected"""
    # given
    name = 'world'  # who should we greet?
    # when
    fxn.greet(name)  # greet them
    captured = capsys.readouterr()  # capture what would have been printed to screen
    # then
    assert captured.out == 'Hello, world!\n'  # check that the greeting was what we expect



def test_goldilocks(capsys):
    """Check goldilocks returns expected output"""
    # given
    test_size1=139
    test_size2=140
    test_size3=151
    test_size4=150
    # when
    fxn.goldilocks(test_size1) 
    captured1 = capsys.readouterr()
    fxn.goldilocks(test_size2) 
    captured2 = capsys.readouterr()
    fxn.goldilocks(test_size3) 
    captured3 = capsys.readouterr()
    fxn.goldilocks(test_size4) 
    captured4 = capsys.readouterr()
    # then
    assert captured1.out == 'Too small.\n'
    assert captured2.out == 'Just right. :)\n'
    assert captured3.out == 'Too large.\n'
    assert captured4.out == 'Just right. :)\n'



def test_square_list():
    """Check square_list returns expected output"""
    # given
    inp = [1, 2, 3]  # test input to function
    exp_out = [1, 4, 9]  # expected output
    # when
    out = fxn.square_list(inp)  # actual output
    # then
    assert exp_out == out  # throw error if actual and expected output don't match


def test_fibonacci_stop():
    """Check fibonacci functions works as expected."""
    # given
    # given
    # when
    # then
    assert False  # TODO! Update the contents of this function so it correctly tests fibonacci_stop


def test_clean_pitch():
    """Check clean_pitch works as expected."""
    # given
    x = [-1, 2, 6, 95]  # "raw" pitch angle at four time steps
    status = [1, 0, 0, 0]  # status signal
    
    exp_out=[-999, 2, 6, 95]
    # when
    out = fxn.clean_pitch(x, status)  # actual output
    # then
    assert exp_out == out
