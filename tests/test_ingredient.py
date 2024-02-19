from constants.ingredient_constants import IngredientConstants
from praktikum.ingredient import Ingredient


class TestIngredients:
    def test_get_name_to_new_ingredient(self):
        new_filling = Ingredient(IngredientConstants.INGREDIENT_FILLING['type'], IngredientConstants.INGREDIENT_FILLING['name'], IngredientConstants.INGREDIENT_FILLING['price'])
        actual_price = new_filling.get_price()
        assert IngredientConstants.INGREDIENT_FILLING['price'] == actual_price

    def test_get_price_to_new_ingredient(self):
        new_sauce = Ingredient(IngredientConstants.INGREDIENT_SAUCE['type'], IngredientConstants.INGREDIENT_SAUCE['name'], IngredientConstants.INGREDIENT_SAUCE['price'])
        actual_name = new_sauce.get_name()
        assert IngredientConstants.INGREDIENT_SAUCE['name'] == actual_name

    def test_get_type_to_new_ingredient(self):
        new_filling = Ingredient(IngredientConstants.INGREDIENT_FILLING['type'], IngredientConstants.INGREDIENT_FILLING['name'], IngredientConstants.INGREDIENT_FILLING['price'])
        actual_type = new_filling.get_type()
        assert IngredientConstants.INGREDIENT_FILLING['type'] == actual_type