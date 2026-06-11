from sqlalchemy import Column, Date, DateTime, Float, Integer, MetaData, String, Table, Time, create_engine, func, inspect
from sqlalchemy.orm import DeclarativeBase, Mapped, declarative_base, mapped_column
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timezone

DB_USERNAME = 'postgres'
DB_PASSWORD = '29022024'

engine = create_engine(f"postgresql+psycopg://{DB_USERNAME}:{DB_PASSWORD}@localhost:5432/postgres", echo=True)
    
Session = sessionmaker(bind=engine)
session = Session()

class Base(DeclarativeBase):
    pass

class Log(Base):
    __tablename__ = 'log'
    exp_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        server_default=func.now(),
        onupdate=func.now()
    )
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
    session.get()


# save_data(table, data)
#     if table==users
#         data['username']
# load_data()

async def save_log(conclusion:object):

    print('LOG TEST: ', conclusion)
    log = Log(
        time= datetime.now(timezone.utc),
        user_id= conclusion['user_id'],
        expression= conclusion['expression'],
        type= conclusion['type'],
        result= conclusion['result'],
    )
    print('LOG TEST: ', log)
    # exp_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # time: Mapped[datetime]
    # user_id: Mapped[int]
    # type: Mapped[str]
    # expression: Mapped[str]
    # result: Mapped[str]
    session.add(log)
    session.commit()
    
# log = Log(
#     user_id= conclusion['user_id'],
#     expression= conclusion['expression'],
#     type= conclusion['type'],
#     result= conclusion['result'],
# )

# save_log(log)