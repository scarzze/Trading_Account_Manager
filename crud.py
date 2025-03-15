from sqlalchemy.orm import sessionmaker
from models import engine, User, Account, Transaction,Base
from datetime import datetime

# Database session setup
Session = sessionmaker(bind=engine)

# Create
def add_user(username, email):
    with Session() as session:
        existing_user = session.query(User).filter_by(email=email).first()
        if existing_user:
            print(f"User with email {email} already exists")
            return None  

        user = User(username=username, email=email)
        session.add(user)
        session.commit()
        print(f"User {username} added")
        return user.id  

def add_account(user_id, balance=0.0):
    with Session() as session:
        user = session.query(User).filter_by(id=user_id).first()
        if not user:
            print(f"User ID {user_id} not found")
            return None

        account = Account(user_id=user_id, balance=balance)
        session.add(account)
        session.commit()
        print(f"Account created for {user.username} with balance {balance}")
        return account.id

def add_transaction(account_id, amount, trans_type):
    with Session() as session:
        account = session.query(Account).filter_by(id=account_id).first()
        if not account:
            print(f"Account ID {account_id} not found")
            return None

        if trans_type.lower() == "withdrawal" and account.balance < amount:
            print(f"Insufficient funds in account {account_id}")
            return None

        transaction = Transaction(account_id=account_id, amount=amount, type=trans_type, timestamp=datetime.utcnow())
        session.add(transaction)

        if trans_type.lower() == "deposit":
            account.balance += amount
        elif trans_type.lower() == "withdrawal":
            account.balance -= amount

        session.commit()
        print(f"{trans_type.capitalize()} of {amount} added to Account ID {account_id}")

# Fetch
def get_all_users():
    with Session() as session:
        users = session.query(User).all()
        if not users:
            print("No users found")
            return

        for user in users:
            print(f"ID: {user.id}, Username: {user.username}, Email: {user.email}")

def get_user_by_id(user_id):
    with Session() as session:
        user = session.query(User).filter_by(id=user_id).first()
        if user:
            print(f"User Found - ID: {user.id}, Username: {user.username}, Email: {user.email}")
            return user
        print("User not found")

def get_accounts_by_user(user_id):
    with Session() as session:
        accounts = session.query(Account).filter_by(user_id=user_id).all()
        if not accounts:
            print(f"No accounts found for user {user_id}")
            return

        for acc in accounts:
            print(f"Account ID: {acc.id}, Balance: {acc.balance}")

def get_transactions_by_account(account_id):
    with Session() as session:
        transactions = session.query(Transaction).filter_by(account_id=account_id).all()
        if not transactions:
            print(f"No transactions found for account {account_id}")
            return

        for txn in transactions:
            print(f"Transaction ID: {txn.id}, Amount: {txn.amount}, Type: {txn.type}, Date: {txn.timestamp}")

# Update
def update_user_email(user_id, new_email):
    with Session() as session:
        user = session.query(User).filter_by(id=user_id).first()
        if user:
            user.email = new_email
            session.commit()
            print(f"Updated email for {user.username} to {new_email}")
        else:
            print("User not found")

def update_account_balance(account_id, new_balance):
    with Session() as session:
        account = session.query(Account).filter_by(id=account_id).first()
        if account:
            account.balance = new_balance
            session.commit()
            print(f"Updated account {account_id} balance to {new_balance}")
        else:
            print("Account not found")

# Delete
def delete_user(user_id):
    with Session() as session:
        user = session.query(User).filter_by(id=user_id).first()
        if user:
            session.delete(user)
            session.commit()
            print(f"Deleted user {user.username}")
        else:
            print("User not found")

def delete_account(account_id):
    with Session() as session:
        account = session.query(Account).filter_by(id=account_id).first()
        if account:
            session.delete(account)
            session.commit()
            print(f"Deleted account {account_id}")
        else:
            print("Account not found")

def delete_transaction(transaction_id):
    with Session() as session:
        transaction = session.query(Transaction).filter_by(id=transaction_id).first()
        if transaction:
            session.delete(transaction)
            session.commit()
            print(f"Deleted transaction {transaction_id}")
        else:
            print("Transaction not found")

# Automate Seeding
def seed_data():
    print("\nSeeding Database...")

    user_id = add_user("scar_trader", "scar@example.com")
    if not user_id:
        user = get_user_by_id(1)  
        user_id = user.id

    account_id = add_account(user_id, 5000.0)
    if not account_id:
        accounts = get_accounts_by_user(user_id)  
        if accounts:
            account_id = accounts[0].id

    add_transaction(account_id, 2000.0, "deposit")
    add_transaction(account_id, 1000.0, "withdrawal")

    print("\nCurrent Users:")
    get_all_users()
    
    print("\nUser's Accounts:")
    get_accounts_by_user(user_id)

    print("\nAccount Transactions:")
    get_transactions_by_account(account_id)

if __name__ == "__main__":
    seed_data()
