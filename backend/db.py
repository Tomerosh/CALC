from sqlalchemy import Column, Date, Float, Integer, MetaData, String, Table, Time, create_engine, inspect
from sqlalchemy.orm import DeclarativeBase, Mapped, declarative_base, mapped_column
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql+psycopg://postgres:2409@localhost:5432/postgres", echo=True)

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
    exp_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int]
    type: Mapped[str]
    expression: Mapped[str]
    result: Mapped[float]
    # path: Mapped[list]

Base.metadata.create_all(engine)
# class User(Base):
#     __tablename__ = 'users'
#     user_id: Mapped[int]
#     username: Mapped[str]
#     hashed_password: Mapped[str]

def load_log(user_id):
    pass
def save_log(conclusion:dict):
    session.add(Log(
        user_id= conclusion['user_id'],
        expression= conclusion['expression'],
        type= conclusion['type'],
        result= conclusion['result'],
    ))
    session.commit()
