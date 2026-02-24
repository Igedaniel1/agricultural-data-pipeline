-- DIMENSION: FARMER
CREATE TABLE IF NOT EXISTS dim_farmer (
    farmer_id INT PRIMARY KEY,
    name TEXT,
    age INT,
    gender TEXT,
    region TEXT,
    registration_date DATE,
    age_bucket TEXT
);

-- DIMENSION: REGION
CREATE TABLE IF NOT EXISTS dim_region (
    region_id SERIAL PRIMARY KEY,
    region_name TEXT UNIQUE
);

-- DIMENSION: DATE
CREATE TABLE IF NOT EXISTS dim_date (
    date_id SERIAL PRIMARY KEY,
    date DATE UNIQUE,
    day INT,
    month INT,
    year INT,
    quarter INT
);

-- DIMENSION: CROP
CREATE TABLE IF NOT EXISTS dim_crop (
    crop_id SERIAL PRIMARY KEY,
    crop_name TEXT UNIQUE
);

-- FACT: YIELDS
CREATE TABLE IF NOT EXISTS fact_yields (
    yield_id INT PRIMARY KEY,
    farmer_id INT REFERENCES dim_farmer(farmer_id),
    crop_id INT REFERENCES dim_crop(crop_id),
    region_id INT REFERENCES dim_region(region_id),
    date_id INT REFERENCES dim_date(date_id),
    yield_kg NUMERIC,
    area_hectares NUMERIC,
    yield_per_hectare NUMERIC
);

-- FACT: LOANS
CREATE TABLE IF NOT EXISTS fact_loans (
    loan_id INT PRIMARY KEY,
    farmer_id INT REFERENCES dim_farmer(farmer_id),
    loan_amount NUMERIC,
    repaid_amount NUMERIC,
    repayment_rate NUMERIC,
    default_flag INT,
    disbursed_date DATE,
    disbursed_date_id INT REFERENCES dim_date(date_id)
);

-- FACT: WEATHER
CREATE TABLE IF NOT EXISTS fact_weather (
    weather_id INT PRIMARY KEY,
    region_id INT REFERENCES dim_region(region_id),
    date_id INT REFERENCES dim_date(date_id),
    rainfall_mm NUMERIC,
    temperature_c NUMERIC,
    rainfall_category TEXT
);