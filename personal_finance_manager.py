import datetime

# Class for individual transactions
class Transaction:
    def __init__(self, amount, category, t_type):
        self.amount = amount
        self.category = category
        self.t_type = t_type  # "Income" or "Expense"
        self.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"{self.date} | {self.t_type}: {self.amount} | Category: {self.category}"


# Class to manage all finances
class FinanceManager:
    def __init__(self):
        self.transactions = []
        self.balance = 0.0

    def add_income(self, amount, category):
        if amount <= 0:
            print("❌ Income must be positive!")
            return
        self.transactions.append(Transaction(amount, category, "Income"))
        self.balance += amount
        print(f"✅ Income of {amount} added!")

    def add_expense(self, amount, category):
        if amount <= 0:
            print("❌ Expense must be positive!")
            return
        if amount > self.balance:
            print("❌ Insufficient balance for this expense!")
            return
        self.transactions.append(Transaction(amount, category, "Expense"))
        self.balance -= amount
        print(f"✅ Expense of {amount} added!")

    def view_transactions(self):
        if not self.transactions:
            print("📂 No transactions yet.")
        else:
            print("\n--- Transaction History ---")
            for t in self.transactions:
                print(t)

    def check_balance(self):
        print(f"💰 Current Balance: {self.balance}")


# Main Program
def main():
    fm = FinanceManager()

    while True:
        print("\n===== Personal Finance Manager =====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. Check Balance")
        print("5. Exit")
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                amt = float(input("Enter income amount: "))
                cat = input("Enter income category: ")
                fm.add_income(amt, cat)

            elif choice == "2":
                amt = float(input("Enter expense amount: "))
                cat = input("Enter expense category: ")
                fm.add_expense(amt, cat)

            elif choice == "3":
                fm.view_transactions()

            elif choice == "4":
                fm.check_balance()

            elif choice == "5":
                print("👋 Exiting Personal Finance Manager. Goodbye!")
                break

            else:
                print("❌ Invalid choice! Please enter 1–5.")

        except ValueError:
            print("❌ Please enter a valid number.")


if __name__ == "__main__":
    main()
