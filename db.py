import bcrypt
from sqlalchemy import Column, Date, DateTime, Float, Integer, MetaData, String, Table, Time, create_engine, func, select
from sqlalchemy.orm import DeclarativeBase, Mapped, declarative_base, mapped_column
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timezone
from sqlalchemy.ext.hybrid import hybrid_property

# INSERT DATABASE INFO HERE #
DB_NAME = 'postgres'
DB_USERNAME = 'postgres'
DB_PASSWORD = '29022024'

# Define db engine and session
engine = create_engine(f"postgresql+psycopg://{DB_USERNAME}:{DB_PASSWORD}@localhost:5432/{DB_NAME}", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Base class
class Base(DeclarativeBase):
    pass

# Log class
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
    score: Mapped[str]
    # path: Mapped[list]

# User class
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

# Get database session and close after finished
def get_db():
    db = Session()
    try:
        yield db  # This sends the session to your endpoint
    finally:
        db.close() 

# Load user logs by username
def load_logs(username):
    user_id = get_user(username).user_id
    print('USERID ==', user_id)
    logs = session.query(Log).where(Log.user_id == user_id).all()
    return logs

# Save expression conclusion to log table
async def save_log(conclusion:object):
    log = Log(
        user_id= conclusion['user_id'],
        expression= conclusion['expression'], 
        type= conclusion['type'],
        result= conclusion['result'],
        score= conclusion['score']
    )
    session.add(log)
    session.commit()
    
# Create user in users table
def create_user(username, password):
    if not get_user(username):
        user = User(username=username)
        user.password = password
        session.add(user)
        session.commit()

# Get user from users table
def get_user(username):
    
    statement = select(User).where(User.username == username)
    result = session.scalars(statement).first() 
    return session.query(User).where(User.username == username).first()


# save_data(table, data)
#     if table==users
#         data['username']
# load_data()