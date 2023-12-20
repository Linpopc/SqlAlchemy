from sqlalchemy import Table, Column, Integer, TIMESTAMP, MetaData, func

metadata_obj = MetaData()

api_data_table = Table(
    'api_data',
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("timestamp", TIMESTAMP, default=func.current_timestamp()),
    Column("value", Integer),
)
