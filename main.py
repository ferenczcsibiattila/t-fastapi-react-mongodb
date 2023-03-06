from enum import Enum
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Category(Enum):
    TOOLS = 'tools'
    CONSUMABLES = 'consumables'


class Item(BaseModel):
    name: str
    price: float
    count: int
    id: int
    category: Category


items = {
    0: Item(name="Hammer", price=9.99, count=20, id=0, category=Category.TOOLS),
    1: Item(name="Pliers", price=20.2, count=20, id=1, category=Category.TOOLS),
    2: Item(name="Nails", price=20.2, count=200, id=2, category=Category.CONSUMABLES)
}

# FastAPI handles serialization and deserialization for us.
# We can simply use built in python and Pydantic types, in this case dict[int, Item]


@app.get("/")
def index() -> dict[str, dict[int, Item]]:
    return {"items": items}


@app.get("/items/{item_id}")
def query_item_by_id(item_id: int) -> Item:
    if item_id not in items:
        raise HTTPException(
            status_code=404, detail=f"Item with item_id={item_id} does not exist."
        )
    return items[item_id]


# function paramters that are not path parameters can be specified as query paramaters
Selection = dict[
    str, str | int | float | Category | None
]  # dictionary containing user's arguments


@app.get("/items/")
def query_item_by_parameters(
    name: str | None = None,
    price: float | None = None,
    count: int | None = None,
    category: Category | None = None
) -> dict[str, Selection | list[Item]]:
    def check_item(item: Item):
        """Check if item matches the query arguments from outer scope."""
        return all(  # Return True if all elements of the iterable are true (or if the iterable is empty).
            (
                name is None or item.name == name,
                price is None or item.price == price,
                count is None or item.count != count,
                category is None or item.category is category
            )
        )

    selection = [item for item in items.values() if check_item(item)]
    return {
        "query": {"name": name, "price": price, "count": count, "category": category},
        "selection": selection
    }


@app.post("/")
def add_item(item: Item) -> dict[str, Item]:
    if item.id in items:
        raise HTTPException(status_code=400,
                            detail=f"Item with item_id={item.id} already exists."
                            )

    items[item.id] = item
    return {"added:": item}


@app.put("/update/{item_id}")
def update(item_id: int,
           name: str | None = None,
           price: float | None = None,
           count: int | None = None,
           category: Category | None = None
           ) -> dict[str, Item]:
    if item_id not in items:
        raise HTTPException(status_code=404,
                            detail=f"Item woth item_id={item_id} does not exists."
                            )

    if all(info is None for info in (name, price, count)):
        raise HTTPException(status_code=400,
                            detail="No paramteres provided for update."
                            )

    item = items[item_id]

    if name is not None:
        item.name = name
    if price is not None:
        item.price = price
    if count is not None:
        item.count = count

    return {"updated": item}


@app.delete("/delete/{item_id}")
def delete_item(item_id: int) -> dict[str, Item]:

    if item_id not in items:
        raise HTTPException(status_code=404,
                            detail=f"Item woth item_id={item_id} does not exists."
                            )

    item = items.pop(item_id)
    return {"deleted": item}
