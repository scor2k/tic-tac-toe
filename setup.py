from setuptools import setup

setup(
    name="tic-tac-toe",
    version="0.1.0",
    description="Simple game",
    url="https://github.com/scor2k/tic-tac-toe",
    author="Scor2k",
    author_email="scor2k@gmail.com",
    license="MIT",
    packages=["tic_tac_toe"],
    entry_points={"console_scripts": ["tic-tac-toe=tic_tac_toe.cli:cli"]},
    zip_safe=False,
)