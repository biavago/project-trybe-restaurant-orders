from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    teste = Ingredient('camarão')

    assert teste.__repr__() == "Ingredient('camarão')"
    assert teste.__hash__() == hash('camarão')
    