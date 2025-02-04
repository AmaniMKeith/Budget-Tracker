from crud import add_transaction, get_transactions, update_transaction, delete_transaction

def display_menu():
    print("\nBudget Tracker Menu:")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. Update Transaction")
    print("4. Delete Transaction")
    print("5. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            type_ = input("Enter type (income/expense): ")
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            date = input("Enter date (YYYY-MM-DD): ")
            add_transaction({"type": type_, "amount": amount, "description": description, "date": date})
            print("Transaction added!")

        elif choice == "2":
            transactions = get_transactions()
            for t in transactions:
                print(t)

        elif choice == "3":
            transaction_id = int(input("Enter transaction ID to update: "))
            amount = float(input("Enter new amount: "))
            update_transaction(transaction_id, {"amount": amount})
            print("Transaction updated!")

        elif choice == "4":
            transaction_id = int(input("Enter transaction ID to delete: "))
            delete_transaction(transaction_id)
            print("Transaction deleted!")

        elif choice == "5":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
