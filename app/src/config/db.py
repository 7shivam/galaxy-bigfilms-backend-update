from sqlalchemy import create_engine, MetaData
import os

ipaddress = os.environ.get('IP_ADDRESS')
mysql_host_name = os.environ.get('HOST_NAME')
mysql_host_pass = os.environ.get('HOST_PASS')
database_name = os.environ.get('DATABASE')

engine = create_engine(f'mysql+pymysql://{mysql_host_name}:{mysql_host_pass}@{ipaddress}:3306/{database_name}')
meta = MetaData()
conn = engine.connect()