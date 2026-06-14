import bcrypt
from sqlalchemy import Column, Date, DateTime, Float, Integer, MetaData, String, Table, Time, create_engine, func, select
from sqlalchemy.orm import DeclarativeBase, Mapped, declarative_base, mapped_column
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timezone
from sqlalchemy.ext.hybrid import hybrid_property

DB_USERNAME = 'postgres'
DB_PASSWORD = '2409'

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

class User(Base):
    __tablename__ = 'users'
    user_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    _password_hash: Mapped[str] = mapped_column(String(128), nullable=False)
    
    @hybrid_property
    def password(self):
        """Prevent the password hash from being read directly."""
        raise AttributeError("Password is not a readable attribute.")

    @password.setter
    def password(self, plaintext_password: str):
        """Automatically salt and hash the password when it is set."""
        # Bcrypt requires bytes, so we encode the string
        password_bytes = plaintext_password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed_bytes = bcrypt.hashpw(password_bytes, salt)
        # Store as a decode string in the database
        self._password_hash = hashed_bytes.decode('utf-8')

    def check_password(self, plaintext_password: str) -> bool:
        """Verify the password against the stored hash."""
        password_bytes = plaintext_password.encode('utf-8')
        hash_bytes = self._password_hash.encode('utf-8')
        return bcrypt.checkpw(password_bytes, hash_bytes)
    
Base.metadata.create_all(engine, checkfirst=True)

def load_log(user_id):
    session.get()


# save_data(table, data)
#     if table==users
#         data['username']
# load_data()

async def save_log(conclusion:object):

    log = Log(
        # time= datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        user_id= conclusion['user_id'],
        expression= conclusion['expression'], 
        type= conclusion['type'],
        result= conclusion['result'],
    )
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

def create_user(username, password):
    user = User(username=username)
    user.password = password
    session.add(user)
    session.commit()

def get_user(username):
    statement = select(User).where(User.username == username)
    result = session.scalars(statement).first() 
    return result