from .init_database import create_database_if_not_exists
from .init_tables import create_tables

def init_db():
    create_database_if_not_exists()
    create_tables()