# -*- coding: UTF-8 -*-

import logging
import random
from datetime import datetime
import sys


class TicTacToe:
    def __init__(self):
        self.EMPTY = 0
        self.field = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.X = 1  # X
        self.O = 2  # O
        self.next = self.X

        random.seed(datetime.now())

    def __set_field(self, field: list):
        self.field = field

    def __print_player(self, player: int) -> str:
        if player == self.X:
            return 'X'
        if player == self.O:
            return 'O'
        return '_'

    @staticmethod
    def __coord_to_position(x: int, y: int) -> int:
        """
        Convert [0,0] -> 0, [0,2] -> 2, [1,0] -> 3, etc...
        :param x:  horizontal position 0..2
        :param y:  vertical position 0..2
        :return:
        """

        if x < 0 or x > 2 or y < 0 or y > 2:
            return -1

        if y == 0:
            return x
        if y == 1:
            return 3 + x
        return 6 + x

    @staticmethod
    def __position_to_coord(pos: int) -> [int, int]:
        """
        Convert 0 -> [0,0],  etc
        :return:  [int, int]
        """

        if pos < 0 or pos > 8:
            return [-1, -1]

        if pos < 3:
            return [pos, 0]
        if pos < 6:
            return [pos - 3, 1]

        return [pos - 6, 2]

    def __is_empty(self, pos: int) -> bool:
        return True if self.field[pos] == self.EMPTY else False

    def __next_random_move(self) -> int:
        """
         - choose random empty spot
        :return:
        """

        possible_moves = []
        for i in range(0, 9):
            if self.__is_empty(pos=i):
                possible_moves.append(i)

        if not possible_moves:
            return -1

        rnd = random.choice(possible_moves)
        logging.debug("RND: %d", rnd)
        return rnd

    def __update_field(self, turn: int) -> bool:
        """
        Update the field if possible, return True or False + change the next value
        :param turn:
        :return:
        """

        if self.field[turn] != self.EMPTY:
            logging.error("The field '{}' is not empty: '{}'".format(turn, self.field))
            return False

        self.field[turn] = self.next
        self.next = self.X if self.next == self.O else self.O
        return True

    def __print_field(self):
        print("~~~~~~~~~")
        for y in range(3):
            for x in range(3):
                print(" {} ".format(self.__print_player(self.field[self.__coord_to_position(x, y)])), end='')
            print("")
        print("~~~~~~~~~")

    def __check_winner(self) -> int:
        # horizontal lines
        if (self.field[0] == self.X or self.field[0] == self.O) and self.field[0] == self.field[1] and self.field[1] == self.field[2]:
            return self.field[0]
        if (self.field[3] == self.X or self.field[3] == self.O) and self.field[3] == self.field[4] and self.field[3] == self.field[5]:
            return self.field[3]
        if (self.field[6] == self.X or self.field[6] == self.O) and self.field[6] == self.field[7] and self.field[6] == self.field[8]:
            return self.field[6]

        # vertical lines
        if (self.field[0] == self.X or self.field[0] == self.O) and self.field[0] == self.field[3] and self.field[0] == self.field[6]:
            return self.field[0]
        if (self.field[1] == self.X or self.field[1] == self.O) and self.field[1] == self.field[4] and self.field[1] == self.field[7]:
            return self.field[1]
        if (self.field[2] == self.X or self.field[2] == self.O) and self.field[2] == self.field[5] and self.field[2] == self.field[8]:
            return self.field[2]

        # diagonal lines
        if (self.field[0] == self.X or self.field[0] == self.O) and self.field[0] == self.field[4] and self.field[0] == self.field[8]:
            return self.field[0]
        if (self.field[2] == self.X or self.field[2] == self.O) and self.field[2] == self.field[4] and self.field[2] == self.field[6]:
            return self.field[2]

        # no winner
        return self.EMPTY

    def play_random_game(self):
        """
        Play random game, Both X & O are random
        :return:
        """

        for i in range(9):
            current_player = self.next
            random_move = self.__next_random_move()
            if random_move == -1:
                logging.error("No empty moves")
                sys.exit(1)
            print("Step: {}. Next turn: {} | '{}' -> '{}'".format(i + 1, self.__print_player(self.next), self.__print_player(self.next),
                                                                  self.__position_to_coord(random_move)))
            self.__update_field(turn=random_move)
            if self.__check_winner() != self.EMPTY:
                print("WE HAVE THE WINNER!\n{}".format(self.__print_player(current_player)))
                self.__print_field()
                sys.exit(0)
