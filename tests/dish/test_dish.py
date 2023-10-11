from src.models.dish import Dish  # noqa: F401, E261, E501
import pytest
from src.models.ingredient import Ingredient


# Req 2
def test_dish():
    teste = Dish('lasanha', 15.99)

    assert teste == Dish('lasanha', 15.99)
    assert teste.__repr__() == "Dish('lasanha', R$15.99)"
    assert teste.__hash__() == hash(Dish('lasanha', 15.99))
    assert teste.__hash__() != hash(Dish('lasanha', 5.99))
    assert teste.name == 'lasanha'
    assert teste.price == 15.99
    assert teste.recipe == {}

    with pytest.raises(ValueError):
        Dish('lasanha', -15.99)
    with pytest.raises(TypeError):
        Dish('lasanha', '15.99')

    ingredient_test = Ingredient('massa de lasanha')
    teste.add_ingredient_dependency(ingredient_test, 5)
    assert teste.get_restrictions()
    assert teste.get_ingredients()
    assert teste.recipe == {ingredient_test: 5}
