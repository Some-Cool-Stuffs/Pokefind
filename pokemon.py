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

        if Code == 200:
            Data: list = Response.json()
            Evos: list = Data["chain"]
            Responder: str = ""

            First: list = str(Evos["species"]["name"]).capitalize()
            Evolver: list = Evos["evolves_to"]
            Initial_Details: list = Evolver[0]["evolution_details"]

            # Initial Additional Information

            Initial_Item: str = str(Initial_Details[0]["item"]).capitalize() if str(Initial_Details[0]["item"]) != None else None
            
            Responder += f"\n1. {First} -- Item: {Initial_Item}\n"

            if Evolver != []:
                Second: list = str(Evolver[0]["species"]["name"]).capitalize()
                Secondary_Evolver: list = Evolver[0]["evolves_to"]
                Secondary_Details: list = Evolver[0]["evolution_details"]
                Item_Data: list = Secondary_Evolver[0]["evolution_details"]

                # Additional Information

                Secondary_Item: str = ""
                Secondary_Level: str = str(Secondary_Details[0]["min_level"])
                Secondary_Item_Vocab: list | None = Item_Data[0]["item"]

                if Secondary_Item_Vocab:
                    Secondary_Item = str(Secondary_Item_Vocab["name"]).replace("-", " ")
                    Secondary_Item = Secondary_Item.split()
                    Secondary_Item = f"{Secondary_Item[0].capitalize()} {Secondary_Item[1].capitalize()}"

                Responder += f"2. {Second} -- Level: {Secondary_Level} -- Item: {Secondary_Item if Secondary_Item != "" else None}\n"

                if Secondary_Evolver != []:
                    Third: list = str(Secondary_Evolver[0]["species"]["name"]).capitalize()
                    Final_Details: list = Secondary_Evolver[0]["evolution_details"]

                    # Final Information

                    Final_Level: str = str(Final_Details[0]["min_level"])

                    Responder += f"3. {Third} -- Level: {Final_Level}\n"

            return Responder
