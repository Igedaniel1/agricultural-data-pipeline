import pandas as pd
from sqlalchemy import create_engine

# Database connection (update password)
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

# Load cleaned data
farmers = pd.read_csv("data/processed/farmers_clean.csv")
yields = pd.read_csv("data/processed/yields_clean.csv")
loans = pd.read_csv("data/processed/loans_clean.csv")
weather = pd.read_csv("data/processed/weather_clean.csv")

# Load to PostgreSQL (staging tables)
farmers.to_sql("staging_farmers", engine, if_exists="replace", index=False)
yields.to_sql("staging_yields", engine, if_exists="replace", index=False)
loans.to_sql("staging_loans", engine, if_exists="replace", index=False)
weather.to_sql("staging_weather", engine, if_exists="replace", index=False)

print("Data loaded to PostgreSQL!")