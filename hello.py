import typer

def Main(
    Name: str, # User's name
    LastName: str = typer.option("", help="Фамилия пользователя."), # Familiya polzivatelya
    Formal: bool = typer.option(False, "--formal", "-f", help="Использовать формальное приветствие."),
):
    """
    Говорит "Привет" пользователю, опционально используя фамилию и формальный стиль.
    """
    if Formal:
        print(f"Добрый день, {Name} {LastName}!")
    else:
        print(f"Привет, {Name}!")

if __name__ == "__main__":
    typer.run(main)
