from . import TicTacToe


# 0 0 0
# 0 0 0
# 0 0 0

def test_convertor1():
    tests = [
        [0, 0, 0],
        [2, 0, 2],
        [0, 1, 3],
        [1, 1, 4],
        [0, 2, 6],
        [2, 2, 8]
    ]

    ttt = TicTacToe()

    for test in tests:
        assert ttt._TicTacToe__coord_to_position(test[0], test[1]) == test[2]


def test_convertor2():
    tests = [
        [0, 0, 0],
        [2, 0, 2],
        [0, 1, 3],
        [1, 1, 4],
        [0, 2, 6],
        [2, 2, 8]
    ]

    ttt = TicTacToe()

    for test in tests:
        assert ttt._TicTacToe__position_to_coord(test[2]) == [test[0], test[1]]


def test_win1():
    field = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    ttt = TicTacToe()
    ttt._TicTacToe__set_field(field)
    assert ttt._TicTacToe__check_winner() == 0


# horizont
def test_win2():
    field = [0, 0, 0, 0, 0, 0, 1, 1, 1]

    ttt = TicTacToe()
    ttt._TicTacToe__set_field(field)
    assert ttt._TicTacToe__check_winner() == 1


# vertical
def test_win3():
    field = [0, 1, 0, 0, 1, 0, 0, 1, 0]

    ttt = TicTacToe()
    ttt._TicTacToe__set_field(field)
    assert ttt._TicTacToe__check_winner() == 1


# diagonal
def test_win4():
    field = [1, 0, 0, 0, 1, 0, 0, 0, 1]

    ttt = TicTacToe()
    ttt._TicTacToe__set_field(field)
    assert ttt._TicTacToe__check_winner() == 1


def test_win5():
    field = [0, 0, 1, 0, 1, 0, 1, 0, 0]

    ttt = TicTacToe()
    ttt._TicTacToe__set_field(field)
    assert ttt._TicTacToe__check_winner() == 1
