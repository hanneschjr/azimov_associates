from .init_database import create_database_if_not_exists
from .init_tables import create_table_lawyers, create_table_processes #, create_table_process_lawyer

def init_db():
    create_database_if_not_exists()
    create_table_processes()
    create_table_lawyers()
    # create_table_process_lawyer()