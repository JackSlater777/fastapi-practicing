import uvicorn
from fastapi import FastAPI
from models.trade import Trade
from models.user import User


app = FastAPI(
    title="Trading App"
)


fake_users = [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "investor", "name": "John"},
    {"id": 3, "role": "trader", "name": "Matt"}
]


@app.get("/users/all", response_model=list[User])
def get_users() -> list[dict]:
    return fake_users


@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int) -> User:
    return next(filter(lambda user: user.get("id") == user_id, fake_users))


@app.patch("/users/{user_id}", response_model=User)
def change_user_name(user_id: int, new_name: str) -> User:
    current_user = next(filter(lambda user: user.get("id") == user_id, fake_users))
    current_user["name"] = new_name
    return current_user


fake_trades = [
    {"id": 1, "user_id": 1, "currency": "BTC", "side": "buy", "price": 123, "amount": 2.12},
    {"id": 2, "user_id": 1, "currency": "BTC", "side": "sell", "price": 125, "amount": 2.12}
]


@app.get("/trades")
def get_trades(limit: int = 1, offset: int = 1) -> list:
    return fake_trades[offset:][:limit]


@app.post("/trades", response_model=list[Trade])
def add_trades(trades: list[dict]) -> dict:
    fake_trades.extend(trades)
    return {"status": 200, "data": fake_trades}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
