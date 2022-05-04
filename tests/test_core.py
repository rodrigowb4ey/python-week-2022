from beerlog.core import add_beer_to_db, get_beers_from_db

def test_add_beer_to_db():
    assert add_beer_to_db("Blue Moon", "Witbier", 10, 3, 6)

def test_get_beers_from_db():
    results = get_beers_from_db()
    assert len(results) > 0

