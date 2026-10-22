import pandas as pd

df = pd.read_csv("data/transactions.csv")

df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

df = df.drop_duplicates(
    subset="transaction_id"
)

df = df.dropna(
    subset=[
        "transaction_id",
        "transaction_date",
        "channel",
        "status"
    ]
)

df = df[
    (df["amount"] > 0)
    & (df["processing_time_sec"] >= 0)
]

df.to_csv("data/transactions.csv", index=False)

print("Clean data shape:", df.shape)                       
print(df.isnull().sum())
