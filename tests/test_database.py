from praktikum.database import Database


class TestDatabase:
    def test_get_buns_list(self):
        database = Database()
        actual_list = database.available_buns()
        assert len(actual_list) == len(database.buns)
        assert actual_list == database.buns

    def test_get_ingredient_list(self):
        database = Database()
        actual_list = database.available_ingredients()
        assert len(actual_list) == len(database.ingredients)
        assert actual_list == database.ingredients


