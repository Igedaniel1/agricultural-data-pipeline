# End-to-End Agricultural Data Pipeline

A production-style data engineering project simulating Babban Gona's agricultural operations.

---

## Project Overview

This project builds a complete ETL pipeline that:

- Generates synthetic agricultural data
- Cleans and transforms raw CSV files
- Loads structured data into PostgreSQL
- Designs a Star Schema data warehouse
- Creates analytics-ready aggregate tables
- Implements data validation checks
- Documents system architecture

---

## Architecture

Raw CSV Data  
↓  
Data Cleaning (Pandas)  
↓  
PostgreSQL Staging  
↓  
Star Schema Warehouse  
↓  
Aggregated Analytics Tables  

---

## Tech Stack

- Python (Pandas, SQLAlchemy)
- PostgreSQL
- pgAdmin 4
- VS Code
- dotenv (secure config handling)

---

## Folder Structure

```
agri_pipeline/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── scripts/
│   ├── generate_data.py
│   ├── clean.py
│   ├── load.py
│   ├── build_star_schema.py
│   ├── validate.py
│   └── create_analytics.py
│
├── sql/
│   └── star_schema.sql
│
├── docs/
│   └── architecture.md
│
├── .env
├── requirements.txt
└── README.md
```

---

## Setup Instructions

### 1. Clone repository

```
git clone https://github.com/yourusername/agricultural-data-pipeline.git
cd agricultural-data-pipeline
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Create .env file

```
DATABASE_URL=postgresql://username:password@localhost:5432/agri_warehouse
```

### 4. Run Pipeline

```
python scripts/generate_data.py
python scripts/clean.py
python scripts/load.py
python scripts/build_star_schema.py
python scripts/validate.py
python scripts/create_analytics.py
```

---

## Data Warehouse Design

### Fact Tables
- fact_yields
- fact_loans

### Dimension Tables
- dim_farmers
- dim_region
- dim_weather

Schema type: Star Schema

---

## Data Quality Checks

- No negative yields
- Valid loan amounts
- Repayment rate validation
- Foreign key integrity checks

---

## Engineering Concepts Demonstrated

- ETL design
- Data modeling (Star Schema)
- PostgreSQL integration
- Data validation logic
- Environment variable security
- Project structuring for production

---

## Future Improvements

- Add Airflow orchestration
- Add Docker containerization
- Add Streamlit dashboard
- Deploy to AWS RDS
- CI/CD integration

---

## Author

Built as a professional data engineering portfolio project.