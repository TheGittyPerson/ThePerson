"""Pytest coverage for Inventory and Item behavior."""

from pathlib import Path
import sys

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from theperson.inventory import Inventory
from theperson.item import Electronic, Food, Item, Valuable, Weapon
from theperson.person import Person, Profile, Professional


@pytest.fixture()
def items() -> dict[str, Item]:
    return {
        "coin": Item(
            "Coin", value=1.5, stackable=True
        ),
        "apple": Food(
            "Apple", calories=95, cooked=False, brand="Farm", value=0.5
        ),
        "phone": Electronic(
            "Phone", brand="Acme", battery=80, value=500
        ),
        "ring": Valuable(
            "Ring", value=250
        ),
        "sword": Weapon(
            "Sword", value=100
        ),
        "token": Item(
            "Token", value=0.25, stackable=True
        ),
    }


@pytest.fixture()
def inventory() -> Inventory:
    return Inventory(max_capacity=6)


@pytest.fixture()
def person(inventory: Inventory) -> Person:
    return Person(
        profile=Profile(name="Inventory Tester", gender="non-binary"),
        professional=Professional(occupation="Code tester"),
        inventory=inventory,
    )


def populate_inventory(inv: Inventory, items: dict[str, Item]) -> None:
    inv.add_item(items["coin"], quantity=2)
    inv.add_item(items["apple"], quantity=1)
    inv.add_item(items["phone"])
    inv.add_item(items["ring"], quantity=2)


def test_item_basics() -> None:
    coin = Item(" Coin ", value=1, stackable=True)
    assert coin.name == "Coin"
    assert coin.value == 1.0
    assert coin.stackable is True
    assert coin.describe() == "Coin (value: 1.0)"
    assert str(coin) == "Coin"
    assert repr(coin).startswith("Item(")


def test_item_equality_and_hash() -> None:
    coin = Item("Coin", value=1)
    coin_same = Item("Coin", value=2, stackable=False)
    assert coin == coin_same
    assert hash(coin) == hash(coin_same)
    assert coin in {coin_same}
    assert coin != Food("Coin")


# noinspection PyTypeChecker
def test_item_validation_errors() -> None:
    with pytest.raises(ValueError):
        Item("")
    with pytest.raises(ValueError):
        Item("   ")
    with pytest.raises(ValueError):
        Item(123)
    with pytest.raises(TypeError):
        Item("Coin", value="gold")
    with pytest.raises(TypeError):
        Item("Coin", stackable="yes")


# noinspection PyTypeChecker
def test_food_and_electronic_validation() -> None:
    apple = Food("Apple", brand=" Farm ", value=0.5)
    assert apple.brand == "Farm"
    assert apple.stackable is True

    with pytest.raises(TypeError):
        Food("Apple", calories="a lot")
    with pytest.raises(TypeError):
        Food("Apple", cooked="yes")
    with pytest.raises(TypeError):
        Food("Apple", brand=123)
    with pytest.raises(ValueError):
        Food("Apple", brand="   ")

    phone = Electronic("Phone", brand="Acme", battery=80, value=500)
    assert phone.stackable is False

    with pytest.raises(TypeError):
        Electronic("Phone", brand=123)
    with pytest.raises(ValueError):
        Electronic("Phone", brand="")
    with pytest.raises(TypeError):
        Electronic("Phone", brand="Acme", battery="80")
    with pytest.raises(ValueError):
        Electronic("Phone", brand="Acme", battery=101)


# noinspection PyTypeChecker
def test_inventory_init_errors() -> None:
    with pytest.raises(TypeError):
        Inventory("ten")
    with pytest.raises(ValueError):
        Inventory(-1)


def test_inventory_empty_state(inventory: Inventory,
                               items: dict[str, Item],
                               capsys: pytest.CaptureFixture[str]) -> None:
    assert inventory.is_empty() is True
    assert inventory.item_count == 0
    assert inventory.unique_item_types == 0
    assert inventory.get_items() == "Inventory is empty"
    assert inventory.sort_items() == "Inventory is empty"
    assert str(inventory) == "Inventory is empty"
    assert inventory.is_full() is False

    inventory.list_items()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Inventory is empty"

    assert inventory.has_item(items["coin"]) is False
    assert inventory.get_quantity(items["coin"]) == 0
    assert inventory.get_quantity(items["ring"]) == 0


# noinspection PyTypeChecker
def test_inventory_add_item_errors(inventory: Inventory,
                                   items: dict[str, Item]) -> None:
    with pytest.raises(TypeError):
        inventory.add_item("not_item", 1)
    with pytest.raises(TypeError):
        inventory.add_item(items["coin"], "1")
    with pytest.raises(ValueError):
        inventory.add_item(items["coin"], 0)
    with pytest.raises(ValueError):
        inventory.add_item(items["coin"], -1)


def test_inventory_add_and_counts(inventory: Inventory,
                                  items: dict[str, Item]) -> None:
    populate_inventory(inventory, items)

    assert inventory.item_count == 6
    assert inventory.unique_item_types == 4
    assert inventory.is_full() is True
    assert inventory.is_empty() is False
    assert inventory.has_item(items["coin"]) is True
    assert inventory.has_item(items["phone"]) is True
    assert inventory.has_item(items["sword"]) is False
    assert inventory.get_quantity(items["coin"]) == 2
    assert inventory.get_quantity(items["ring"]) == 2
    assert inventory.get_quantity(items["sword"]) == 0


def test_inventory_get_items_and_repr(
        inventory: Inventory,
        items: dict[str, Item],
        capsys: pytest.CaptureFixture[str]
) -> None:
    populate_inventory(inventory, items)

    expected_items = "\n".join(
        [
            "Apple (value: 0.5) x1",
            "Coin (value: 1.5) x2",
            "Phone (value: 500.0)",
            "Ring (value: 250.0)",
            "Ring (value: 250.0)",
        ]
    )
    assert inventory.get_items() == expected_items
    assert inventory.sort_items() == expected_items
    assert str(inventory) == expected_items

    repr_text = repr(inventory)
    assert repr_text.startswith("Inventory(")
    assert f"max_capacity={inventory.max_capacity}" in repr_text

    inventory.list_items()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_items


def test_inventory_filter_and_total_value(inventory: Inventory,
                                          items: dict[str, Item]) -> None:
    populate_inventory(inventory, items)

    assert inventory.filter_items(Food) == "Apple (value: 0.5) x1"
    assert inventory.filter_items(Electronic) == "Phone (value: 500.0)"
    assert inventory.filter_items(Weapon) == "No items of type Weapon found."
    assert inventory.total_value() == 1003.5


# noinspection PyTypeChecker
def test_inventory_remove_item_errors(inventory: Inventory,
                                      items: dict[str, Item]) -> None:
    populate_inventory(inventory, items)

    with pytest.raises(TypeError):
        inventory.remove_item("not_item", 1)
    with pytest.raises(TypeError):
        inventory.remove_item(items["coin"], "1")
    with pytest.raises(ValueError):
        inventory.remove_item(items["coin"], 0)
    with pytest.raises(ValueError):
        inventory.remove_item(items["sword"], 1)
    with pytest.raises(ValueError):
        inventory.remove_item(items["coin"], 99)


def test_inventory_remove_item_success(inventory: Inventory,
                                       items: dict[str, Item]) -> None:
    populate_inventory(inventory, items)

    inventory.remove_item(items["coin"], 1)
    assert inventory.get_quantity(items["coin"]) == 1
    inventory.remove_item(items["ring"], 1)
    assert inventory.get_quantity(items["ring"]) == 1
    assert inventory.item_count == 4


def test_inventory_remove_all_and_clear(inventory: Inventory,
                                        items: dict[str, Item]) -> None:
    populate_inventory(inventory, items)

    inventory.remove_all(items["coin"])
    assert inventory.get_quantity(items["coin"]) == 0
    assert inventory.has_item(items["coin"]) is False
    inventory.remove_all(items["ring"])
    assert inventory.get_quantity(items["ring"]) == 0
    assert inventory.item_count == 2
    assert (inventory.filter_items(Valuable)
            == "No items of type Valuable found.")

    inventory.clear()
    assert inventory.is_empty() is True
    assert inventory.item_count == 0
    assert inventory.unique_item_types == 0
    assert inventory.get_items() == "Inventory is empty"


def test_inventory_capacity_limits(items: dict[str, Item]) -> None:
    small_inv = Inventory(max_capacity=1)
    small_inv.add_item(items["token"], 1)
    assert small_inv.is_full() is True
    with pytest.raises(ValueError):
        small_inv.add_item(items["token"], 1)
    small_inv.remove_item(items["token"], 1)
    assert small_inv.is_empty() is True
    small_inv.remove_all(items["token"])
    assert small_inv.get_items() == "Inventory is empty"

    zero_inv = Inventory(max_capacity=0)
    assert zero_inv.is_full() is True
    assert zero_inv.is_empty() is True
    with pytest.raises(ValueError):
        zero_inv.add_item(items["token"], 1)


def test_person_inventory_integration(person: Person) -> None:
    assert person.inventory.max_capacity == 6
