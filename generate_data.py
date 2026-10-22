import pandas as pd
import numpy as np
from pathlib import Path

np.random.seed(42)

n = 10000

channels = ["UPI", "Card", "NEFT", "IMPS"]
statuses = ["Success", "Failed", "Pending"]

df = pd.DataFrame({
    "transaction_id": range(1, n + 1),
    "transaction_date": pd.to_datetime(
        np.random.choice(
            pd.date_range("2026-01-01", periods=90),
            n
        )
    ),
    "channel": np.random.choice(channels, n),
    "amount": np.random.randint(100, 50000, n),
    "status": np.random.choice(
        statuses, n, p=[0.92, 0.05, 0.03]
    ),
    "processing_time_sec": np.random.randint(1, 121, n),
    "branch": np.random.choice(
        ["Mumbai", "Delhi", "Ranchi", "Patna"], n
    )
})

output_dir = Path("data")
output_dir.mkdir(parents=True, exist_ok=True)
df.to_csv(output_dir / "transactions.csv", index=False)

print(df.head())
print("Total rows:", len(df))