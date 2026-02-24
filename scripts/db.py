from sqlalchemy import create_engine

# Update with your password
DATABASE_URL = "postgresql://postgres:Igepostgres@localhost:5432/agri_warehouse"

engine = create_engine(DATABASE_URL)

print("Database engine created!")