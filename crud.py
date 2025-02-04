import json

FILE_PATH = "transactions.json"

def load_transactions():
    try:
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_transactions(transactions):
    with open(FILE_PATH, 'w') as file:
        json.dump(transactions, file, indent=4)

def add_transaction(transaction):
    transactions = load_transactions()
    transaction["id"] = len(transactions) + 1
    transactions.append(transaction)
    save_transactions(transactions)

def get_transactions():
    return load_transactions()

def update_transaction(transaction_id, updated_transaction):
    transactions = load_transactions()
    for t in transactions:
        if t["id"] == transaction_id:
            t.update(updated_transaction)
            break
    save_transactions(transactions)

def delete_transaction(transaction_id):
    transactions = load_transactions()
    transactions = [t for t in transactions if t["id"] != transaction_id]
    save_transactions(transactions)
