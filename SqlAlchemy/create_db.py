from sqlalchemy import create_engine, insert, select
from sqlalchemy_utils import database_exists, create_database
from config import settings
from models import metadata_obj, api_data_table

engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=False,
)

if not database_exists(url=engine.url):
    create_database(url=engine.url)


def create_table():
    metadata_obj.drop_all(engine)
    metadata_obj.create_all(engine)


create_table()
