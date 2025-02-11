import requests as Request;

# Variables

Pokedex: str = "https://pokeapi.co/api/v2/pokemon/"
Species: str = "https://pokeapi.co/api/v2/pokemon-species/"
Chain  : str = "https://pokeapi.co/api/v2/evolution-chain/"


# Classes

from responses import Responses;

class Pokemon:
    def findID(Name: str = None) -> int | None:
        if not Name:
            return Responses.Failure(Message="Attempted to find ID of invalid Pokemon")

        Response: object = Request.get(Pokedex + Name)
        Code: int = Response.status_code

        if Code == 200:
            return Response.json()["id"]

        else:
            return Responses.Failure(Message=f"Unknown error, responded using code: {Code}")
    
    def findChainID(ID: str = None) -> int | None:
        if not ID:
            return Responses.Failure(Message="Attempted to find chain ID using invalid Pokedex ID")

        Response: object = Request.get(Species + ID)
        Code: int = Response.status_code

        if Code == 200:
            Data: list = Response.json()
            URL: str = Data["evolution_chain"]["url"]

            return int(URL.rsplit("/", 2)[-2])
        
        else:
            return Responses.Failure(Message=f"Unknown error, responded using code: {Code}")

    def findEvolutions(ChainID: int = None) -> str | None:
        if not ChainID:
            return Responses.Failure(Message="Attempted to find evolutions using an invalid Chain ID")
        
        Response: object = Request.get(Chain + str(ChainID))
        Code: int = Response.status_code

        # Someone kill me,
        # I'm going to scrape my friggen eyes out if I have to do this again.

        # This project will be very helpful to me, so it's worth it I guess..!

        # Ignore how bad this code is LOL, it could be fixed in a later update

        if Code == 200:
            Data: list = Response.json()
            Evos: list = Data["chain"]
            Responder: str = ""

            First: list = str(Evos["species"]["name"]).capitalize()
            Responder += f"\n1. {First}\n"

            if Evos["evolves_to"] != []:
                Second: list = str(Evos["evolves_to"][0]["species"]["name"]).capitalize()
                SLevel: int = str(Evos["evolves_to"][0]["evolution_details"][0]["min_level"])
                Responder += f"2. {Second} - Level: {SLevel}\n"

                if Evos["evolves_to"][0]["evolves_to"] != []:
                    Third: list = str(Evos["evolves_to"][0]["evolves_to"][0]["species"]["name"]).capitalize()
                    TLevel: int = str(Evos["evolves_to"][0]["evolves_to"][0]["evolution_details"][0]["min_level"])
                    Responder += f"3. {Third} - Level: {TLevel}\n"

            return Responder
        
        else:
            return Responses.Failure(Message=f"Unknown error, responded using code: {Code}")
