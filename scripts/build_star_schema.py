import pandas as pd
from sqlalchemy import create_engine

import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

# ======================
# DIM_REGION
# ======================
df_farmers = pd.read_sql("staging_farmers", engine)
regions = df_farmers[["region"]].drop_duplicates()
regions["region_id"] = range(1, len(regions) + 1)

regions.to_sql("dim_region", engine, if_exists="replace", index=False)

# Map region_id for later use
region_map = dict(zip(regions["region"], regions["region_id"]))

# ======================
# DIM_FARMER
# ======================
df_farmers["region"] = df_farmers["region"]
df_farmers.to_sql("dim_farmer", engine, if_exists="replace", index=False)

# ======================
# DIM_CROP
# ======================
df_yields = pd.read_sql("staging_yields", engine)
crops = df_yields[["crop"]].drop_duplicates()
crops["crop_id"] = range(1, len(crops) + 1)

crops.to_sql("dim_crop", engine, if_exists="replace", index=False)

crop_map = dict(zip(crops["crop"], crops["crop_id"]))

# ======================
# DIM_DATE
# ======================
dates = pd.concat([
    df_farmers["registration_date"],
    df_yields["season"].astype(str),
    pd.read_sql("staging_loans", engine)["disbursed_date"]
])

dates = pd.to_datetime(dates, errors="coerce").dropna().drop_duplicates()
dim_date = pd.DataFrame({
    "date": dates,
    "day": dates.dt.day,
    "month": dates.dt.month,
    "year": dates.dt.year,
    "quarter": dates.dt.quarter
})

dim_date.to_sql("dim_date", engine, if_exists="replace", index=False)

date_map = dict(zip(dim_date["date"].astype(str), dim_date.index + 1))

# ======================
# FACT_YIELDS
# ======================
df_yields["crop_id"] = df_yields["crop"].map(crop_map)
df_yields["region_id"] = df_farmers.set_index("farmer_id")["region"].map(region_map)
df_yields["date_id"] = pd.to_datetime(df_yields["season"]).astype(str).map(date_map)

df_yields.to_sql("fact_yields", engine, if_exists="replace", index=False)

# ======================
# FACT_LOANS
# ======================
df_loans = pd.read_sql("staging_loans", engine)
df_loans["disbursed_date_id"] = pd.to_datetime(df_loans["disbursed_date"]).astype(str).map(date_map)

df_loans.to_sql("fact_loans", engine, if_exists="replace", index=False)

# ======================
# FACT_WEATHER
# ======================
df_weather = pd.read_sql("staging_weather", engine)
df_weather["date_id"] = pd.to_datetime(df_weather["date"]).astype(str).map(date_map)
df_weather["region_id"] = df_weather["region"].map(region_map)

df_weather.to_sql("fact_weather", engine, if_exists="replace", index=False)

print("Star schema built!")