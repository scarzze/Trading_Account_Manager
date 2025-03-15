from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from datetime import datetime
from crud import User, Account, Transaction, Base

# Database setup
engine = create_engine("sqlite:///trading.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Clear existing data
session.query(Transaction).delete()
session.query(Account).delete()
session.query(User).delete()
session.commit()

# Seed users
user1 = User(username="scar_trader", email="scar@example.com")
user2 = User(username="gold_master", email="gold@example.com")
session.add_all([user1, user2])
session.commit()

# Seed accounts
account1 = Account(user_id=user1.id, balance=5000.0)
account2 = Account(user_id=user2.id, balance=10000.0)
session.add_all([account1, account2])
session.commit()

# Seed transactions
transactions = [
    Transaction(account_id=account1.id, amount=2000.0, type="deposit", timestamp=datetime.utcnow()),
    Transaction(account_id=account1.id, amount=1000.0, type="withdrawal", timestamp=datetime.utcnow()),
    Transaction(account_id=account2.id, amount=5000.0, type="deposit", timestamp=datetime.utcnow()),
    Transaction(account_id=account2.id, amount=2500.0, type="withdrawal", timestamp=datetime.utcnow()),
]

session.add_all(transactions)
session.commit()

print("✅ Database seeded successfully!")
session.close()
