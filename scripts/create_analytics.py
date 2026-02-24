import pandas as pd
from sqlalchemy import create_engine

import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

# =============================
# 1. Farmer Performance Summary
# =============================
query1 = """
SELECT 
    farmer_id,
    AVG(yield_per_hectare) AS avg_yield_per_hectare
FROM fact_yields
GROUP BY farmer_id
"""

df_farmer_perf = pd.read_sql(query1, engine)
df_farmer_perf.to_sql("agg_farmer_performance", engine, if_exists="replace", index=False)

# =============================
# 2. Regional Yield Summary
# =============================
query2 = """
SELECT 
    region_id,
    AVG(yield_per_hectare) AS avg_yield
FROM fact_yields
GROUP BY region_id
"""

df_region_perf = pd.read_sql(query2, engine)
df_region_perf.to_sql("agg_region_yield", engine, if_exists="replace", index=False)

# =============================
# 3. Loan Default Rate
# =============================
query3 = """
SELECT 
    COUNT(*) AS total_loans,
    SUM(default_flag) AS total_defaults,
    SUM(default_flag)::float / COUNT(*) AS default_rate
FROM fact_loans
"""

df_default = pd.read_sql(query3, engine)
df_default.to_sql("agg_loan_default_summary", engine, if_exists="replace", index=False)

print("Analytics tables created!")