import uvicorn
from fastapi import FastAPI, HTTPException
# from models.trade import Trade
from models.user import User, UserToAdd
from db import fake_users #, fake_trades
from enums.error import ErrorDetail


app = FastAPI(
    title="Trading App"
)


@app.get("/users/all", response_model=list[User])
def get_users() -> list[dict]:
    return fake_users


@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int) -> User:
    for user in fake_users:
        if user.get("id") == user_id:
            return user
    raise HTTPException(status_code=404, detail=ErrorDetail.NOT_FOUND.value)


@app.post("/add_user", response_model=User)
def add_user(user: UserToAdd) -> dict:
    user_to_add = user.model_dump()
    user_id = fake_users[-1].get("id") + 1
    user_to_add["id"] = user_id
    if not user_to_add.get("degree"):
        user_to_add["degree"] = list()
    fake_users.append(user_to_add)
    return user_to_add


@app.patch("/users/{user_id}", response_model=User)
def change_user_name(user_id: int, new_name: str) -> User:
    for user in fake_users:
        if user.get("id") == user_id:
            user["name"] = new_name
            return user
    raise HTTPException(status_code=404, detail=ErrorDetail.NOT_FOUND.value)


# @app.get("/trades")
# def get_trades(limit: int = 1, offset: int = 1) -> list:
#     return fake_trades[offset:][:limit]
#
#
# @app.post("/trades", response_model=list[Trade])
# def add_trades(trades: list[dict]) -> dict:
#     fake_trades.extend(trades)
#     return {"status": 200, "data": fake_trades}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
