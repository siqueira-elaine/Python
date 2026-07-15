from sqlalchemy import create_engine

import pandas

host = 'localhost'
user = 'root'
password = ''
database = 'pandas'

engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

print(pandas.read_sql("Select * from odontologia", con=engine))