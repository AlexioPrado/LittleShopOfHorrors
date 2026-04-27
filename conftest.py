import pytest

@pytest.fixture
def item():
    return {"name": "sword", "price": 6.70, "item_type": "weapon", "damage": 10, defense:0}