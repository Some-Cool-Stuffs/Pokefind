"""

    Ideas:

    - Use Pokemon API to search for Pokemon
    - Extract evolution from search
    - Use a loop to keep asking what Pokemon

"""

# Classes

from pokemon import Pokemon;
from responses import Responses;


# Variables

Running: bool = True


# Conditioned looping

while Running:
    Choice: str = input("Evolutions of Pokemon <Name: string>: ").lower()

    if Choice == "dip" or Choice == "close":
        Running = False

    else:
        try:
            ID: int = Pokemon.findID(Choice)
            Chain: str = Pokemon.findEvolutions(Pokemon.findChainID(str(ID)))

            print(Chain)

        except RuntimeError as Issue:
            Responses.Failure(Issue)