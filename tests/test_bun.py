from constants.bun_constants import BunConstants
from praktikum.bun import Bun


class TestBun:
    def test_get_name_to_new_bun(self):
        new_bun = Bun(BunConstants.BUN_NAME, BunConstants.BUN_PRICE)
        actual_name = new_bun.get_name()
        assert BunConstants.BUN_NAME == actual_name

    def test_get_price_to_new_bun(self):
        new_bun = Bun(BunConstants.BUN_NAME, BunConstants.BUN_PRICE)
        actual_price = new_bun.get_price()
        assert BunConstants.BUN_PRICE == actual_price
