# Splitwise Backend

# github link


# run api
endpoint 1 '/expenses' method= POST (adds expenses and updates balance of all users)
endpint  2 '/balances' method=GET (balance of all users)

payload for equal split
{
    {
    "paid_by": "u3",
    "amount": 1000,
    "users": ["u1", "u2", "u3", "u4"],
    "split":"equally"
}
}
payload for unequal split
{
    "paid_by": "u3",
    "amount": 1000,
    "users": ["u1", "u2", "u3", "u4"],
    "owes": {"u2": 370, "u1": 880, "u4": 0},
    "split":"unequally"
}
