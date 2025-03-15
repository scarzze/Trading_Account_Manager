import argparse
from crud import (
    add_user, add_account, add_transaction, get_all_users, get_user_by_id,
    get_accounts_by_user, get_transactions_by_account, update_user_email,
    update_account_balance, delete_user, delete_account, delete_transaction
)

def main():
    parser = argparse.ArgumentParser(description="Trading Account Manager CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Add User
    user_parser = subparsers.add_parser("add-user", help="Add a new user")
    user_parser.add_argument("username", type=str, help="Username")
    user_parser.add_argument("email", type=str, help="Email")
    
    # Add Account
    account_parser = subparsers.add_parser("add-account", help="Add an account")
    account_parser.add_argument("user_id", type=int, help="User ID")
    account_parser.add_argument("balance", type=float, default=0.0, nargs="?", help="Initial balance")
    
    # Add Transaction
    transaction_parser = subparsers.add_parser("add-transaction", help="Add a transaction")
    transaction_parser.add_argument("account_id", type=int, help="Account ID")
    transaction_parser.add_argument("amount", type=float, help="Transaction amount")
    transaction_parser.add_argument("type", type=str, choices=["deposit", "withdrawal"], help="Transaction type")
    
    # Fetch Users
    subparsers.add_parser("list-users", help="List all users")
    
    # Get User by ID
    get_user_parser = subparsers.add_parser("get-user", help="Get user details")
    get_user_parser.add_argument("user_id", type=int, help="User ID")
    
    # Get Accounts by User
    get_accounts_parser = subparsers.add_parser("get-accounts", help="Get accounts for a user")
    get_accounts_parser.add_argument("user_id", type=int, help="User ID")
    
    # Get Transactions by Account
    get_transactions_parser = subparsers.add_parser("get-transactions", help="Get transactions for an account")
    get_transactions_parser.add_argument("account_id", type=int, help="Account ID")
    
    # Update User Email
    update_email_parser = subparsers.add_parser("update-email", help="Update user email")
    update_email_parser.add_argument("user_id", type=int, help="User ID")
    update_email_parser.add_argument("new_email", type=str, help="New Email")
    
    # Update Account Balance
    update_balance_parser = subparsers.add_parser("update-balance", help="Update account balance")
    update_balance_parser.add_argument("account_id", type=int, help="Account ID")
    update_balance_parser.add_argument("new_balance", type=float, help="New balance")
    
    # Delete User
    delete_user_parser = subparsers.add_parser("delete-user", help="Delete a user")
    delete_user_parser.add_argument("user_id", type=int, help="User ID")
    
    # Delete Account
    delete_account_parser = subparsers.add_parser("delete-account", help="Delete an account")
    delete_account_parser.add_argument("account_id", type=int, help="Account ID")
    
    # Delete Transaction
    delete_transaction_parser = subparsers.add_parser("delete-transaction", help="Delete a transaction")
    delete_transaction_parser.add_argument("transaction_id", type=int, help="Transaction ID")
    
    args = parser.parse_args()
    
    if args.command == "add-user":
        add_user(args.username, args.email)
    elif args.command == "add-account":
        add_account(args.user_id, args.balance)
    elif args.command == "add-transaction":
        add_transaction(args.account_id, args.amount, args.type)
    elif args.command == "list-users":
        get_all_users()
    elif args.command == "get-user":
        get_user_by_id(args.user_id)
    elif args.command == "get-accounts":
        get_accounts_by_user(args.user_id)
    elif args.command == "get-transactions":
        get_transactions_by_account(args.account_id)
    elif args.command == "update-email":
        update_user_email(args.user_id, args.new_email)
    elif args.command == "update-balance":
        update_account_balance(args.account_id, args.new_balance)
    elif args.command == "delete-user":
        delete_user(args.user_id)
    elif args.command == "delete-account":
        delete_account(args.account_id)
    elif args.command == "delete-transaction":
        delete_transaction(args.transaction_id)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
