from sqlalchemy.orm import sessionmaker
from datetime import datetime
from models import engine, Transaction  # Import your SQLAlchemy engine and Transaction model

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Find transactions with missing timestamps
transactions = session.query(Transaction).filter(Transaction.timestamp == None).all()

# Update missing timestamps
for txn in transactions:
    txn.timestamp = datetime.utcnow()  # Set current timestamp

# Commit changes
session.commit()
session.close()

print(f"✅ Updated {len(transactions)} transactions with missing timestamps.")
