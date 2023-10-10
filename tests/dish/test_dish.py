from src.models.dish import Dish  # noqa: F401, E261, E501
import pytest
from src.models.ingredient import Ingredient


# Req 2
def test_dish():
    with pytest.raises(ValueError):
        Dish('lasanha', -1)
    with pytest.raises(TypeError):
        Dish('lasanha', '15.00')

    teste = Dish('lasanha', 15.00)
    assert teste == Dish('lasanha', 15.00)
    assert teste.__repr__() == "Dish('lasanha', R$15.00)"
    assert teste.__hash__() == teste.__hash__()
    assert teste.__hash__() != hash(Dish('lasanha', 0.00))
    assert teste.name == 'lasanha'
    assert teste.recipe == {}

    ingredient_test = Ingredient('camarão')
    teste.add_ingredient_dependency(ingredient_test, 1)
    assert teste.get_restrictions()
    assert teste.get_ingredients()
    assert teste.recipe == {ingredient_test: 1}
