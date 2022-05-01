import typer
from typing import Optional
from beerlog.core import add_beer_to_db, get_beers_from_db

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
def list_beers(style: Optional[str] = None):
    """Lists all beers in database"""
    beers = get_beers_from_db()
    
    print(
        "ID" + " | " +
        "Name" + " | " +
        "Style" + " | " +
        "Flavor" + " | " +
        "Image" + " | " +
        "Cost" + " | " +
        "Rate"
    )
    for beer in beers:
        print(
            str(beer.id) + " | " +
            beer.name + " | " + 
            beer.style + " | " + 
            str(beer.flavor) + " | " + 
            str(beer.image) + " | " +  
            str(beer.cost) + " | " +  
            str(beer.rate)
        )

