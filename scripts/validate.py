import pandas as pd
from sqlalchemy import create_engine

import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

print("Running validation checks...\n")

# =====================
# Check 1: Negative yields
# =====================
df_yields = pd.read_sql("fact_yields", engine)
if (df_yields["yield_kg"] < 0).any():
    print("❌ Negative yields found")
else:
    print("✅ No negative yields")

# =====================
# Check 2: Loan amount > 0
# =====================
df_loans = pd.read_sql("fact_loans", engine)
if (df_loans["loan_amount"] <= 0).any():
    print("❌ Invalid loan amounts")
else:
    print("✅ Loan amounts valid")

# =====================
# Check 3: Repayment rate <= 1
# =====================
if (df_loans["repayment_rate"] > 1).any():
    print("❌ Repayment rate above 1 detected")
else:
    print("✅ Repayment rates valid")

# =====================
# Check 4: Null foreign keys
# =====================
if df_yields["farmer_id"].isnull().any():
    print("❌ Null farmer_id in fact_yields")
else:
    print("✅ No null farmer_id")

print("\nValidation complete.")