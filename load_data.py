import pandas as pd
from sqlalchemy import create_engine

# CSV file se data read karo
df = pd.read_csv("data/transactions.csv")

# SQLite database connection banao
engine = create_engine("sqlite:///banking.db")

# Data ko SQL table mein save karo
df.to_sql(
    "transactions",
    engine,
    if_exists="replace",
    index=False
)

print("Data successfully loaded!")
print("Total rows:", len(df))