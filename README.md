# Trading Account Manager

This is a command-line-based Trading Account Manager built using SQLAlchemy. It allows users to create accounts, perform transactions, and manage financial data efficiently.

## Features
- Add and manage users
- Create accounts for users
- Perform deposits and withdrawals
- Fetch user details, account balances, and transaction history
- Update user email and account balance
- Delete users, accounts, and transactions

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/scarzze/Trading_Account_Manager.git
   ```
2. Navigate to the project directory:
   ```sh
   cd Trading_Account_Manager
   ```
3. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
4. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
### 1. Database Setup
Run the following command to initialize the database:
```sh
python models.py
```
This will create the necessary tables.

### 2. Seeding the Database
To add sample data, run:
```sh
python seed.py
```

### 3. Command-Line Interface (CLI)
Execute commands using:
```sh
python cli.py [command] [arguments]
```
#### Available Commands:
- **Add a new user**:
  ```sh
  python cli.py add-user <username> <email>
  ```
- **Create an account for a user**:
  ```sh
  python cli.py add-account <user_id> <initial_balance>
  ```
- **Perform a transaction**:
  ```sh
  python cli.py add-transaction <account_id> <amount> <deposit/withdrawal>
  ```
- **List all users**:
  ```sh
  python cli.py list-users
  ```
- **Get user details**:
  ```sh
  python cli.py get-user <user_id>
  ```
- **Get user accounts**:
  ```sh
  python cli.py get-accounts <user_id>
  ```
- **Get transaction history**:
  ```sh
  python cli.py get-transactions <account_id>
  ```
- **Update user email**:
  ```sh
  python cli.py update-email <user_id> <new_email>
  ```
- **Update account balance**:
  ```sh
  python cli.py update-balance <account_id> <new_balance>
  ```
- **Delete a user**:
  ```sh
  python cli.py delete-user <user_id>
  ```
- **Delete an account**:
  ```sh
  python cli.py delete-account <account_id>
  ```
- **Delete a transaction**:
  ```sh
  python cli.py delete-transaction <transaction_id>
  ```

## Project Structure
```
Trading_Account_Manager/
│── cli.py            # Command-line interface
│── crud.py           # Database operations
│── models.py         # Database models
│── seed.py           # Seeding initial data
│── requirements.txt  # Dependencies
│── README.md         # Documentation
```

## Notes
- Ensure the database is set up before running any commands.
- Transactions will update account balances automatically.
- Use valid IDs for users, accounts, and transactions.

## License
This project is for business purposes.

## Made by Scar

