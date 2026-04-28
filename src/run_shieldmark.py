from validate_amount import process_transaction
from generate_transactions import generate_transactions

generate_transactions()
# print (transactions)

print("====================================")
print("   SHIELDMARK TRANSACTION REPORT")
print("====================================")

for transaction in generate_transactions():
    result = process_transaction(transaction)

    

    print("Employee: " + result["staff_name"] ) 
    print("Discrepancy: $" + str(result["discrepancy"]))
    print("Status: " + result["status"]) 
    print("ID: " + result["staff_id"])
    print("----------------------------------------------------")