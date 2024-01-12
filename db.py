fake_users = [
    {
        "id": 1,
        "role": "admin",
        "name": "Bob",
        "degree": [
            {
                "id": 1,
                "created_at": "2020-01-01T00:00:00.000Z",
                "type_degree": "expert"
            }
        ]
    },
    {
        "id": 2,
        "role": "investor",
        "name": "John"
    },
    {
        "id": 3,
        "role": "trader",
        "name": "Matt"
    }
]

fake_trades = [
    {
        "id": 1,
        "user_id": 1,
        "currency": "BTC",
        "side": "buy",
        "price": 123,
        "amount": 2.12
    },
    {
        "id": 2,
        "user_id": 1,
        "currency": "BTC",
        "side": "sell",
        "price": 125,
        "amount": 2.12
    }
]
