import colorama as Colors;

# Classes

from pokemon import Pokemon;
from responses import Responses;

# Variables

Running: bool = True

# Conditioned looping

while Running:
    Choice: str = input(f"Evolutions of Pokémon {Colors.Style.DIM}<Name: string>{Colors.Style.RESET_ALL}: ").lower()
    print()

    if Choice == "dip" or Choice == "close":
        Running = False

    else:
        try:
            ID: int = Pokemon.findID(Choice)
            Chain: str = Pokemon.findEvolutions(Pokemon.findChainID(str(ID)))

            print()

        except RuntimeError as Issue:
            Responses.Failure(Issue)
