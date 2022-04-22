from sqlalchemy import create_engine, MetaData

engine = create_engine('mysql+pymysql://root:root@localhost:3306/s3_moviemasala_db')
meta = MetaData()
conn = engine.connect()