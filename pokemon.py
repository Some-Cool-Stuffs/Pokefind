import requests as Request;
import colorama as Colors;

# Variables

Pokedex: str = "https://pokeapi.co/api/v2/pokemon/"
Species: str = "https://pokeapi.co/api/v2/pokemon-species/"
Chain  : str = "https://pokeapi.co/api/v2/evolution-chain/"

# Classes

from responses import Responses;

class Pokemon:
    def findID(Name: str = None) -> int | None:
        if not Name:
            return Responses.Failure(Message="Tried searching ID of unknown Pokémon")

        Response: object = Request.get(Pokedex + Name)
        Code: int = Response.status_code

        if Code == 200:
            return Response.json()["id"]

        else:
            return Responses.Failure(Message=f"Unknown error, responded using code: {Code}")
    
    def findChainID(ID: str = None) -> int | None:
        if not ID:
            return Responses.Failure(Message="Tried searching chain ID using invalid Pokedex ID")

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
            return Responses.Failure(Message="Tried searching evo/devos using invalid Chain ID")
        
        Response: object = Request.get(Chain + str(ChainID))
        Code: int = Response.status_code

        # Someone kill me,
        # I'm going to scrape my friggen eyes out if I have to do this again.

        # UPDATE: I've recoded this like 4 times!

        # This project will be very helpful to me, so it's worth it I guess..!

        Responder: str = ""
        Stones: list = {
            "Dawn": Colors.Fore.CYAN,
            "Fire": Colors.Fore.RED,
            "Dusk": Colors.Fore.MAGENTA,
            "Ice": Colors.Fore.CYAN,
            "Leaf": Colors.Fore.GREEN,
            "Moon": Colors.Fore.LIGHTBLACK_EX,
            "Oval": Colors.Fore.LIGHTBLACK_EX,
            "Shiny": Colors.Fore.YELLOW,
            "Sun": Colors.Fore.RED,
            "Thunder": Colors.Fore.YELLOW,
            "Water": Colors.Fore.BLUE
        }

        if Code == 200:
            Data: list = Response.json()
            Evolutions: list = Data["chain"]
            
            Initial_Data: list = Evolutions["evolves_to"]
            Initial_Name: str = str(Evolutions["species"]["name"]).capitalize()
            Initial_Name_Formatted: str = Colors.Style.RESET_ALL + Colors.Style.BRIGHT + Initial_Name + Colors.Style.RESET_ALL

            def assignMessage(Level, Item):
                if Level != None:
                    return f"when LV. {Colors.Fore.YELLOW}{Level}{Colors.Style.RESET_ALL}"

                elif Item != None:
                    for Stone in Stones:
                        if str(Item).lower().find(Stone.lower()) != -1:
                            Formatted: str = str(Item).replace("-", " ").split()
                            Capitalized: str = [Word.capitalize() for Word in Formatted]

                            return f"using a {Colors.Style.BRIGHT}{Stones[Stone]}{" ".join(Capitalized)}{Colors.Style.RESET_ALL}"

                else:
                    return "by reaching high Friendship levels"

            if Initial_Data != []:
                Initial_Evolution_Data: list = Initial_Data[0]["evolution_details"]

                Initial_Level_Arrangement: int | None = Initial_Evolution_Data[0]["min_level"]
                Initial_Item_Arrangement: list | None = Initial_Evolution_Data[0]["item"]

                Initial_Level_Statement: str | None = Initial_Level_Arrangement if Initial_Level_Arrangement != None else None
                Initial_Item_Statement: str | None = Initial_Item_Arrangement["name"] if Initial_Item_Arrangement != None else None

                Responder += f"{Colors.Style.DIM} 1. {Colors.Style.RESET_ALL}{Initial_Name_Formatted} evolves "
                Responder += assignMessage(Level=Initial_Level_Statement, Item=Initial_Item_Statement) + "\n" if Initial_Name != "Eevee" else f"using ~{Colors.Style.BRIGHT}All Stones{Colors.Style.RESET_ALL}"

                Secondary_Data: list = Initial_Data[0]["evolves_to"]
                Secondary_Name: str = str(Initial_Data[0]["species"]["name"]).capitalize()

                if "eon" not in Secondary_Name.lower():
                    if Secondary_Data != []:
                        Secondary_Evolution_Data: list = Secondary_Data[0]["evolution_details"]

                        Secondary_Level_Arrangement: int | None = Secondary_Evolution_Data[0]["min_level"]
                        Secondary_Item_Arrangement: list | None = Secondary_Evolution_Data[0]["item"]

                        Secondary_Level_Statement: str | None = Secondary_Level_Arrangement if Secondary_Level_Arrangement != None else None
                        Secondary_Item_Statement: str | None = Secondary_Item_Arrangement["name"] if Secondary_Item_Arrangement != None else None

                        Responder += f"{Colors.Style.DIM} 2. {Colors.Style.RESET_ALL}{Colors.Style.BRIGHT}{Secondary_Name}{Colors.Style.RESET_ALL} evolves "
                        Responder += assignMessage(Level=Secondary_Level_Statement, Item=Secondary_Item_Statement) + "\n"

                        Responder += f"{Colors.Style.DIM} 3. {Colors.Style.RESET_ALL}{Colors.Style.BRIGHT}{str(Secondary_Data[0]["species"]["name"]).capitalize()}{Colors.Style.RESET_ALL} is {Initial_Name_Formatted}'s final evolution"

                    else:
                        Responder += f"{Colors.Style.DIM} 2. {Colors.Style.RESET_ALL}{Colors.Style.BRIGHT}{Secondary_Name}{Colors.Style.RESET_ALL} is {Colors.Style.RESET_ALL}{Initial_Name_Formatted}'s final evolution"

            else:
                Responder += f"{Colors.Style.DIM} 1. {Colors.Style.RESET_ALL}{Initial_Name_Formatted} does not evolve"

            print(Responder)
