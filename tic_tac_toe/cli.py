# -*- coding: UTF-8 -*-

import logging
import click
from . import TicTacToe


logging.basicConfig(format="[%(asctime)s][%(levelname)s][%(filename)s] %(message)s", level=logging.INFO)


@click.group()
def cli():
    """Tic-tac-toe"""


@cli.command(name="play")
@click.option("--debug", help="debug mode on", type=bool, default=False, is_flag=True)
def play(debug: bool) -> None:
    if debug:
        logging.getLogger().setLevel(logging.DEBUG)

    ttt = TicTacToe()
    ttt.play_random_game()




if __name__ == "__main__":
    cli()
