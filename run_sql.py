# import pandas as pd
# from sqlalchemy import create_engine

# # 1. Connect to SQLite database
# engine = create_engine("sqlite:///banking.db")

#********************************************************************************************************
# Transaction Analysis
# # 2. Write SQL query
# query = """
# SELECT
#     status,
#     COUNT(*) AS total_transactions,
#     SUM(amount) AS total_amount
# FROM transactions
# GROUP BY status;
# """

# # 3. Execute query and display result
# df = pd.read_sql(query, engine)

# print("Transaction Analysis")
# print(df)



#************************************************************************************************
#Channel-wise Success Rate
# import pandas as pd
# from sqlalchemy import create_engine

# engine = create_engine("sqlite:///banking.db")

# query = """
# SELECT
#     channel,
#     COUNT(*) AS total_transactions,

#     SUM(
#         CASE WHEN status = 'Success'
#              THEN 1 ELSE 0 END
#     ) AS successful_transactions,

#     ROUND(
#         100.0 * SUM(
#             CASE WHEN status = 'Success'
#                  THEN 1 ELSE 0 END
#         ) / COUNT(*),
#         2
#     ) AS success_rate

# FROM transactions
# GROUP BY channel
# ORDER BY success_rate DESC;
# """

# df = pd.read_sql(query, engine)

# print("Channel-wise Success Rate")
# print(df.to_string(index=False))

#*********************************************************************************************

## Daily transaction analysis
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///banking.db")

query1 = """
SELECT
    DATE(transaction_date) AS transaction_day,
    COUNT(*) AS total_transactions,
    SUM(
        CASE WHEN status = 'Failed'
             THEN 1 ELSE 0 END
    ) AS failed_transactions
FROM transactions
GROUP BY DATE(transaction_date)
ORDER BY transaction_day;
"""

daily_data = pd.read_sql(query1, engine)

print("\nDaily Transaction Analysis")
print(daily_data.to_string(index=False))

#**************************************************************************************************************
# Average processing time by channel
query2 = """
SELECT
    channel,
    ROUND(AVG(processing_time_sec), 2)
        AS avg_processing_time_sec,
    MAX(processing_time_sec)
        AS max_processing_time_sec
FROM transactions
GROUP BY channel
ORDER BY avg_processing_time_sec DESC;
"""

time_data = pd.read_sql(query2, engine)

print("\nProcessing Time Analysis")
print(time_data.to_string(index=False))
