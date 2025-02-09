class Responses:
    def Failure(Message) -> None:
        if Message:
            print(f"[-] Failed using Response: {Message}")

    def Passed(Message: str) -> None:
        if Message:
            print(f"[•] {Message}")