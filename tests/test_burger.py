from unittest.mock import Mock

from constants.burger_constants import BurgerConstants
from praktikum.burger import Burger


class TestBurger:
    def test_set_bun(self):
        mock_bun = Mock()
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self):
        mock_sauce = Mock()
        mock_filling = Mock()
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        assert len(burger.ingredients) == 2

    def test_remove_ingredient(self):
        mock_sauce = Mock()
        mock_filling = Mock()
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 1

    def test_move_ingredient(self):
        mock_sauce = Mock()
        mock_filling = Mock()
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.move_ingredient(1, 0)

        assert burger.ingredients[0] == mock_filling

    def test_get_price(self):
        mock_bun = Mock()
        mock_sauce = Mock()
        mock_filling = Mock()

        mock_bun.configure_mock(price=BurgerConstants.BUN_PRICE)
        mock_bun.get_price.return_value = BurgerConstants.BUN_PRICE

        mock_sauce.configure_mock(price=BurgerConstants.SAUCE_PRICE)
        mock_sauce.get_price.return_value = BurgerConstants.SAUCE_PRICE

        mock_filling.configure_mock(price=BurgerConstants.FILLING_PRICE)
        mock_filling.get_price.return_value = BurgerConstants.FILLING_PRICE

        mock_total_sum = sum((mock_bun.price * 2, mock_sauce.price, mock_filling.price))

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        actual_price = burger.get_price()

        assert actual_price == mock_total_sum

    def test_get_receipt(self):
        mock_bun = Mock()
        mock_sauce = Mock()
        mock_filling = Mock()

        mock_bun.configure_mock(name=BurgerConstants.BUN_NAME, price=BurgerConstants.BUN_PRICE)
        mock_bun.get_name.return_value = BurgerConstants.BUN_NAME
        mock_bun.get_price.return_value = BurgerConstants.BUN_PRICE

        mock_sauce.configure_mock(name=BurgerConstants.SAUCE_NAME, price=BurgerConstants.SAUCE_PRICE)
        mock_sauce.get_name.return_value = BurgerConstants.SAUCE_NAME
        mock_sauce.get_price.return_value = BurgerConstants.SAUCE_PRICE

        mock_filling.configure_mock(name=BurgerConstants.FILLING_NAME, price=BurgerConstants.FILLING_PRICE)
        mock_filling.get_name.return_value = BurgerConstants.FILLING_NAME
        mock_filling.get_price.return_value = BurgerConstants.FILLING_PRICE

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        actual_receipt = burger.get_receipt()

        assert all(name in actual_receipt for name in (BurgerConstants.BUN_NAME, BurgerConstants.SAUCE_NAME, BurgerConstants.FILLING_NAME))
