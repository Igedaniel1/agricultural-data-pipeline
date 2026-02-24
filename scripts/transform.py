import pandas as pd

# Load raw data
farmers = pd.read_csv("data/raw/farmers.csv")
yields = pd.read_csv("data/raw/yields.csv")
loans = pd.read_csv("data/raw/loans.csv")
weather = pd.read_csv("data/raw/weather.csv")

# ============================
# CLEAN FARMERS
# ============================
farmers["registration_date"] = pd.to_datetime(farmers["registration_date"])
farmers["age"] = farmers["age"].fillna(farmers["age"].median())

# Derived feature: age bucket
farmers["age_bucket"] = pd.cut(
    farmers["age"],
    bins=[0, 25, 35, 50, 100],
    labels=["18-25", "26-35", "36-50", "51+"]
)

# ============================
# CLEAN YIELDS
# ============================
yields["yield_per_hectare"] = yields["yield_kg"] / yields["area_hectares"]
yields["yield_per_hectare"] = yields["yield_per_hectare"].fillna(0)

# ============================
# CLEAN LOANS
# ============================
loans["disbursed_date"] = pd.to_datetime(loans["disbursed_date"])

loans["repayment_rate"] = loans["repaid_amount"] / loans["loan_amount"]
loans["repayment_rate"] = loans["repayment_rate"].fillna(0)

# Default flag
loans["default_flag"] = loans["status"].apply(lambda x: 1 if x == "Default" else 0)

# ============================
# CLEAN WEATHER
# ============================
weather["date"] = pd.to_datetime(weather["date"])
weather["rainfall_category"] = pd.cut(
    weather["rainfall_mm"],
    bins=[-1, 20, 100, 200],
    labels=["Low", "Medium", "High"]
)

# ============================
# SAVE PROCESSED DATA
# ============================
farmers.to_csv("data/processed/farmers_clean.csv", index=False)
yields.to_csv("data/processed/yields_clean.csv", index=False)
loans.to_csv("data/processed/loans_clean.csv", index=False)
weather.to_csv("data/processed/weather_clean.csv", index=False)

print("Transformation complete!")