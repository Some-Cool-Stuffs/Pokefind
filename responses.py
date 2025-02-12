import colorama as Colors;

# Classes

class Responses:
    def Failure(Message) -> None:
        if Message:
            print(Colors.Fore.RED + Colors.Style.BRIGHT + f"Failed using Response: {Colors.Style.RESET_ALL}{Colors.Style.BRIGHT}{Message}{Colors.Style.RESET_ALL}")

    def Passed(Message: str) -> None:
        if Message:
            print(f"{Colors.Style.BRIGHT}{Message}{Colors.Style.RESET_ALL}")
