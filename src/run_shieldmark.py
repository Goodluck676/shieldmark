from validate_amount import process_transaction
from generate_transactions import generate_transactions

transactions = generate_transactions()
# print (transactions)

for transaction in transactions:
    result = process_transaction(transaction)

    print(result)