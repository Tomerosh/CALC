from sqlalchemy import Column, Date, Float, Integer, MetaData, String, Table, Time, create_engine, inspect
from sqlalchemy.orm import DeclarativeBase, Mapped, declarative_base, mapped_column
from sqlalchemy.orm import sessionmaker

DB_USERNAME = 'postgres'
DB_PASSWORD = '2409'

engine = create_engine(f"postgresql+psycopg://{DB_USERNAME}:{DB_PASSWORD}@localhost:5432/postgres", echo=True)

# CREATE LOG TABLE
# print(engine.dialect.has_table(engine.connect(), 'log'))
# if not inspect(engine).has_table('log'):  # If table don't exist, Create.
#     metadata = MetaData(engine)
#     # Create a table with the appropriate Columns
#     Table('log', metadata,
#           Column('exp_id', Integer, primary_key=True, nullable=False), 
#           Column('time', Time),
#           Column('user_id', Integer),
#           Column('expression', String),
#           Column('type', String),
#           Column('result', Float)
#     )
#     # Implement the creation
#     metadata.create_all()
    
Session = sessionmaker(bind=engine)
session = Session()

class Base(DeclarativeBase):
    pass

class Log(Base):
    __tablename__ = 'log'
    # time: Mapped[Time]
    exp_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int]
    type: Mapped[str]
    expression: Mapped[str]
    result: Mapped[str]
    # path: Mapped[list]

# class User(Base):
#     __tablename__ = 'users'
#     user_id: Mapped[int]
#     username: Mapped[str]
#     hashed_password: Mapped[str]

Base.metadata.create_all(engine)

def load_log(user_id):
    pass


# save_data(table, data)
#     if table==users
#         data['username']
# load_data()

def save_log(conclusion:object):
    session.add(log)
    session.commit()
    
# log = Log(
#     user_id= conclusion['user_id'],
#     expression= conclusion['expression'],
#     type= conclusion['type'],
#     result= conclusion['result'],
# )

# save_log(log)