import unittest
from crud import add_transaction, get_transactions, delete_transaction

class TestBudgetTracker(unittest.TestCase):
    def setUp(self):
        # Clear the transactions.json file for a clean test environment
        with open("transactions.json", "w") as file:
            file.write("[]")
        self.sample_transaction = {
            "type": "expense",
            "amount": 100,
            "description": "Groceries",
            "date": "2025-01-02"
        }

    def test_add_transaction(self):
        add_transaction(self.sample_transaction)
        transactions = get_transactions()
        self.assertEqual(len(transactions), 1)

    def test_delete_transaction(self):
        add_transaction(self.sample_transaction)
        delete_transaction(1)
        transactions = get_transactions()
        self.assertEqual(len(transactions), 0)

if __name__ == "__main__":
    unittest.main()
