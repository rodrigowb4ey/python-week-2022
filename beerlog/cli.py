import typer
from beerlog.core import add_beer_to_db

main = typer.Typer(help="Beer management app")


@main.command("add")
def add(
    name: str,
    style: str,
    flavor: int = typer.Option(...),
    image: int = typer.Option(...),
    cost: int = typer.Option(...),
):
    """Adds a new beer to database"""
    if add_beer_to_db(name, style, flavor, image, cost):
        print("Beer added to database!")


@main.command("list")
def list_beers():
    """Lists all beers in database"""
    print(style)
