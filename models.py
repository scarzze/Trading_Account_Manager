from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime  # Import datetime for default timestamp

# Create database engine
engine = create_engine("sqlite:///trading.db") 
Base = declarative_base()

# User model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    accounts = relationship("Account", back_populates="user")

# Account model
class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    balance = Column(Float, default=0.0)
    user = relationship("User", back_populates="accounts")
    transactions = relationship("Transaction", back_populates="account")

# Transaction model
class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)
    amount = Column(Float, nullable=False)
    type = Column(String, nullable=False)  # "deposit" or "withdrawal"
    timestamp = Column(DateTime, default=datetime.utcnow)  

    account = relationship("Account", back_populates="transactions")

# Create tables
Base.metadata.create_all(engine)
