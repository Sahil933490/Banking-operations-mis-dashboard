import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///banking.db")

df = pd.read_sql(
    "SELECT * FROM transactions",
    engine
)

df.to_csv(
    "data/transactions_for_powerbi.csv",
    index=False
)

print("Power BI data exported successfully!")
print("Total rows:", len(df))